import { useState } from 'react';
import { Pause, Play, RotateCcw, Mail, BarChart3, ListTodo, FileCode } from 'lucide-react';
import { Badge, Button, ProgressBar } from '../ui';
import { deptColors, getInitials } from '../../data/agents';
import useFetch from '../../hooks/useFetch';
import { useWs } from '../../hooks/useWebSocket';
import AgentMailbox from './AgentMailbox';
import AgentMetrics from './AgentMetrics';
import AgentQueue from './AgentQueue';
import AgentConfig from './AgentConfig';

const tabs = [
  { id: 'mailbox', label: 'Mailbox', icon: Mail },
  { id: 'metrics', label: 'Metrics', icon: BarChart3 },
  { id: 'queue', label: 'Queue', icon: ListTodo },
  { id: 'config', label: 'Config', icon: FileCode },
];

export default function AgentDetail({ agentId }) {
  const [activeTab, setActiveTab] = useState('mailbox');
  const { on } = useWs();
  const { data, loading } = useFetch(`/api/v1/agents/${agentId}`, {
    interval: 30000,
    wsEvents: ['agent:status', 'comms:message'],
    onWs: on,
  });

  if (loading && !data) {
    return (
      <div className="flex items-center justify-center h-full">
        <p className="text-sm text-ctp-overlay0">Loading agent...</p>
      </div>
    );
  }

  if (!data) {
    return (
      <div className="flex items-center justify-center h-full">
        <p className="text-sm text-ctp-red">Agent not found</p>
      </div>
    );
  }

  const dept = deptColors[data.dept] || deptColors.OPS;
  const initials = getInitials(data.name);

  return (
    <div className="flex flex-col h-full">
      {/* Header */}
      <div className="p-4 border-b-2 border-ctp-surface0 bg-ctp-mantle/50">
        <div className="flex items-start gap-4">
          {/* Large avatar */}
          <div className={`w-14 h-14 ${dept.bg} flex items-center justify-center shrink-0`}>
            <span className="font-pixel text-sm text-ctp-crust">{initials}</span>
          </div>

          <div className="flex-1 min-w-0">
            <div className="flex items-center gap-3 mb-1">
              <h2 className="font-pixel text-[12px] text-ctp-text">{data.name}</h2>
              <Badge status={data.status} />
            </div>
            <p className="text-xs text-ctp-overlay1 font-mono">
              {data.dept} · {data.model} · Phase {data.phase}
            </p>

            {/* Current task */}
            {data.currentTask ? (
              <div className="mt-2">
                <p className="text-xs text-ctp-subtext0 mb-1">{data.currentTask}</p>
                <ProgressBar value={0} max={100} color="blue" size="sm" />
              </div>
            ) : (
              <p className="text-xs text-ctp-overlay0 mt-2">No active task</p>
            )}
          </div>

          {/* XP */}
          <div className="text-right shrink-0">
            <p className="font-pixel text-[10px] text-ctp-mauve">Lv.{data.level}</p>
            <ProgressBar
              value={data.xp}
              max={data.xpToNext}
              color="mauve"
              showValue
              size="sm"
              className="w-24 mt-1"
            />
          </div>
        </div>

        {/* Quick actions */}
        <div className="flex gap-2 mt-3">
          <Button variant="secondary" size="sm" disabled>
            <Pause size={12} /> Pause
          </Button>
          <Button variant="secondary" size="sm" disabled>
            <Play size={12} /> Resume
          </Button>
          <Button variant="secondary" size="sm" disabled>
            <RotateCcw size={12} /> Restart
          </Button>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex border-b-2 border-ctp-surface0 bg-ctp-mantle/30">
        {tabs.map(({ id, label, icon: Icon }) => (
          <button
            key={id}
            onClick={() => setActiveTab(id)}
            className={`flex items-center gap-2 px-4 py-2.5 text-xs font-mono transition-colors border-b-2 ${
              activeTab === id
                ? 'border-ctp-mauve text-ctp-mauve'
                : 'border-transparent text-ctp-overlay1 hover:text-ctp-text'
            }`}
          >
            <Icon size={14} />
            {label}
            {id === 'mailbox' && data.unreadMessages > 0 && (
              <span className="bg-ctp-mauve text-ctp-crust text-[9px] font-bold px-1.5 rounded-full">
                {data.unreadMessages}
              </span>
            )}
          </button>
        ))}
      </div>

      {/* Tab content */}
      <div className="flex-1 overflow-auto">
        {activeTab === 'mailbox' && <AgentMailbox agentId={agentId} messages={data.messages} />}
        {activeTab === 'metrics' && <AgentMetrics metrics={data.metrics} />}
        {activeTab === 'queue' && <AgentQueue queue={data.queue} />}
        {activeTab === 'config' && <AgentConfig agent={data} />}
      </div>
    </div>
  );
}
