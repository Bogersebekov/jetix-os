import { NavLink } from 'react-router-dom';
import {
  Building2,
  Bot,
  BarChart3,
  KanbanSquare,
  BookOpen,
  Settings,
} from 'lucide-react';

const navItems = [
  { to: '/hq', label: 'HQ', icon: Building2 },
  { to: '/agents', label: 'Agents', icon: Bot },
  { to: '/dashboard', label: 'Dashboard', icon: BarChart3 },
  { to: '/kanban', label: 'Kanban', icon: KanbanSquare },
  { to: '/knowledge', label: 'Knowledge', icon: BookOpen },
  { to: '/settings', label: 'Settings', icon: Settings },
];

export default function Layout({ children }) {
  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <aside className="w-56 bg-ctp-mantle border-r border-ctp-surface0 flex flex-col">
        {/* Logo */}
        <div className="p-4 border-b border-ctp-surface0">
          <h1 className="font-pixel text-sm text-ctp-blue tracking-wider">
            JETIX HQ
          </h1>
          <p className="text-[10px] text-ctp-subtext0 mt-1 font-mono">
            v0.1.0 — Level 1
          </p>
        </div>

        {/* Navigation */}
        <nav className="flex-1 py-2">
          {navItems.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              className={({ isActive }) =>
                `flex items-center gap-3 px-4 py-3 text-sm transition-colors ${
                  isActive
                    ? 'bg-ctp-surface0 text-ctp-blue border-r-2 border-ctp-blue'
                    : 'text-ctp-subtext0 hover:bg-ctp-surface0/50 hover:text-ctp-text'
                }`
              }
            >
              <Icon size={18} />
              <span>{label}</span>
            </NavLink>
          ))}
        </nav>

        {/* Footer */}
        <div className="p-4 border-t border-ctp-surface0">
          <div className="text-[10px] text-ctp-overlay0 font-mono">
            <div>Agents: 0/12 online</div>
            <div className="mt-1">API: --</div>
          </div>
        </div>
      </aside>

      {/* Main content */}
      <main className="flex-1 overflow-auto bg-ctp-base">
        <div className="p-6">{children}</div>
      </main>
    </div>
  );
}
