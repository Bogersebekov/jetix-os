import { useState, useEffect } from 'react';
import { Badge, StatusDot } from '../ui';

function formatDuration(seconds) {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m}:${String(s).padStart(2, '0')}`;
}

function LiveTimer({ startedAt, running }) {
  const [elapsed, setElapsed] = useState(0);

  useEffect(() => {
    if (!running) return;
    const start = new Date(startedAt).getTime();
    const tick = () => setElapsed(Math.floor((Date.now() - start) / 1000));
    tick();
    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, [startedAt, running]);

  if (!running) return <span>--</span>;
  return <span>{formatDuration(elapsed)}</span>;
}

export default function ActiveSessions({ sessions }) {
  if (!sessions || sessions.length === 0) {
    return (
      <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip p-4">
        <p className="text-xs text-ctp-overlay0 text-center py-4">No active sessions</p>
      </div>
    );
  }

  const statusMap = {
    running: 'active',
    completed: 'offline',
    error: 'error',
  };

  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
      <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
        <h3 className="font-pixel text-[10px] text-ctp-subtext1">ACTIVE SESSIONS</h3>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-xs">
          <thead>
            <tr className="text-ctp-overlay0 font-mono text-left border-b-2 border-ctp-surface0">
              <th className="px-4 py-2 font-normal">Agent</th>
              <th className="px-4 py-2 font-normal">Task</th>
              <th className="px-4 py-2 font-normal">Duration</th>
              <th className="px-4 py-2 font-normal">Tokens</th>
              <th className="px-4 py-2 font-normal">Status</th>
            </tr>
          </thead>
          <tbody>
            {sessions.map((s) => (
              <tr key={s.id} className="border-b border-ctp-surface0/50 hover:bg-ctp-surface0/20">
                <td className="px-4 py-2.5">
                  <div className="flex items-center gap-2">
                    <StatusDot status={statusMap[s.status] || 'offline'} size={6} />
                    <span className="text-ctp-text">{s.agent}</span>
                  </div>
                </td>
                <td className="px-4 py-2.5 text-ctp-subtext0 font-mono">{s.task}</td>
                <td className="px-4 py-2.5 font-mono text-ctp-subtext1">
                  {s.status === 'running' ? (
                    <LiveTimer startedAt={s.startedAt} running />
                  ) : (
                    formatDuration(s.duration)
                  )}
                </td>
                <td className="px-4 py-2.5 font-mono text-ctp-subtext0">
                  {s.tokens.toLocaleString()}
                </td>
                <td className="px-4 py-2.5">
                  <Badge status={statusMap[s.status] || 'offline'} label={s.status} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
