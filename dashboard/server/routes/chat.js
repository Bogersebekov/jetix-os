import { Router } from 'express';
import fs from 'node:fs/promises';
import path from 'node:path';

const ROSTER = {
  manager: 'MGMT',
  strategist: 'MGMT',
  'personal-assistant': 'OPS',
  'system-admin': 'OPS',
  'sales-lead': 'Sales',
  'sales-researcher': 'Sales',
  'sales-outreach': 'Sales',
  'inbox-processor': 'Brain',
  'knowledge-synth': 'Brain',
  'crazy-agent': 'Meta',
  'meta-agent': 'Meta',
  'life-coach': 'Life',
};

function mailboxPath(JETIX_ROOT, name) {
  return path.join(JETIX_ROOT, 'comms/mailboxes', `${name}.jsonl`);
}

function isSafeName(name) {
  return typeof name === 'string' && /^[a-z0-9][a-z0-9-_]*$/i.test(name);
}

async function readJsonl(file) {
  try {
    const raw = await fs.readFile(file, 'utf-8');
    const lines = raw.split('\n').filter(Boolean);
    const out = [];
    for (const l of lines) {
      try { out.push(JSON.parse(l)); } catch {}
    }
    return out;
  } catch (e) {
    if (e.code === 'ENOENT') return [];
    throw e;
  }
}

async function appendJsonl(file, obj) {
  await fs.mkdir(path.dirname(file), { recursive: true });
  await fs.appendFile(file, JSON.stringify(obj) + '\n', 'utf-8');
}

async function listAgents(JETIX_ROOT) {
  const dir = path.join(JETIX_ROOT, 'comms/mailboxes');
  let files = [];
  try { files = await fs.readdir(dir); } catch { files = []; }
  const names = new Set([...Object.keys(ROSTER)]);
  for (const f of files) {
    if (f.endsWith('.jsonl') && f !== 'human.jsonl') {
      names.add(f.replace(/\.jsonl$/, ''));
    }
  }
  return Array.from(names).sort();
}

export default function chatRoute(JETIX_ROOT) {
  const router = Router();

  router.get('/agents', async (_req, res) => {
    try {
      const names = await listAgents(JETIX_ROOT);
      const agents = await Promise.all(
        names.map(async (name) => {
          const msgs = await readJsonl(mailboxPath(JETIX_ROOT, name));
          const unread = msgs.filter((m) => m.status === 'pending' || m.status === 'unread').length;
          return { name, department: ROSTER[name] || 'Other', unread, total: msgs.length };
        })
      );
      res.json({ agents });
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  router.get('/mailbox/:agent', async (req, res) => {
    try {
      const { agent } = req.params;
      if (!isSafeName(agent)) return res.status(400).json({ error: 'bad name' });
      const msgs = await readJsonl(mailboxPath(JETIX_ROOT, agent));
      res.json({ agent, total: msgs.length, messages: msgs.slice(-50) });
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  router.get('/human', async (_req, res) => {
    try {
      const msgs = await readJsonl(mailboxPath(JETIX_ROOT, 'human'));
      res.json({ agent: 'human', total: msgs.length, messages: msgs.slice(-50) });
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  router.post('/send', async (req, res) => {
    try {
      const { to, from = 'human', subject = '', content = '', priority = 'normal' } = req.body || {};
      if (!isSafeName(to)) return res.status(400).json({ error: 'invalid "to"' });
      if (!content.trim()) return res.status(400).json({ error: 'content required' });

      const now = new Date();
      const ymd = now.toISOString().slice(0, 10).replace(/-/g, '');
      const file = mailboxPath(JETIX_ROOT, to);
      const existing = await readJsonl(file);
      const todayCount = existing.filter((m) => (m.id || '').startsWith(`msg-${ymd}-`)).length;
      const seq = String(todayCount + 1).padStart(3, '0');

      const msg = {
        id: `msg-${ymd}-${seq}`,
        timestamp: now.toISOString(),
        from,
        to,
        type: 'message',
        priority,
        subject,
        body: content,
        status: 'pending',
      };
      await appendJsonl(file, msg);
      res.json({ ok: true, message: msg });
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  return router;
}
