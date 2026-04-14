import { StatusDot } from '../ui';
import { deptColors, getInitials } from '../../data/agents';

export default function OfficeRoom({ room, agents, onAgentClick, onAgentHover }) {
  const hasActive = agents.some((a) => a.status === 'active');

  return (
    <div
      className={`
        ${room.bg} border-2 p-3 flex flex-col min-h-[120px]
        transition-all duration-300
        ${hasActive ? 'border-opacity-100 shadow-md' : 'border-opacity-40'}
      `}
      style={{
        borderColor: hasActive ? room.accent : '#45475a',
        boxShadow: hasActive ? `0 0 12px ${room.accent}20` : 'none',
      }}
    >
      {/* Room header */}
      <div className="flex items-center gap-1.5 mb-2">
        <span className="text-sm">{room.emoji}</span>
        <span className="font-pixel text-[8px] text-ctp-subtext0 truncate">{room.name}</span>
      </div>

      {/* Agents */}
      <div className="flex-1 flex flex-wrap gap-2 items-start content-start">
        {agents.map((agent) => (
          <AgentAvatar
            key={agent.id}
            agent={agent}
            onClick={() => onAgentClick?.(agent)}
            onHover={onAgentHover}
          />
        ))}
        {agents.length === 0 && (
          <p className="text-[9px] text-ctp-overlay0 italic">empty</p>
        )}
      </div>
    </div>
  );
}

function AgentAvatar({ agent, onClick, onHover }) {
  const dept = deptColors[agent.dept] || deptColors.OPS;
  const initials = getInitials(agent.name);
  const isActive = agent.status === 'active';

  return (
    <div
      className="relative group cursor-pointer"
      onClick={onClick}
      onMouseEnter={() => onHover?.(agent)}
      onMouseLeave={() => onHover?.(null)}
    >
      {/* Avatar square */}
      <div
        className={`
          w-8 h-8 flex items-center justify-center relative
          ${isActive ? 'animate-pulse' : ''}
        `}
        style={{ backgroundColor: dept.hex + (agent.status === 'offline' ? '40' : 'ff') }}
      >
        <span className="font-pixel text-[7px] text-ctp-crust leading-none">{initials}</span>
        <StatusDot
          status={agent.status}
          size={6}
          className="absolute -bottom-0.5 -right-0.5"
        />
      </div>

      {/* Mini task label */}
      {agent.currentTask && (
        <div className="absolute top-full left-0 mt-0.5 w-16">
          <p className="text-[7px] text-ctp-overlay0 truncate leading-tight">{agent.currentTask}</p>
        </div>
      )}

      {/* Tooltip */}
      <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-44 bg-ctp-crust border-2 border-ctp-surface1 p-2 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-30">
        <p className="font-pixel text-[8px] text-ctp-text mb-1">{agent.name}</p>
        <p className="text-[9px] text-ctp-overlay1">{agent.dept} · {agent.model}</p>
        {agent.currentTask && (
          <p className="text-[9px] text-ctp-subtext0 mt-1 truncate">📋 {agent.currentTask}</p>
        )}
        <div className="flex items-center gap-1 mt-1">
          <StatusDot status={agent.status} size={5} />
          <span className="text-[8px] text-ctp-overlay0">{agent.status}</span>
        </div>
      </div>
    </div>
  );
}
