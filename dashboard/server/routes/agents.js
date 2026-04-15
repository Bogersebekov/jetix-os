import { Router } from 'express';
import fs from 'node:fs/promises';
import path from 'node:path';
import matter from 'gray-matter';

async function readAgentFrontmatter(dir, agentId) {
  const candidates = [
    path.join(dir, agentId, 'baseline.md'),
    path.join(dir, `${agentId}.md`),
  ];
  for (const p of candidates) {
    try {
      const raw = await fs.readFile(p, 'utf-8');
      const parsed = matter(raw);
      return { file: p, data: parsed.data };
    } catch {}
  }
  return null;
}

async function lastMailboxMessage(JETIX_ROOT, agentId) {
  const file = path.join(JETIX_ROOT, 'comms/mailboxes', `${agentId}.jsonl`);
  try {
    const raw = await fs.readFile(file, 'utf-8');
    const lines = raw.split('\n').filter((l) => l.trim());
    if (!lines.length) return null;
    try { return JSON.parse(lines[lines.length - 1]); } catch { return { raw: lines[lines.length - 1] }; }
  } catch {
    return null;
  }
}

export default function agentsRoute(JETIX_ROOT) {
  const router = Router();

  router.get('/', async (_req, res) => {
    try {
      const dir = path.join(JETIX_ROOT, 'agents');
      const entries = await fs.readdir(dir, { withFileTypes: true });
      const agents = [];
      for (const entry of entries) {
        if (entry.name.startsWith('_') || entry.name.startsWith('.')) continue;
        let agentId;
        if (entry.isDirectory()) agentId = entry.name;
        else if (entry.isFile() && entry.name.endsWith('.md')) agentId = entry.name.replace(/\.md$/, '');
        else continue;

        const fm = await readAgentFrontmatter(dir, agentId);
        const lastMsg = await lastMailboxMessage(JETIX_ROOT, agentId);
        const data = fm?.data || {};
        agents.push({
          id: agentId,
          name: data.name || agentId,
          model: data.model || null,
          department: data.department || data.dept || null,
          function: data.function || data.role || null,
          status: data.status || null,
          file: fm ? path.relative(JETIX_ROOT, fm.file) : null,
          last_message: lastMsg,
        });
      }
      res.json({ agents });
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  router.get('/:name/mailbox', async (req, res) => {
    const name = req.params.name.replace(/[^a-zA-Z0-9_-]/g, '');
    const file = path.join(JETIX_ROOT, 'comms/mailboxes', `${name}.jsonl`);
    try {
      const raw = await fs.readFile(file, 'utf-8');
      const lines = raw.split('\n').filter((l) => l.trim());
      const last = lines.slice(-20).map((l) => {
        try { return JSON.parse(l); } catch { return { raw: l }; }
      });
      res.json({ agent: name, total: lines.length, messages: last });
    } catch (e) {
      if (e.code === 'ENOENT') return res.json({ agent: name, total: 0, messages: [] });
      res.status(500).json({ error: e.message });
    }
  });

  return router;
}
