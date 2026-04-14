import { useState } from 'react';
import { ChevronDown, ChevronRight, AlertTriangle, XCircle } from 'lucide-react';

export default function ErrorLog({ errors }) {
  const [expanded, setExpanded] = useState({});

  if (!errors || errors.length === 0) {
    return (
      <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip p-4">
        <p className="text-xs text-ctp-overlay0 text-center py-4">No errors</p>
      </div>
    );
  }

  const toggle = (id) => setExpanded((p) => ({ ...p, [id]: !p[id] }));

  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
      <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30 flex items-center justify-between">
        <h3 className="font-pixel text-[10px] text-ctp-subtext1">ERROR LOG</h3>
        <span className="text-[10px] font-mono text-ctp-overlay0">{errors.length} entries</span>
      </div>
      <div className="divide-y divide-ctp-surface0/50">
        {errors.map((err) => {
          const isError = err.severity === 'error';
          const Icon = isError ? XCircle : AlertTriangle;
          const color = isError ? 'text-ctp-red' : 'text-ctp-yellow';

          return (
            <div key={err.id}>
              <button
                onClick={() => toggle(err.id)}
                className="w-full flex items-center gap-3 px-4 py-2.5 text-left hover:bg-ctp-surface0/20 transition-colors"
              >
                {expanded[err.id] ? (
                  <ChevronDown size={12} className="text-ctp-overlay0 shrink-0" />
                ) : (
                  <ChevronRight size={12} className="text-ctp-overlay0 shrink-0" />
                )}
                <Icon size={14} className={`${color} shrink-0`} />
                <span className="text-xs text-ctp-text flex-1 truncate">{err.message}</span>
                <span className="text-[10px] font-mono text-ctp-overlay0 shrink-0">
                  {new Date(err.timestamp).toLocaleTimeString()}
                </span>
              </button>
              {expanded[err.id] && (
                <div className="px-4 pb-3 pl-12 space-y-1">
                  <p className="text-[10px] text-ctp-overlay1">
                    <span className="text-ctp-subtext0">Agent:</span> {err.agent}
                  </p>
                  <p className="text-[10px] text-ctp-overlay1">
                    <span className="text-ctp-subtext0">Severity:</span>{' '}
                    <span className={color}>{err.severity}</span>
                  </p>
                  <p className="text-[10px] text-ctp-overlay1">
                    <span className="text-ctp-subtext0">Time:</span> {new Date(err.timestamp).toLocaleString()}
                  </p>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
