import { Inbox } from 'lucide-react';
import Button from './Button';

export default function EmptyState({
  icon: Icon = Inbox,
  title = 'No data yet',
  description,
  actionLabel,
  onAction,
  className = '',
}) {
  return (
    <div className={`flex flex-col items-center justify-center py-12 ${className}`}>
      <div className="p-4 bg-ctp-surface0 rpg-clip mb-4">
        <Icon size={32} className="text-ctp-overlay1" />
      </div>
      <h3 className="font-pixel text-[10px] text-ctp-subtext1 mb-2">{title}</h3>
      {description && (
        <p className="text-sm text-ctp-overlay1 text-center max-w-xs mb-4">{description}</p>
      )}
      {actionLabel && onAction && (
        <Button variant="secondary" size="sm" onClick={onAction}>
          {actionLabel}
        </Button>
      )}
    </div>
  );
}
