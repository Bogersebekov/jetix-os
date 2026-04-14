import { Users } from 'lucide-react';
import { Card, Badge, ProgressBar, EmptyState } from '../components/ui';

const mockAgents = [
  { name: 'Manager', dept: 'MGMT', model: 'Sonnet 4.6', level: 1, xp: 0, status: 'offline' },
  { name: 'Personal Assistant', dept: 'OPS', model: 'Haiku 4.5', level: 1, xp: 0, status: 'offline' },
  { name: 'System Admin', dept: 'OPS', model: 'Haiku 4.5', level: 1, xp: 0, status: 'offline' },
  { name: 'Sales Lead', dept: 'SALES', model: 'Sonnet 4.6', level: 1, xp: 0, status: 'offline' },
  { name: 'Sales Researcher', dept: 'SALES', model: 'Haiku 4.5', level: 1, xp: 0, status: 'offline' },
  { name: 'Sales Outreach', dept: 'SALES', model: 'Haiku 4.5', level: 1, xp: 0, status: 'offline' },
  { name: 'Inbox Processor', dept: 'BRAIN', model: 'Haiku 4.5', level: 1, xp: 0, status: 'offline' },
  { name: 'Crazy Agent', dept: 'META', model: 'Sonnet 4.6', level: 1, xp: 0, status: 'offline' },
  { name: 'Knowledge Synth', dept: 'BRAIN', model: 'Sonnet 4.6', level: 1, xp: 0, status: 'offline' },
  { name: 'Strategist', dept: 'MGMT', model: 'Opus 4.6', level: 1, xp: 0, status: 'offline' },
  { name: 'Life Coach', dept: 'LIFE', model: 'Sonnet 4.6', level: 1, xp: 0, status: 'offline' },
  { name: 'Meta Agent', dept: 'META', model: 'Sonnet 4.6', level: 1, xp: 0, status: 'offline' },
];

export default function Agents() {
  return (
    <div className="space-y-6">
      <div className="flex items-center gap-3">
        <Users size={24} className="text-ctp-mauve" />
        <h2 className="font-pixel text-sm text-ctp-text">AGENT ROSTER</h2>
        <span className="text-xs text-ctp-overlay1 font-mono">12 agents</span>
      </div>

      <div className="grid grid-cols-3 gap-4">
        {mockAgents.map((agent) => (
          <Card key={agent.name} className="hover:border-ctp-surface2 transition-colors">
            <div className="flex items-start justify-between mb-3">
              <div>
                <p className="font-pixel text-[10px] text-ctp-text">{agent.name}</p>
                <p className="text-[10px] text-ctp-overlay1 font-mono mt-1">
                  {agent.dept} · {agent.model}
                </p>
              </div>
              <Badge status={agent.status} />
            </div>
            <ProgressBar
              value={agent.xp}
              max={100}
              color="mauve"
              label={`Lv.${agent.level}`}
              showValue
              size="sm"
            />
          </Card>
        ))}
      </div>
    </div>
  );
}
