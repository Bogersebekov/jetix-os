import { Flame, Users, Coins } from 'lucide-react';
import { ProgressBar } from '../ui';
import { getCompanyLevel, getXpToNext } from '../../data/rooms';

export default function CompanyHeader({ companyXp, streak, budget, activeAgents, totalAgents }) {
  const level = getCompanyLevel(companyXp);
  const xpInfo = getXpToNext(companyXp);

  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip px-4 py-3">
      <div className="flex items-center gap-4">
        {/* Company name + level */}
        <div className="flex items-center gap-2">
          <span className="text-xl">{level.icon}</span>
          <div>
            <h1 className="font-pixel text-[12px] text-ctp-mauve leading-none">JETIX HQ</h1>
            <p className="font-pixel text-[8px] text-ctp-overlay1 mt-1">
              Lv.{level.level} {level.name}
            </p>
          </div>
        </div>

        {/* XP bar */}
        <div className="flex-1 max-w-xs">
          <ProgressBar
            value={xpInfo.current}
            max={xpInfo.target}
            color="mauve"
            showValue
            size="sm"
            label="XP"
          />
        </div>

        {/* Streak */}
        <div className="flex items-center gap-1.5 px-3 py-1 bg-ctp-surface0 border border-ctp-surface1">
          <Flame size={14} className="text-ctp-peach" />
          <span className="font-pixel text-[10px] text-ctp-peach">{streak}</span>
        </div>

        {/* Budget mini-bar */}
        <div className="flex items-center gap-2">
          <Coins size={14} className="text-ctp-green" />
          <ProgressBar
            value={budget.spent}
            max={budget.total}
            color={budget.spent / budget.total > 0.8 ? 'red' : 'green'}
            size="sm"
            className="w-20"
          />
          <span className="text-[10px] font-mono text-ctp-overlay0">
            ${budget.spent}/{budget.total}
          </span>
        </div>

        {/* Active agents */}
        <div className="flex items-center gap-1.5 px-3 py-1 bg-ctp-surface0 border border-ctp-surface1">
          <Users size={14} className="text-ctp-blue" />
          <span className="font-pixel text-[10px] text-ctp-text">
            {activeAgents}/{totalAgents}
          </span>
        </div>
      </div>
    </div>
  );
}
