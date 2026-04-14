import { Badge } from '../ui';

export default function AgentConfig({ agent }) {
  const cfg = agent.config || {};

  return (
    <div className="p-4 space-y-4">
      {/* Read-only fields */}
      <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
        <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
          <h3 className="font-pixel text-[10px] text-ctp-subtext1">CONFIGURATION</h3>
        </div>
        <div className="p-4 space-y-3">
          <ConfigRow label="Model" value={agent.model} />
          <ConfigRow label="Max Turns" value={cfg.maxTurns || '--'} />
          <ConfigRow label="Permission Mode" value={cfg.permissionMode || '--'} />
          <ConfigRow label="Phase" value={String(agent.phase)} />
          <ConfigRow label="Department" value={agent.dept} />
          <div className="flex items-center justify-between">
            <span className="text-sm text-ctp-subtext0">Auto Restart</span>
            <Badge status="offline" label="disabled" />
          </div>
          <div className="flex items-center justify-between">
            <span className="text-sm text-ctp-subtext0">Priority</span>
            <span className="font-mono text-xs text-ctp-text">normal</span>
          </div>
        </div>
      </div>

      {/* System prompt preview */}
      <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
        <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30 flex items-center justify-between">
          <h3 className="font-pixel text-[10px] text-ctp-subtext1">SYSTEM PROMPT</h3>
          <span className="text-[10px] text-ctp-overlay0 font-mono">read-only</span>
        </div>
        <div className="p-4">
          {cfg.systemPrompt ? (
            <pre className="text-xs text-ctp-subtext0 font-mono whitespace-pre-wrap max-h-96 overflow-y-auto leading-relaxed">
              {cfg.systemPrompt}
            </pre>
          ) : (
            <p className="text-xs text-ctp-overlay0">No system prompt loaded</p>
          )}
        </div>
      </div>
    </div>
  );
}

function ConfigRow({ label, value }) {
  return (
    <div className="flex items-center justify-between">
      <span className="text-sm text-ctp-subtext0">{label}</span>
      <span className="font-mono text-xs text-ctp-text">{value}</span>
    </div>
  );
}
