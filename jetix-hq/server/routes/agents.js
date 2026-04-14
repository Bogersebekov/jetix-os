import { Router } from 'express';
import { readFileSync, existsSync } from 'fs';
import { join } from 'path';
import config from '../config.js';

const router = Router();

const AGENT_DEFS = [
  { id: 'manager', name: 'Manager', dept: 'MGMT', model: 'Sonnet 4.6', phase: 1 },
  { id: 'personal-assistant', name: 'Personal Assistant', dept: 'OPS', model: 'Haiku 4.5', phase: 1 },
  { id: 'system-admin', name: 'System Admin', dept: 'OPS', model: 'Haiku 4.5', phase: 1 },
  { id: 'sales-lead', name: 'Sales Lead', dept: 'SALES', model: 'Sonnet 4.6', phase: 2 },
  { id: 'sales-researcher', name: 'Sales Researcher', dept: 'SALES', model: 'Haiku 4.5', phase: 2 },
  { id: 'sales-outreach', name: 'Sales Outreach', dept: 'SALES', model: 'Haiku 4.5', phase: 2 },
  { id: 'inbox-processor', name: 'Inbox Processor', dept: 'BRAIN', model: 'Haiku 4.5', phase: 2 },
  { id: 'crazy-agent', name: 'Crazy Agent', dept: 'META', model: 'Sonnet 4.6', phase: 2 },
  { id: 'knowledge-synth', name: 'Knowledge Synth', dept: 'BRAIN', model: 'Sonnet 4.6', phase: 3 },
  { id: 'strategist', name: 'Strategist', dept: 'MGMT', model: 'Opus 4.6', phase: 3 },
  { id: 'life-coach', name: 'Life Coach', dept: 'LIFE', model: 'Sonnet 4.6', phase: 4 },
  { id: 'meta-agent', name: 'Meta Agent', dept: 'META', model: 'Sonnet 4.6', phase: 4 },
];

function readMailbox(agentId) {
  const mailboxPath = join(config.paths.mailboxes(), `${agentId}.jsonl`);
  if (!existsSync(mailboxPath)) return [];
  const content = readFileSync(mailboxPath, 'utf-8').trim();
  if (!content) return [];
  return content.split('\n').map((line) => {
    try { return JSON.parse(line); } catch { return null; }
  }).filter(Boolean);
}

function readAgentPrompt(agentId) {
  const promptPath = join(config.jetixRoot, '.claude', 'agents', `${agentId}.md`);
  if (!existsSync(promptPath)) return null;
  return readFileSync(promptPath, 'utf-8');
}

// GET /api/v1/agents — list all agents with status
router.get('/', (req, res) => {
  const agents = AGENT_DEFS.map((def) => {
    const messages = readMailbox(def.id);
    const unread = messages.filter((m) => m.status === 'pending').length;
    return {
      ...def,
      status: 'offline',
      level: 1,
      xp: 0,
      xpToNext: 100,
      currentTask: null,
      unreadMessages: unread,
      totalMessages: messages.length,
      tasksToday: 0,
      tokensToday: 0,
      costToday: 0,
      errorRate: 0,
      avgTaskTime: 0,
    };
  });
  res.json({ agents });
});

// GET /api/v1/agents/:id — agent detail
router.get('/:id', (req, res) => {
  const def = AGENT_DEFS.find((a) => a.id === req.params.id);
  if (!def) return res.status(404).json({ error: 'Agent not found' });

  const messages = readMailbox(def.id);
  const unread = messages.filter((m) => m.status === 'pending').length;
  const prompt = readAgentPrompt(def.id);

  res.json({
    ...def,
    status: 'offline',
    level: 1,
    xp: 0,
    xpToNext: 100,
    currentTask: null,
    unreadMessages: unread,
    messages: messages.slice(-50).reverse(),
    queue: [],
    config: {
      systemPrompt: prompt,
      maxTurns: prompt?.match(/maxTurns:\s*(\d+)/)?.[1] || '30',
      permissionMode: prompt?.match(/permissionMode:\s*(\w+)/)?.[1] || 'auto',
    },
    metrics: {
      tasksToday: 0,
      tokensToday: 0,
      costToday: 0,
      avgTaskTime: 0,
      errorRate: 0,
      tokenHistory: Array.from({ length: 14 }, (_, i) => ({
        date: new Date(Date.now() - (13 - i) * 86400000).toISOString().slice(0, 10),
        tokens: 0,
        cost: 0,
      })),
      recentTasks: [],
    },
  });
});

// GET /api/v1/agents/:id/mailbox
router.get('/:id/mailbox', (req, res) => {
  const def = AGENT_DEFS.find((a) => a.id === req.params.id);
  if (!def) return res.status(404).json({ error: 'Agent not found' });
  const messages = readMailbox(def.id);
  const limit = parseInt(req.query.limit) || 50;
  const offset = parseInt(req.query.offset) || 0;
  res.json({
    messages: messages.slice().reverse().slice(offset, offset + limit),
    total: messages.length,
  });
});

export default router;
