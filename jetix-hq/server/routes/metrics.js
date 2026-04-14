import { Router } from 'express';

const router = Router();

const AGENTS = [
  { id: 'manager', name: 'Manager', dept: 'MGMT' },
  { id: 'personal-assistant', name: 'Personal Assistant', dept: 'OPS' },
  { id: 'system-admin', name: 'System Admin', dept: 'OPS' },
  { id: 'sales-lead', name: 'Sales Lead', dept: 'SALES' },
  { id: 'sales-researcher', name: 'Sales Researcher', dept: 'SALES' },
  { id: 'sales-outreach', name: 'Sales Outreach', dept: 'SALES' },
  { id: 'inbox-processor', name: 'Inbox Processor', dept: 'BRAIN' },
  { id: 'crazy-agent', name: 'Crazy Agent', dept: 'META' },
  { id: 'knowledge-synth', name: 'Knowledge Synth', dept: 'BRAIN' },
  { id: 'strategist', name: 'Strategist', dept: 'MGMT' },
  { id: 'life-coach', name: 'Life Coach', dept: 'LIFE' },
  { id: 'meta-agent', name: 'Meta Agent', dept: 'META' },
];

// Seeded pseudo-random for deterministic mock data
function seededRandom(seed) {
  let s = seed;
  return () => {
    s = (s * 16807 + 0) % 2147483647;
    return (s - 1) / 2147483646;
  };
}

function generateTimeSeries(days, seed) {
  const rand = seededRandom(seed);
  const now = new Date();
  return Array.from({ length: days }, (_, i) => {
    const date = new Date(now);
    date.setDate(date.getDate() - (days - 1 - i));
    const dateStr = date.toISOString().slice(0, 10);
    const totalTokens = Math.floor(rand() * 45000 + 5000);
    const inputTokens = Math.floor(totalTokens * (0.6 + rand() * 0.2));
    const outputTokens = totalTokens - inputTokens;
    const cost = +(totalTokens * 0.000008 + outputTokens * 0.000024).toFixed(4);
    const sessions = Math.floor(rand() * 8 + 2);
    const errors = rand() < 0.15 ? Math.floor(rand() * 3 + 1) : 0;
    return { date: dateStr, tokens: totalTokens, inputTokens, outputTokens, cost, sessions, errors };
  });
}

function generateAgentTokens(seed) {
  const rand = seededRandom(seed);
  return AGENTS.map((a) => {
    const weight = a.id === 'manager' ? 3 : a.id === 'strategist' ? 2.5 : a.id === 'sales-lead' ? 2 : 1;
    const input = Math.floor((rand() * 8000 + 2000) * weight);
    const output = Math.floor((rand() * 4000 + 1000) * weight);
    return { id: a.id, name: a.name, dept: a.dept, inputTokens: input, outputTokens: output, total: input + output };
  }).sort((a, b) => b.total - a.total);
}

function generateSessions(seed) {
  const rand = seededRandom(seed);
  const statuses = ['running', 'completed', 'completed', 'completed', 'error'];
  return AGENTS.slice(0, 6).map((a, i) => {
    const status = statuses[Math.floor(rand() * statuses.length)];
    const duration = status === 'running' ? Math.floor(rand() * 180 + 10) : Math.floor(rand() * 300 + 30);
    const tokens = Math.floor(rand() * 12000 + 1000);
    return {
      id: `session-${i}`,
      agent: a.name,
      agentId: a.id,
      task: ['Morning pipeline', 'Research prospects', 'Process inbox', 'Generate briefing', 'Outreach sequence', 'Health check'][i],
      duration,
      tokens,
      status,
      startedAt: new Date(Date.now() - duration * 1000).toISOString(),
    };
  });
}

function generateErrors(seed) {
  const rand = seededRandom(seed);
  const severities = ['warning', 'warning', 'warning', 'error', 'error'];
  const messages = [
    'Timeout waiting for Notion API response',
    'Mailbox write failed: disk full simulation',
    'Agent exceeded maxTurns limit',
    'Schema validation failed for outgoing message',
    'MCP connection dropped, reconnecting',
    'Rate limit approached: 80% of quota',
  ];
  return Array.from({ length: 4 }, (_, i) => ({
    id: `err-${i}`,
    severity: severities[Math.floor(rand() * severities.length)],
    agent: AGENTS[Math.floor(rand() * AGENTS.length)].name,
    message: messages[Math.floor(rand() * messages.length)],
    timestamp: new Date(Date.now() - Math.floor(rand() * 86400000)).toISOString(),
  })).sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
}

