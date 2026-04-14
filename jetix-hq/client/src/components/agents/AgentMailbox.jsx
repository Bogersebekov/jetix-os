import { useState } from 'react';
import { Send } from 'lucide-react';
import { EmptyState } from '../ui';
import { deptColors } from '../../data/agents';

// Agent → dept mapping for bubble colors
const agentDeptMap = {
  manager: 'MGMT', strategist: 'MGMT',
  'sales-lead': 'SALES', 'sales-researcher': 'SALES', 'sales-outreach': 'SALES',
  'inbox-processor': 'BRAIN', 'knowledge-synth': 'BRAIN',
  'personal-assistant': 'OPS', 'system-admin': 'OPS',
  'life-coach': 'LIFE',
  'meta-agent': 'META', 'crazy-agent': 'META',
  human: 'OPS',
};

function getBubbleColor(agentId) {
  const dept = agentDeptMap[agentId] || 'OPS';
  return deptColors[dept]?.hex || '#89b4fa';
}

export default function AgentMailbox({ agentId, messages }) {
  const [draft, setDraft] = useState('');

  if (!messages || messages.length === 0) {
    return (
      <div className="h-full flex flex-col">
        <div className="flex-1 flex items-center justify-center">
          <EmptyState
            title="No messages"
            description="This agent's mailbox is empty"
          />
        </div>
        <MessageInput draft={draft} setDraft={setDraft} />
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        {messages.map((msg, i) => {
          const isOutgoing = msg.from === agentId;
          const bubbleColor = getBubbleColor(msg.from);
          return (
            <div key={msg.id || i} className={`flex ${isOutgoing ? 'justify-end' : 'justify-start'}`}>
              <div
                className={`max-w-[80%] p-3 ${
                  isOutgoing
                    ? 'bg-ctp-surface1 border-ctp-surface2'
                    : 'bg-ctp-surface0 border-ctp-surface1'
                } border-2`}
                style={!isOutgoing ? { borderLeftColor: bubbleColor, borderLeftWidth: 3 } : undefined}
              >
                {/* Header */}
                <div className="flex items-center gap-2 mb-1">
                  <span className="font-pixel text-[8px] text-ctp-subtext0">{msg.from}</span>
                  <span className="text-[10px] text-ctp-overlay0 font-mono">
                    {msg.type}/{msg.priority}
                  </span>
                </div>
                {/* Subject */}
                {msg.subject && (
                  <p className="text-xs font-semibold text-ctp-text mb-1">{msg.subject}</p>
                )}
                {/* Body */}
                <p className="text-xs text-ctp-subtext1 whitespace-pre-wrap">{msg.body}</p>
                {/* Timestamp */}
                <p className="text-[9px] text-ctp-overlay0 font-mono mt-1.5 text-right">
                  {msg.timestamp ? new Date(msg.timestamp).toLocaleTimeString() : '--'}
                </p>
              </div>
            </div>
          );
        })}
      </div>

      <MessageInput draft={draft} setDraft={setDraft} />
    </div>
  );
}

function MessageInput({ draft, setDraft }) {
  return (
    <div className="p-3 border-t-2 border-ctp-surface0 bg-ctp-mantle/50">
      <div className="flex gap-2">
        <input
          type="text"
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          placeholder="Send a message..."
          className="flex-1 bg-ctp-surface0 text-ctp-text text-sm px-3 py-2 border border-ctp-surface1 focus:border-ctp-mauve focus:outline-none placeholder:text-ctp-overlay0"
        />
        <button
          disabled={!draft.trim()}
          className="px-3 py-2 bg-ctp-mauve text-ctp-crust disabled:opacity-30 hover:brightness-110 transition-all"
        >
          <Send size={14} />
        </button>
      </div>
    </div>
  );
}
