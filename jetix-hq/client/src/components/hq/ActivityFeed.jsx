import { MessageSquare, CheckCircle, AlertTriangle, Zap, Send, Brain } from 'lucide-react';

const mockEvents = [
  { id: 1, icon: Zap, color: 'text-ctp-yellow', text: 'System initialized — 12 agents configured', time: '2m ago' },
  { id: 2, icon: Send, color: 'text-ctp-green', text: 'Message sent: human → manager (task)', time: '5m ago' },
  { id: 3, icon: CheckCircle, color: 'text-ctp-green', text: 'Morning pipeline completed', time: '12m ago' },
  { id: 4, icon: Brain, color: 'text-ctp-teal', text: 'Knowledge base indexed: 70 files', time: '15m ago' },
  { id: 5, icon: AlertTriangle, color: 'text-ctp-yellow', text: 'Crazy Agent ideas session pending', time: '1h ago' },
  { id: 6, icon: MessageSquare, color: 'text-ctp-blue', text: 'Strategist: awaiting briefing data', time: '2h ago' },
];

export default function ActivityFeed() {
  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip h-full flex flex-col">
      <div className="px-3 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30 shrink-0">
        <h3 className="font-pixel text-[9px] text-ctp-subtext1">ACTIVITY FEED</h3>
      </div>
      <div className="flex-1 overflow-y-auto">
        {mockEvents.map((evt) => (
          <div key={evt.id} className="flex items-start gap-2 px-3 py-2 border-b border-ctp-surface0/30">
            <evt.icon size={12} className={`${evt.color} shrink-0 mt-0.5`} />
            <div className="min-w-0">
              <p className="text-[10px] text-ctp-subtext0 leading-snug">{evt.text}</p>
              <p className="text-[9px] text-ctp-overlay0 font-mono mt-0.5">{evt.time}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
