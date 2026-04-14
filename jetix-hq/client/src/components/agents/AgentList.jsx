import { useState, useMemo } from 'react';
import { Search, ChevronDown, ChevronRight } from 'lucide-react';
import { StatusDot } from '../ui';
import { deptColors, departments, getInitials } from '../../data/agents';

export default function AgentList({ agents, selectedId, onSelect }) {
  const [search, setSearch] = useState('');
  const [statusFilter, setStatusFilter] = useState('all');
  const [deptFilter, setDeptFilter] = useState('ALL');
  const [collapsedDepts, setCollapsedDepts] = useState({});
  const [sortBy, setSortBy] = useState('name');

  const filtered = useMemo(() => {
    let list = agents;

    if (search) {
      const q = search.toLowerCase();
      list = list.filter((a) => a.name.toLowerCase().includes(q) || a.id.toLowerCase().includes(q));
    }

    if (statusFilter !== 'all') {
      list = list.filter((a) => a.status === statusFilter);
    }

    if (deptFilter !== 'ALL') {
      list = list.filter((a) => a.dept === deptFilter);
    }

    list = [...list].sort((a, b) => {
      if (sortBy === 'name') return a.name.localeCompare(b.name);
      if (sortBy === 'status') {
        const order = { active: 0, idle: 1, error: 2, offline: 3 };
        return (order[a.status] ?? 4) - (order[b.status] ?? 4);
      }
      return (b.tasksToday || 0) - (a.tasksToday || 0);
    });

    return list;
  }, [agents, search, statusFilter, deptFilter, sortBy]);

  const grouped = useMemo(() => {
    const groups = {};
    for (const agent of filtered) {
      (groups[agent.dept] ||= []).push(agent);
    }
    return groups;
  }, [filtered]);

  const toggleDept = (dept) =>
    setCollapsedDepts((p) => ({ ...p, [dept]: !p[dept] }));

  const statusFilters = ['all', 'active', 'idle', 'error', 'offline'];

  return (
    <div className="flex flex-col h-full">
      {/* Search */}
      <div className="p-3 border-b-2 border-ctp-surface0">
        <div className="relative">
          <Search size={14} className="absolute left-2.5 top-1/2 -translate-y-1/2 text-ctp-overlay0" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search agents..."
            className="w-full bg-ctp-surface0 text-ctp-text text-sm pl-8 pr-3 py-2 border border-ctp-surface1 focus:border-ctp-mauve focus:outline-none placeholder:text-ctp-overlay0"
          />
        </div>
      </div>

      {/* Status filters */}
      <div className="px-3 py-2 border-b-2 border-ctp-surface0 flex flex-wrap gap-1.5">
        {statusFilters.map((s) => (
          <button
            key={s}
            onClick={() => setStatusFilter(s)}
            className={`px-2 py-0.5 text-[10px] font-mono border transition-colors ${
              statusFilter === s
                ? 'bg-ctp-surface1 border-ctp-mauve text-ctp-text'
                : 'bg-transparent border-ctp-surface1 text-ctp-overlay1 hover:text-ctp-text'
            }`}
          >
            {s}
          </button>
        ))}
      </div>

      {/* Dept filters */}
      <div className="px-3 py-2 border-b-2 border-ctp-surface0 flex flex-wrap gap-1.5">
        {departments.map((d) => (
          <button
            key={d}
            onClick={() => setDeptFilter(d)}
            className={`px-2 py-0.5 text-[10px] font-mono border transition-colors ${
              deptFilter === d
                ? 'bg-ctp-surface1 border-ctp-mauve text-ctp-text'
                : 'bg-transparent border-ctp-surface1 text-ctp-overlay1 hover:text-ctp-text'
            }`}
          >
            {d}
          </button>
        ))}
      </div>

      {/* Sort */}
      <div className="px-3 py-1.5 border-b border-ctp-surface0/50 flex items-center gap-2">
        <span className="text-[10px] text-ctp-overlay0">Sort:</span>
        {['name', 'status', 'activity'].map((s) => (
          <button
            key={s}
            onClick={() => setSortBy(s)}
            className={`text-[10px] font-mono ${
              sortBy === s ? 'text-ctp-mauve' : 'text-ctp-overlay0 hover:text-ctp-text'
            }`}
          >
            {s}
          </button>
        ))}
      </div>

      {/* Agent list grouped by dept */}
      <div className="flex-1 overflow-y-auto">
        {Object.entries(grouped).map(([dept, deptAgents]) => (
          <div key={dept}>
            {/* Department header */}
            <button
              onClick={() => toggleDept(dept)}
              className="w-full flex items-center gap-2 px-3 py-2 bg-ctp-surface0/30 hover:bg-ctp-surface0/50 transition-colors"
            >
              {collapsedDepts[dept] ? (
                <ChevronRight size={12} className="text-ctp-overlay0" />
              ) : (
                <ChevronDown size={12} className="text-ctp-overlay0" />
              )}
              <span
                className={`font-pixel text-[8px] ${deptColors[dept]?.text || 'text-ctp-overlay1'}`}
              >
                {dept}
              </span>
              <span className="text-[10px] text-ctp-overlay0 font-mono ml-auto">
                {deptAgents.length}
              </span>
            </button>

            {/* Agent items */}
            {!collapsedDepts[dept] &&
              deptAgents.map((agent) => (
                <AgentListItem
                  key={agent.id}
                  agent={agent}
                  selected={selectedId === agent.id}
                  onSelect={() => onSelect(agent.id)}
                />
              ))}
          </div>
        ))}

        {filtered.length === 0 && (
          <div className="p-6 text-center text-xs text-ctp-overlay0">No agents match filters</div>
        )}
      </div>
    </div>
  );
}

function AgentListItem({ agent, selected, onSelect }) {
  const dept = deptColors[agent.dept] || deptColors.OPS;
  const initials = getInitials(agent.name);

  return (
    <button
      onClick={onSelect}
      className={`w-full flex items-center gap-3 px-3 py-2.5 text-left transition-colors ${
        selected
          ? 'bg-ctp-surface0 border-l-[3px] border-ctp-blue pl-[9px]'
          : 'border-l-[3px] border-transparent pl-[9px] hover:bg-ctp-surface0/30'
      }`}
    >
      {/* Avatar */}
      <div
        className={`w-8 h-8 ${dept.bg} flex items-center justify-center shrink-0`}
      >
        <span className="font-pixel text-[8px] text-ctp-crust">{initials}</span>
      </div>

      {/* Info */}
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-1.5">
          <span className="text-sm text-ctp-text truncate">{agent.name}</span>
          <StatusDot status={agent.status} size={6} />
        </div>
        {agent.currentTask ? (
          <p className="text-[10px] text-ctp-overlay1 truncate mt-0.5">
            {agent.currentTask.length > 40
              ? agent.currentTask.slice(0, 40) + '...'
              : agent.currentTask}
          </p>
        ) : (
          <p className="text-[10px] text-ctp-overlay0 mt-0.5">idle</p>
        )}
      </div>

      {/* Unread badge */}
      {agent.unreadMessages > 0 && (
        <span className="bg-ctp-mauve text-ctp-crust text-[9px] font-bold px-1.5 py-0.5 rounded-full min-w-[20px] text-center">
          {agent.unreadMessages}
        </span>
      )}
    </button>
  );
}
