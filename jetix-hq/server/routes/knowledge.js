import { Router } from 'express';
import { readdirSync, readFileSync, statSync, existsSync } from 'fs';
import { join, relative, extname, basename } from 'path';
import config from '../config.js';

const router = Router();
const MAX_FILE_SIZE = 1024 * 1024; // 1MB

function getKbRoot() {
  return process.env.OBSIDIAN_PATH || config.jetixRoot;
}

function buildTree(dir, root, depth = 0) {
  if (depth > 6) return [];
  if (!existsSync(dir)) return [];

  const entries = readdirSync(dir, { withFileTypes: true })
    .filter((e) => !e.name.startsWith('.') && !e.name.startsWith('node_modules') && e.name !== 'data')
    .sort((a, b) => {
      if (a.isDirectory() && !b.isDirectory()) return -1;
      if (!a.isDirectory() && b.isDirectory()) return 1;
      return a.name.localeCompare(b.name);
    });

  return entries.map((entry) => {
    const fullPath = join(dir, entry.name);
    const relPath = relative(root, fullPath);

    if (entry.isDirectory()) {
      return {
        name: entry.name,
        path: relPath,
        type: 'directory',
        children: buildTree(fullPath, root, depth + 1),
      };
    }

    if (extname(entry.name) !== '.md') return null;

    const stat = statSync(fullPath);
    return {
      name: entry.name,
      path: relPath,
      type: 'file',
      size: stat.size,
      modified: stat.mtime.toISOString(),
    };
  }).filter(Boolean);
}

function extractWikilinks(content) {
  const links = [];
  const regex = /\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g;
  let match;
  while ((match = regex.exec(content))) {
    links.push(match[1].trim());
  }
  return [...new Set(links)];
}

function extractFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  const fm = {};
  match[1].split('\n').forEach((line) => {
    const [key, ...rest] = line.split(':');
    if (key && rest.length) fm[key.trim()] = rest.join(':').trim();
  });
  return fm;
}

// GET /api/v1/knowledge/tree
router.get('/tree', (req, res) => {
  const root = getKbRoot();
  const tree = buildTree(root, root);
  res.json({ root: root.split('/').pop(), tree });
});

// GET /api/v1/knowledge/file?path=relative/path.md
router.get('/file', (req, res) => {
  const filePath = req.query.path;
  if (!filePath) return res.status(400).json({ error: 'path required' });

  const root = getKbRoot();
  const full = join(root, filePath);

  // Security: prevent path traversal
  if (!full.startsWith(root)) return res.status(403).json({ error: 'Access denied' });
  if (!existsSync(full)) return res.status(404).json({ error: 'File not found' });

  const stat = statSync(full);
  if (stat.size > MAX_FILE_SIZE) {
    return res.json({
      path: filePath,
      name: basename(filePath),
      content: null,
      tooLarge: true,
      size: stat.size,
    });
  }

  const content = readFileSync(full, 'utf-8');
  const frontmatter = extractFrontmatter(content);
  const wikilinks = extractWikilinks(content);
  const wordCount = content.split(/\s+/).filter(Boolean).length;

  res.json({
    path: filePath,
    name: basename(filePath),
    content,
    frontmatter,
    wikilinks,
    wordCount,
    size: stat.size,
    modified: stat.mtime.toISOString(),
    tooLarge: false,
  });
});

// GET /api/v1/knowledge/search?q=query
router.get('/search', (req, res) => {
  const query = (req.query.q || '').toLowerCase().trim();
  if (!query) return res.json({ results: [] });

  const root = getKbRoot();
  const results = [];

  function searchDir(dir, depth) {
    if (depth > 5 || results.length >= 20) return;
    if (!existsSync(dir)) return;

    const entries = readdirSync(dir, { withFileTypes: true })
      .filter((e) => !e.name.startsWith('.') && !e.name.startsWith('node_modules'));

    for (const entry of entries) {
      if (results.length >= 20) break;
      const full = join(dir, entry.name);

      if (entry.isDirectory()) {
        searchDir(full, depth + 1);
        continue;
      }

      if (extname(entry.name) !== '.md') continue;
      const relPath = relative(root, full);

      // Match filename
      if (entry.name.toLowerCase().includes(query)) {
        const stat = statSync(full);
        if (stat.size <= MAX_FILE_SIZE) {
          const content = readFileSync(full, 'utf-8');
          const snippet = extractSnippet(content, query);
          results.push({ path: relPath, name: entry.name, snippet, matchType: 'filename' });
        }
        continue;
      }

      // Match content
      const stat = statSync(full);
      if (stat.size > MAX_FILE_SIZE) continue;
      const content = readFileSync(full, 'utf-8');
      if (content.toLowerCase().includes(query)) {
        const snippet = extractSnippet(content, query);
        results.push({ path: relPath, name: entry.name, snippet, matchType: 'content' });
      }
    }
  }

  searchDir(root, 0);
  res.json({ results, query });
});

function extractSnippet(content, query, len = 120) {
  const lower = content.toLowerCase();
  const idx = lower.indexOf(query);
  if (idx === -1) return content.slice(0, len) + '...';
  const start = Math.max(0, idx - 40);
  const end = Math.min(content.length, idx + query.length + 80);
  return (start > 0 ? '...' : '') + content.slice(start, end) + (end < content.length ? '...' : '');
}

// GET /api/v1/knowledge/graph
router.get('/graph', (req, res) => {
  const root = getKbRoot();
  const nodes = [];
  const edgeSet = new Set();
  const fileMap = new Map(); // basename (no ext) → path

  function scanDir(dir, depth) {
    if (depth > 5) return;
    if (!existsSync(dir)) return;

    const entries = readdirSync(dir, { withFileTypes: true })
      .filter((e) => !e.name.startsWith('.') && !e.name.startsWith('node_modules'));

    for (const entry of entries) {
      const full = join(dir, entry.name);
      if (entry.isDirectory()) { scanDir(full, depth + 1); continue; }
      if (extname(entry.name) !== '.md') continue;

      const relPath = relative(root, full);
      const name = basename(entry.name, '.md');
      fileMap.set(name.toLowerCase(), relPath);

      const stat = statSync(full);
      let linkCount = 0;
      if (stat.size <= MAX_FILE_SIZE) {
        const content = readFileSync(full, 'utf-8');
        const links = extractWikilinks(content);
        linkCount = links.length;
        for (const link of links) {
          edgeSet.add(JSON.stringify([relPath, link.toLowerCase()]));
        }
      }

      nodes.push({ id: relPath, label: name, links: linkCount });
    }
  }

  scanDir(root, 0);

  // Resolve edges
  const edges = [];
  for (const raw of edgeSet) {
    const [source, targetName] = JSON.parse(raw);
    const target = fileMap.get(targetName);
    if (target && target !== source) {
      edges.push({ source, target });
    }
  }

  res.json({ nodes, edges });
});

export default router;
