import { Bot } from 'lucide-react';

export default function Agents() {
  return (
    <div>
      <div className="flex items-center gap-3 mb-6">
        <Bot size={24} className="text-ctp-mauve" />
        <h2 className="text-xl font-bold text-ctp-text">Agents</h2>
      </div>
      <div className="bg-ctp-mantle border border-ctp-surface0 rounded-lg p-8 text-center">
        <p className="text-ctp-subtext0">
          Agent cards, levels, XP bars, and performance metrics will appear here.
        </p>
      </div>
    </div>
  );
}
