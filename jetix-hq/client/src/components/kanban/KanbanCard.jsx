import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import { Calendar, MessageSquare, CheckSquare } from 'lucide-react';
import { StatusDot } from '../ui';
import { deptColors, getInitials } from '../../data/agents';

const priorityBadge = {
  high: { dot: 'bg-ctp-red', label: '🔴' },
  medium: { dot: 'bg-ctp-yellow', label: '🟡' },
  low: { dot: 'bg-ctp-overlay1', label: '⚪' },
};

export default function KanbanCard({ card, onClick }) {
  const {
    attributes, listeners, setNodeRef, transform, transition, isDragging,
  } = useSortable({ id: card.id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    opacity: isDragging ? 0.5 : 1,
  };

  const pri = priorityBadge[card.priority] || priorityBadge.medium;
  const isOverdue = card.due_date && new Date(card.due_date) < new Date();
  const doneSubtasks = (card.subtasks || []).filter((s) => s.done).length;
  const totalSubtasks = (card.subtasks || []).length;
  const commentCount = (card.comments || []).length;

  return (
    <div
      ref={setNodeRef}
      style={style}
      {...attributes}
      {...listeners}
      onClick={() => onClick?.(card)}
      className={`
        bg-ctp-base border-2 border-ctp-surface1 p-2.5 cursor-grab active:cursor-grabbing
        hover:border-ctp-surface2 transition-colors
        ${isDragging ? 'shadow-lg shadow-ctp-crust/50' : ''}
      `}
    >
      {/* Title */}
      <p className="text-xs text-ctp-text leading-snug line-clamp-2 mb-2">{card.title}</p>

      {/* Tags */}
      {card.tags?.length > 0 && (
        <div className="flex flex-wrap gap-1 mb-2">
          {card.tags.slice(0, 3).map((tag) => (
            <span key={tag} className="px-1.5 py-0 text-[9px] font-mono bg-ctp-surface0 text-ctp-overlay1 border border-ctp-surface1">
              {tag}
            </span>
          ))}
        </div>
      )}

      {/* Subtask progress */}
      {totalSubtasks > 0 && (
        <div className="mb-2">
          <div className="w-full h-1 bg-ctp-surface0 overflow-hidden">
            <div
              className="h-full bg-ctp-green transition-all"
              style={{ width: `${(doneSubtasks / totalSubtasks) * 100}%` }}
            />
          </div>
        </div>
      )}

      {/* Footer */}
      <div className="flex items-center gap-2 mt-1">
        {/* Priority */}
        <span className="text-[10px]">{pri.label}</span>

        {/* Assignee */}
        {card.assignee && (
          <div className={`w-5 h-5 ${deptColors[card.assignee]?.bg || 'bg-ctp-surface1'} flex items-center justify-center`}
               title={card.assignee}>
            <span className="font-pixel text-[6px] text-ctp-crust">
              {getInitials(card.assignee)}
            </span>
          </div>
        )}

        {/* Project badge */}
        {card.project && (
          <span className="text-[9px] font-mono text-ctp-overlay0 truncate max-w-[60px]">
            {card.project}
          </span>
        )}

        <div className="flex-1" />

        {/* Subtasks count */}
        {totalSubtasks > 0 && (
          <span className="flex items-center gap-0.5 text-[9px] text-ctp-overlay0">
            <CheckSquare size={9} /> {doneSubtasks}/{totalSubtasks}
          </span>
        )}

        {/* Comments */}
        {commentCount > 0 && (
          <span className="flex items-center gap-0.5 text-[9px] text-ctp-overlay0">
            <MessageSquare size={9} /> {commentCount}
          </span>
        )}

        {/* Due date */}
        {card.due_date && (
          <span className={`flex items-center gap-0.5 text-[9px] font-mono ${isOverdue ? 'text-ctp-red' : 'text-ctp-overlay0'}`}>
            <Calendar size={9} />
            {card.due_date.slice(5)}
          </span>
        )}
      </div>
    </div>
  );
}
