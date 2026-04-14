import { KanbanSquare } from 'lucide-react';

export default function Kanban() {
  return (
    <div>
      <div className="flex items-center gap-3 mb-6">
        <KanbanSquare size={24} className="text-ctp-peach" />
        <h2 className="text-xl font-bold text-ctp-text">Kanban</h2>
      </div>
      <div className="bg-ctp-mantle border border-ctp-surface0 rounded-lg p-8 text-center">
        <p className="text-ctp-subtext0">
          Task board with columns (Backlog, In Progress, Review, Done) will appear here.
        </p>
      </div>
    </div>
  );
}
