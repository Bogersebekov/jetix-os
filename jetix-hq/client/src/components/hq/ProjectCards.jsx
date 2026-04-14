import { ProgressBar, Badge } from '../ui';

const mockProjects = [
  {
    id: 'quick-money',
    emoji: '💰',
    title: 'Quick Money',
    progress: 12,
    health: 'on-track',
    agents: ['sales-lead', 'sales-researcher', 'sales-outreach'],
    target: '$50K by June 30',
  },
  {
    id: 'brand',
    emoji: '🎨',
    title: 'Jetix Brand',
    progress: 5,
    health: 'at-risk',
    agents: ['sales-outreach'],
    target: 'LinkedIn + content',
  },
  {
    id: 'research',
    emoji: '🔬',
    title: 'Research',
    progress: 20,
    health: 'on-track',
    agents: ['knowledge-synth'],
    target: 'Knowledge base',
  },
  {
    id: 'infra',
    emoji: '⚙️',
    title: 'Infrastructure',
    progress: 65,
    health: 'on-track',
    agents: ['system-admin'],
    target: 'Multi-agent system',
  },
];

const healthMap = {
  'on-track': 'active',
  'at-risk': 'idle',
  blocked: 'error',
};

export default function ProjectCards() {
  return (
    <div className="grid grid-cols-4 gap-3">
      {mockProjects.map((p) => (
        <div key={p.id} className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip p-3">
          <div className="flex items-center gap-2 mb-2">
            <span className="text-sm">{p.emoji}</span>
            <span className="font-pixel text-[9px] text-ctp-text truncate">{p.title}</span>
            <Badge status={healthMap[p.health]} label={p.health} className="ml-auto" />
          </div>
          <ProgressBar value={p.progress} max={100} color={p.health === 'at-risk' ? 'yellow' : 'green'} size="sm" />
          <p className="text-[9px] text-ctp-overlay0 mt-1.5">{p.target}</p>
          <div className="flex items-center gap-1 mt-1.5">
            <span className="text-[8px] text-ctp-overlay0">{p.agents.length} agents</span>
          </div>
        </div>
      ))}
    </div>
  );
}
