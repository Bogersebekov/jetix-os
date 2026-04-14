import { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import {
  Building2,
  Users,
  BarChart3,
  Columns3,
  BookOpen,
  Settings,
  ChevronLeft,
  ChevronRight,
  Activity,
  CheckCircle2,
  AlertCircle,
} from 'lucide-react';
import Badge from './ui/Badge';

const navItems = [
  { to: '/hq', label: 'HQ', icon: Building2 },
  { to: '/agents', label: 'Agents', icon: Users },
  { to: '/dashboard', label: 'Dashboard', icon: BarChart3 },
  { to: '/kanban', label: 'Kanban', icon: Columns3 },
  { to: '/knowledge', label: 'Knowledge', icon: BookOpen },
  { to: '/settings', label: 'Settings', icon: Settings },
];

const breadcrumbMap = {
  '/hq': 'Headquarters',
  '/agents': 'Agent Roster',
  '/dashboard': 'Analytics Dashboard',
  '/kanban': 'Task Board',
  '/knowledge': 'Knowledge Base',
  '/settings': 'Settings',
};

// Mock team status
const teamStatus = { active: 0, errors: 0, tasks: 0 };

export default function Layout({ children }) {
  const [collapsed, setCollapsed] = useState(false);
  const location = useLocation();
  const currentPage = breadcrumbMap[location.pathname] || 'Jetix HQ';

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Sidebar */}
      <aside
        className={`
          ${collapsed ? 'w-16' : 'w-60'}
          bg-ctp-mantle border-r-2 border-ctp-surface0
          flex flex-col shrink-0
          transition-[width] duration-200
        `}
      >
        {/* Logo */}
        <div className="p-3 border-b-2 border-ctp-surface0 flex items-center gap-2 min-h-[56px]">
          <span className="text-lg leading-none">🏰</span>
          {!collapsed && (
            <div>
              <h1 className="font-pixel text-[12px] text-ctp-mauve tracking-wider leading-none">
                JETIX HQ
              </h1>
              <p className="text-[10px] text-ctp-overlay0 font-mono mt-1">v0.1 · Garage</p>
            </div>
          )}
        </div>

        {/* Navigation */}
        <nav className="flex-1 py-2 overflow-y-auto">
          {navItems.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              title={collapsed ? label : undefined}
              className={({ isActive }) =>
                `flex items-center gap-3 mx-2 my-0.5 px-3 py-2.5 rounded-sm text-sm transition-colors ${
                  isActive
                    ? 'bg-ctp-surface0 text-ctp-mauve border-l-[3px] border-ctp-mauve pl-[9px]'
                    : 'text-ctp-subtext0 hover:bg-ctp-surface0/40 hover:text-ctp-text border-l-[3px] border-transparent pl-[9px]'
                }`
              }
            >
              <Icon size={18} className="shrink-0" />
              {!collapsed && <span>{label}</span>}
            </NavLink>
          ))}
        </nav>

        {/* Team Status */}
        <div className="border-t-2 border-ctp-surface0 p-3">
          {!collapsed ? (
            <div className="space-y-1.5">
              <p className="font-pixel text-[8px] text-ctp-overlay0 mb-2">TEAM STATUS</p>
              <div className="flex items-center gap-2 text-xs text-ctp-subtext0">
                <Activity size={12} className="text-ctp-green" />
                <span>{teamStatus.active} active</span>
              </div>
              <div className="flex items-center gap-2 text-xs text-ctp-subtext0">
                <AlertCircle size={12} className="text-ctp-red" />
                <span>{teamStatus.errors} errors</span>
              </div>
              <div className="flex items-center gap-2 text-xs text-ctp-subtext0">
                <CheckCircle2 size={12} className="text-ctp-blue" />
                <span>{teamStatus.tasks} tasks</span>
              </div>
            </div>
          ) : (
            <div className="flex flex-col items-center gap-1">
              <Activity size={14} className="text-ctp-overlay0" />
            </div>
          )}
        </div>

        {/* Collapse toggle */}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className="border-t-2 border-ctp-surface0 p-3 flex items-center justify-center text-ctp-overlay1 hover:text-ctp-text hover:bg-ctp-surface0/40 transition-colors"
        >
          {collapsed ? <ChevronRight size={16} /> : <ChevronLeft size={16} />}
        </button>
      </aside>

      {/* Main area */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Header bar */}
        <header className="h-14 bg-ctp-mantle border-b-2 border-ctp-surface0 flex items-center justify-between px-6 shrink-0">
          <div className="flex items-center gap-2">
            <span className="font-mono text-xs text-ctp-overlay1">jetix</span>
            <span className="text-ctp-surface2">/</span>
            <span className="font-mono text-sm text-ctp-text">{currentPage}</span>
          </div>
          <div className="flex items-center gap-3">
            <Badge status="active" label="running" />
            <Badge status="offline" label="0 done" />
            <Badge status="offline" label="0 errors" />
          </div>
        </header>

        {/* Content */}
        <main className="flex-1 overflow-auto p-6">{children}</main>
      </div>
    </div>
  );
}
