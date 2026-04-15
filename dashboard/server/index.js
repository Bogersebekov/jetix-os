import express from 'express';
import cors from 'cors';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const JETIX_ROOT = process.env.JETIX_ROOT
  ? path.resolve(process.env.JETIX_ROOT)
  : path.resolve(__dirname, '..', '..');
const PORT = Number(process.env.PORT || 3001);

const app = express();
app.use(cors({ origin: ['http://localhost:3000', /^http:\/\/\d+\.\d+\.\d+\.\d+:3000$/] }));
app.use(express.json());

app.get('/api/health', (_req, res) => {
  res.json({ status: 'ok', jetix_root: JETIX_ROOT, timestamp: new Date().toISOString() });
});

app.get('/api/projects', async (_req, res) => {
  try {
    const data = await fs.readFile(path.join(JETIX_ROOT, 'config/projects.json'), 'utf-8');
    res.json(JSON.parse(data));
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/api/decisions', async (_req, res) => {
  try {
    const data = await fs.readFile(path.join(JETIX_ROOT, 'config/decisions.json'), 'utf-8');
    res.json(JSON.parse(data));
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/api/agents', async (_req, res) => {
  try {
    const dir = path.join(JETIX_ROOT, 'agents');
    const entries = await fs.readdir(dir, { withFileTypes: true });
    const agents = [];
    for (const entry of entries) {
      if (entry.name.startsWith('_')) continue;
      const agentId = entry.name;
      let baselinePath;
      if (entry.isDirectory()) {
        baselinePath = path.join(dir, agentId, 'baseline.md');
      } else if (entry.isFile() && entry.name.endsWith('.md')) {
        baselinePath = path.join(dir, entry.name);
      } else {
        continue;
      }
      try {
        const raw = await fs.readFile(baselinePath, 'utf-8');
        const parsed = matter(raw);
        agents.push({
          id: agentId.replace(/\.md$/, ''),
          file: path.relative(JETIX_ROOT, baselinePath),
          ...parsed.data,
        });
      } catch {
        agents.push({ id: agentId, file: null, missing: true });
      }
    }
    res.json({ agents });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/api/mailboxes/:agent', async (req, res) => {
  try {
    const agent = req.params.agent.replace(/[^a-zA-Z0-9_-]/g, '');
    const file = path.join(JETIX_ROOT, 'comms/mailboxes', `${agent}.jsonl`);
    const raw = await fs.readFile(file, 'utf-8');
    const lines = raw.split('\n').filter((l) => l.trim());
    const last = lines.slice(-20).map((l) => {
      try { return JSON.parse(l); } catch { return { raw: l }; }
    });
    res.json({ agent, messages: last, total: lines.length });
  } catch (e) {
    if (e.code === 'ENOENT') return res.json({ agent: req.params.agent, messages: [], total: 0 });
    res.status(500).json({ error: e.message });
  }
});

app.get('/api/state/:file', async (req, res) => {
  try {
    const name = req.params.file.replace(/[^a-zA-Z0-9._-]/g, '');
    const full = path.join(JETIX_ROOT, 'shared/state', name);
    const raw = await fs.readFile(full, 'utf-8');
    if (name.endsWith('.json')) {
      res.json(JSON.parse(raw));
    } else {
      res.type('text/plain').send(raw);
    }
  } catch (e) {
    if (e.code === 'ENOENT') return res.status(404).json({ error: 'not found' });
    res.status(500).json({ error: e.message });
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`[jetix-dashboard-server] listening on :${PORT}, JETIX_ROOT=${JETIX_ROOT}`);
});
