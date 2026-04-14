export const rooms = [
  {
    id: 'director',
    emoji: '🌟',
    name: "Director's Office",
    accent: '#cba6f7',
    bg: 'bg-ctp-surface0',
    agents: ['strategist'],
  },
  {
    id: 'management',
    emoji: '📊',
    name: 'Management',
    accent: '#89b4fa',
    bg: 'bg-ctp-surface0',
    agents: ['manager'],
  },
  {
    id: 'sales',
    emoji: '💰',
    name: 'Sales Department',
    accent: '#a6e3a1',
    bg: 'bg-ctp-surface0',
    agents: ['sales-lead', 'sales-researcher', 'sales-outreach'],
  },
  {
    id: 'brain',
    emoji: '📝',
    name: 'Brain Center',
    accent: '#94e2d5',
    bg: 'bg-ctp-surface0',
    agents: ['inbox-processor', 'knowledge-synth'],
  },
  {
    id: 'server',
    emoji: '🤖',
    name: 'Server Room',
    accent: '#89b4fa',
    bg: 'bg-ctp-surface0',
    agents: ['personal-assistant', 'system-admin'],
  },
  {
    id: 'lounge',
    emoji: '🏋️',
    name: 'Lounge',
    accent: '#fab387',
    bg: 'bg-ctp-surface0',
    agents: ['life-coach'],
  },
  {
    id: 'lab',
    emoji: '🎓',
    name: 'Laboratory',
    accent: '#f5c2e7',
    bg: 'bg-ctp-surface0',
    agents: ['meta-agent'],
  },
  {
    id: 'attic',
    emoji: '🤪',
    name: 'The Attic',
    accent: '#eba0ac',
    bg: 'bg-ctp-surface0',
    agents: ['crazy-agent'],
  },
];

export const companyLevels = [
  { level: 1, name: 'Garage', minXp: 0, icon: '🏚️' },
  { level: 2, name: 'Small Office', minXp: 5000, icon: '🏢' },
  { level: 3, name: 'Growing Startup', minXp: 15000, icon: '🏗️' },
  { level: 4, name: 'AI Startup', minXp: 30000, icon: '🚀' },
  { level: 5, name: 'Scale-up', minXp: 50000, icon: '🏙️' },
  { level: 6, name: 'Corporation', minXp: 100000, icon: '🏰' },
  { level: 7, name: 'Empire', minXp: 200000, icon: '👑' },
];

export function getCompanyLevel(xp) {
  for (let i = companyLevels.length - 1; i >= 0; i--) {
    if (xp >= companyLevels[i].minXp) return companyLevels[i];
  }
  return companyLevels[0];
}

export function getXpToNext(xp) {
  const current = getCompanyLevel(xp);
  const idx = companyLevels.findIndex((l) => l.level === current.level);
  const next = companyLevels[idx + 1];
  if (!next) return { current: xp, target: xp, progress: 100 };
  return {
    current: xp - current.minXp,
    target: next.minXp - current.minXp,
    progress: ((xp - current.minXp) / (next.minXp - current.minXp)) * 100,
  };
}
