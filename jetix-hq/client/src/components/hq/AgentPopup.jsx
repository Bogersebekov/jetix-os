import { useNavigate } from 'react-router-dom';
import { X, ExternalLink } from 'lucide-react';
import { Badge, ProgressBar, Button } from '../ui';
import { deptColors, getInitials } from '../../data/agents';

export default function AgentPopup({ agent, onClose }) {
  const navigate = useNavigate();

  if (!agent) return null;

  const dept = deptColors[agent.dept] || deptColors.OPS;
  const initials = getInitials(agent.name);

  return (
    <div className="fixed inset-0 z-40 flex items-center justify-center bg-ctp-crust/50" onClick={onClose}>
      <div
        className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip w-72 shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between px-3 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
          <span className="font-pixel text-[10px] text-ctp-mauve">AGENT INFO</span>
          <button onClick={onClose} className="text-ctp-overlay1 hover:text-ctp-red">
            <X size={14} />
          </button>
        </div>

        <div className="p-3 space-y-3">
          {/* Avatar + name */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 flex items-center justify-center" style={{ backgroundColor: dept.hex }}>
              <span className="font-pixel text-xs text-ctp-crust">{initials}</span>
            </div>
            <div>
              <p className="font-pixel text-[10px] text-ctp-text">{agent.name}</p>
              <p className="text-[10px] text-ctp-overlay1 font-mono">{agent.dept} · {agent.model}</p>
            </div>
            <Badge status={agent.status} className="ml-auto" />
          </div>

          {/* XP */}
          <ProgressBar
            value={agent.xp || 0}
            max={agent.xpToNext || 100}
            color="mauve"
            label={`Lv.${agent.level || 1}`}
            showValue
            size="sm"
          />

          {/* Current task */}
          <div>
            <p className="text-[9px] text-ctp-overlay0 mb-0.5">Current Task</p>
            <p className="text-xs text-ctp-subtext0">
              {agent.currentTask || 'No active task'}
            </p>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-3 gap-2 text-center">
            <div className="bg-ctp-surface0 p-1.5">
              <p className="font-mono text-sm font-bold text-ctp-text">{agent.tasksToday || 0}</p>
              <p className="text-[8px] text-ctp-overlay0">Tasks</p>
            </div>
            <div className="bg-ctp-surface0 p-1.5">
              <p className="font-mono text-sm font-bold text-ctp-text">{agent.unreadMessages || 0}</p>
              <p className="text-[8px] text-ctp-overlay0">Msgs</p>
            </div>
            <div className="bg-ctp-surface0 p-1.5">
              <p className="font-mono text-sm font-bold text-ctp-text">{agent.errorRate || 0}%</p>
              <p className="text-[8px] text-ctp-overlay0">Errors</p>
            </div>
          </div>

          {/* View details link */}
          <Button
            variant="secondary"
            size="sm"
            className="w-full"
            onClick={() => { onClose(); navigate('/agents'); }}
          >
            <ExternalLink size={12} /> View Details
          </Button>
        </div>
      </div>
    </div>
  );
}
