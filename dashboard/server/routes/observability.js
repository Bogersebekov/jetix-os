import { Router } from 'express';

const MOCK_DATA = {
  summary: {
    total_tokens: 2450000,
    total_cost: 42.5,
    total_sessions: 28,
    avg_tokens_per_session: 87500,
  },
  daily: [
    { date: '2026-04-10', tokens: 320000, cost: 5.6, sessions: 4 },
    { date: '2026-04-11', tokens: 280000, cost: 4.9, sessions: 3 },
    { date: '2026-04-12', tokens: 410000, cost: 7.2, sessions: 5 },
    { date: '2026-04-13', tokens: 350000, cost: 6.1, sessions: 4 },
    { date: '2026-04-14', tokens: 520000, cost: 9.1, sessions: 6 },
    { date: '2026-04-15', tokens: 380000, cost: 6.6, sessions: 4 },
    { date: '2026-04-16', tokens: 190000, cost: 3.0, sessions: 2 },
  ],
  by_agent: [
    { agent: 'manager', tokens: 450000, cost: 7.8 },
    { agent: 'system-admin', tokens: 680000, cost: 5.4 },
    { agent: 'personal-assistant', tokens: 320000, cost: 2.5 },
    { agent: 'sales-lead', tokens: 280000, cost: 4.9 },
    { agent: 'strategist', tokens: 520000, cost: 12.5 },
    { agent: 'other', tokens: 200000, cost: 9.4 },
  ],
};

export default function observabilityRoute() {
  const router = Router();
  router.get('/', (_req, res) => res.json(MOCK_DATA));
  return router;
}
