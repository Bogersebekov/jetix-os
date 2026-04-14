import { TrendingUp, TrendingDown, Minus } from 'lucide-react';

const trendIcons = {
  up: { icon: TrendingUp, color: 'text-ctp-green', label: '↑' },
  down: { icon: TrendingDown, color: 'text-ctp-red', label: '↓' },
  flat: { icon: Minus, color: 'text-ctp-overlay1', label: '—' },
};

export default function StatCard({ label, value, trend, trendLabel, icon: Icon, className = '' }) {
  const t = trendIcons[trend] || trendIcons.flat;

  return (
    <div
      className={`
        bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip p-4
        ${className}
      `}
    >
      <div className="flex items-start justify-between">
        <div>
          <p className="text-xs text-ctp-subtext0 mb-1">{label}</p>
          <p className="text-2xl font-bold font-mono text-ctp-text">{value}</p>
        </div>
        {Icon && (
          <div className="p-2 bg-ctp-surface0 rpg-clip">
            <Icon size={18} className="text-ctp-overlay2" />
          </div>
        )}
      </div>
      {trend && (
        <div className={`flex items-center gap-1 mt-2 text-xs ${t.color}`}>
          <t.icon size={14} />
          <span>{trendLabel || trend}</span>
        </div>
      )}
    </div>
  );
}
