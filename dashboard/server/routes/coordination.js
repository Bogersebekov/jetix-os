import { Router } from 'express';
import fs from 'node:fs/promises';
import path from 'node:path';
import matter from 'gray-matter';

const ROSTER = {
  manager: 'MGMT',
  strategist: 'MGMT',
  'personal-assistant': 'OPS',
  'system-admin': 'OPS',
  'sales-lead': 'Sales',
  'sales-researcher': 'Sales',
  'sales-outreach': 'Sales',
  'sales-team': 'Sales',
  'inbox-processor': 'Brain',
  'knowledge-synth': 'Brain',
  'research-team': 'Brain',
  'content-team': 'Brain',
  'crazy-agent': 'Meta',
  'meta-agent': 'Meta',
  'life-coach': 'Life',
};

const DEPT_ORDER = ['MGMT', 'OPS', 'Sales', 'Brain', 'Meta', 'Life'];

async function readAgentFrontmatter(dir, agentId) {
  for (const p of [path.join(dir, agentId, 'baseline.md'), path.join(dir, `${agentId}.md`)]) {
    try {
      const raw = await fs.readFile(p, 'utf-8');
      return matter(raw).data;
    } catch {}
  }
  return null;
}

async function readJsonl(file) {
  try {
    const raw = await fs.readFile(file, 'utf-8');
    const lines = raw.split('\n').filter((l) => l.trim());
    return lines.map((l) => {
      try { return JSON.parse(l); } catch { return null; }
    }).filter(Boolean);
  } catch (e) {
    if (e.code === 'ENOENT') return [];
    throw e;
  }
}

export default function coordinationRoute(JETIX_ROOT) {
  const router = Router();

  router.get('/', async (_req, res) => {
    try {
      const agentsDir = path.join(JETIX_ROOT, 'agents');
      const mailboxDir = path.join(JETIX_ROOT, 'comms/mailboxes');

      let agentEntries = [];
      try { agentEntries = await fs.readdir(agentsDir, { withFileTypes: true }); } catch {}

      const agentIds = new Set();
      for (const e of agentEntries) {
        if (e.name.startsWith('_') || e.name.startsWith('.')) continue;
        if (e.isDirectory()) agentIds.add(e.name);
        else if (e.isFile() && e.name.endsWith('.md')) agentIds.add(e.name.replace(/\.md$/, ''));
      }
      for (const n of Object.keys(ROSTER)) agentIds.add(n);

      const agents = [];
      const allMessages = [];

      for (const id of agentIds) {
        const fm = (await readAgentFrontmatter(agentsDir, id)) || {};
        const msgs = await readJsonl(path.join(mailboxDir, `${id}.jsonl`));
        const last = msgs.length ? msgs[msgs.length - 1] : null;
        agents.push({
          id,
          name: fm.name || id,
          model: fm.model || null,
          department: fm.department || fm.dept || ROSTER[id] || 'Other',
          function: fm.function || fm.role || null,
          status: fm.status || null,
          last_message: last,
        });
        for (const m of msgs) {
          allMessages.push({
            timestamp: m.timestamp || '',
            from: m.from || '—',
            to: m.to || id,
            subject: m.subject || m.type || '',
          });
        }
      }

      const humanMsgs = await readJsonl(path.join(mailboxDir, 'human.jsonl'));
      for (const m of humanMsgs) {
        allMessages.push({
          timestamp: m.timestamp || '',
          from: m.from || '—',
          to: m.to || 'human',
          subject: m.subject || m.type || '',
        });
      }

      allMessages.sort((a, b) => (a.timestamp < b.timestamp ? 1 : a.timestamp > b.timestamp ? -1 : 0));
      const recent_activity = allMessages.slice(0, 20);

      const byDept = new Map();
      for (const a of agents) {
        const d = a.department;
        if (!byDept.has(d)) byDept.set(d, []);
        byDept.get(d).push(a.id);
      }
      const departments = [...DEPT_ORDER, ...[...byDept.keys()].filter((d) => !DEPT_ORDER.includes(d))]
        .filter((d) => byDept.has(d))
        .map((name) => {
          const ids = byDept.get(name);
          const active = agents.filter(
            (a) => ids.includes(a.id) && ['working', 'busy', 'active'].includes((a.status || '').toLowerCase())
          ).length;
          return { name, agents: ids, active };
        });

      res.json({ departments, agents, recent_activity });
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  return router;
}