// GET /api/v1/metrics?period=today|week|month
router.get('/', (req, res) => {
  const period = req.query.period || 'today';
  const days = period === 'today' ? 1 : period === 'week' ? 7 : 30;
  const seed = period === 'today' ? 42 : period === 'week' ? 137 : 271;

  const timeSeries = generateTimeSeries(days, seed);
  const totals = timeSeries.reduce(
    (acc, d) => ({
      tokens: acc.tokens + d.tokens,
      cost: +(acc.cost + d.cost).toFixed(4),
      sessions: acc.sessions + d.sessions,
      errors: acc.errors + d.errors,
    }),
    { tokens: 0, cost: 0, sessions: 0, errors: 0 }
  );
  const avgTime = Math.floor(45 + (seed % 30));
  const errorRate = totals.sessions > 0 ? +((totals.errors / totals.sessions) * 100).toFixed(1) : 0;

  // Resources
  const rand = seededRandom(seed + 99);
  const timeLogged = Math.floor(rand() * 3 + 2);
  const timeAvailable = 5;
  const moneySpent = totals.cost;
  const moneyBudget = period === 'today' ? 5 : period === 'week' ? 35 : 150;

  const timeByProject = [
    { name: 'quick-money', hours: +(rand() * 2 + 0.5).toFixed(1), color: '#a6e3a1' },
    { name: 'research', hours: +(rand() * 1 + 0.2).toFixed(1), color: '#89b4fa' },
    { name: 'brand', hours: +(rand() * 0.5 + 0.1).toFixed(1), color: '#cba6f7' },
    { name: 'infra', hours: +(rand() * 0.3 + 0.1).toFixed(1), color: '#fab387' },
  ];

  const costByCategory = [
    { name: 'Opus', value: +(totals.cost * 0.35).toFixed(2), color: '#cba6f7' },
    { name: 'Sonnet', value: +(totals.cost * 0.45).toFixed(2), color: '#89b4fa' },
    { name: 'Haiku', value: +(totals.cost * 0.15).toFixed(2), color: '#a6e3a1' },
    { name: 'Tools', value: +(totals.cost * 0.05).toFixed(2), color: '#fab387' },
  ];

  const focusAreas = [
    { name: 'Sales', weight: 35, color: '#a6e3a1' },
    { name: 'Ops', weight: 25, color: '#89b4fa' },
    { name: 'Research', weight: 20, color: '#94e2d5' },
    { name: 'Strategy', weight: 12, color: '#cba6f7' },
    { name: 'Other', weight: 8, color: '#585b70' },
  ];

  const balance = 487.50;
  const burnRate = period === 'month' ? totals.cost : totals.cost * (30 / Math.max(days, 1));
  const runway = burnRate > 0 ? +(balance / burnRate).toFixed(1) : 99;
  const runwayProjection = Array.from({ length: 6 }, (_, i) => ({
    month: new Date(Date.now() + i * 30 * 86400000).toISOString().slice(0, 7),
    balance: +(balance - burnRate * i).toFixed(2),
  }));

  res.json({
    period,
    // KPIs
    kpi: {
      tokens: { value: totals.tokens, delta: period === 'today' ? 0 : Math.floor(totals.tokens * 0.12) },
      cost: { value: totals.cost, delta: period === 'today' ? 0 : +(totals.cost * 0.08).toFixed(2) },
      sessions: { value: totals.sessions, delta: period === 'today' ? 0 : Math.floor(totals.sessions * 0.15) },
      errorRate: { value: errorRate, delta: period === 'today' ? 0 : -1.2 },
      avgTime: { value: avgTime, delta: period === 'today' ? 0 : -3 },
    },
    // Observability
    costTrend: timeSeries,
    agentTokens: generateAgentTokens(seed + 50),
    activeSessions: generateSessions(seed + 77),
    errorLog: generateErrors(seed + 33),
    // Resources
    resources: {
      time: { logged: timeLogged, available: timeAvailable, byProject: timeByProject },
      money: { spent: moneySpent, budget: moneyBudget, byCategory: costByCategory },
      attention: { areas: focusAreas },
      runway: { balance, burnRate: +burnRate.toFixed(2), months: runway, projection: runwayProjection },
    },
  });
});

export default router;
