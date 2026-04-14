import { Columns3 } from 'lucide-react';
import { Card, EmptyState } from '../components/ui';

const columns = [
  { id: 'backlog', label: 'BACKLOG', color: 'ctp-overlay1' },
  { id: 'in_progress', label: 'IN PROGRESS', color: 'ctp-blue' },
  { id: 'review', label: 'REVIEW', color: 'ctp-yellow' },
  { id: 'done', label: 'DONE', color: 'ctp-green' },
];

export default function Kanban() {
  return (
    <div className="space-y-6">
      <div className="flex items-center gap-3">
        <Columns3 size={24} className="text-ctp-peach" />
        <h2 className="font-pixel text-sm text-ctp-text">TASK BOARD</h2>
      </div>

      <div className="grid grid-cols-4 gap-4 h-[calc(100vh-12rem)]">
        {columns.map((col) => (
          <div key={col.id} className="flex flex-col">
            <div className="flex items-center gap-2 mb-3 px-1">
              <div className={`w-2 h-2 bg-${col.color}`} />
              <span className="font-pixel text-[9px] text-ctp-subtext0">{col.label}</span>
              <span className="text-[10px] text-ctp-overlay0 font-mono ml-auto">0</span>
            </div>
            <div className="flex-1 bg-ctp-mantle/50 border-2 border-dashed border-ctp-surface0 rounded-sm p-2">
              <EmptyState title="Empty" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
