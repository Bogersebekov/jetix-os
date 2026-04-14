import { Plus, GripVertical } from 'lucide-react';
import { Button, Badge, EmptyState } from '../ui';

export default function AgentQueue({ queue }) {
  return (
    <div className="p-4 space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="font-pixel text-[10px] text-ctp-subtext1">TASK QUEUE</h3>
        <Button variant="secondary" size="sm" disabled>
          <Plus size={12} /> Add Task
        </Button>
      </div>

      {queue && queue.length > 0 ? (
        <div className="space-y-2">
          {queue.map((task, i) => (
            <div
              key={task.id || i}
              className="flex items-center gap-3 bg-ctp-surface0/50 border border-ctp-surface1 p-3"
            >
              <GripVertical size={14} className="text-ctp-overlay0 cursor-grab" />
              <div className="flex-1 min-w-0">
                <p className="text-sm text-ctp-text truncate">{task.title}</p>
                <p className="text-[10px] text-ctp-overlay1 font-mono">
                  {task.priority} · {task.project || 'no project'}
                </p>
              </div>
              <Badge status={task.status === 'pending' ? 'idle' : 'active'} label={task.status} />
            </div>
          ))}
        </div>
      ) : (
        <EmptyState
          title="Queue empty"
          description="Tasks will appear here when assigned to this agent"
        />
      )}
    </div>
  );
}
