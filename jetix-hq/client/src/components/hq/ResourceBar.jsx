import { Clock, Coins, Target } from 'lucide-react';
import { ProgressBar } from '../ui';

export default function ResourceBar({ time, money, focus }) {
  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip px-4 py-2 flex items-center gap-6">
      {/* Time */}
      <div className="flex items-center gap-2 flex-1">
        <Clock size={12} className="text-ctp-blue shrink-0" />
        <span className="text-[9px] text-ctp-overlay0 w-8 shrink-0">Time</span>
        <ProgressBar value={time.used} max={time.total} color="blue" size="sm" className="flex-1" />
        <span className="text-[9px] font-mono text-ctp-overlay0 w-12 text-right">{time.used}h/{time.total}h</span>
      </div>

      {/* Money */}
      <div className="flex items-center gap-2 flex-1">
        <Coins size={12} className="text-ctp-green shrink-0" />
        <span className="text-[9px] text-ctp-overlay0 w-10 shrink-0">Budget</span>
        <ProgressBar
          value={money.spent}
          max={money.budget}
          color={money.spent / money.budget > 0.8 ? 'red' : 'green'}
          size="sm"
          className="flex-1"
        />
        <span className="text-[9px] font-mono text-ctp-overlay0 w-16 text-right">${money.spent}/{money.budget}</span>
      </div>

      {/* Focus */}
      <div className="flex items-center gap-2 flex-1">
        <Target size={12} className="text-ctp-mauve shrink-0" />
        <span className="text-[9px] text-ctp-overlay0 w-8 shrink-0">Focus</span>
        <div className="flex-1 flex gap-0.5 h-2">
          {focus.map((f) => (
            <div
              key={f.name}
              className="h-full"
              style={{ backgroundColor: f.color, flex: f.weight }}
              title={`${f.name}: ${f.weight}%`}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
