import { StatCard, EmptyState } from '../ui';
import { Zap, Coins, Clock, AlertTriangle, Hash } from 'lucide-react';
import {
  AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid,
} from 'recharts';

const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 p-2 text-xs font-mono">
      <p className="text-ctp-subtext0">{label}</p>
      <p className="text-ctp-blue">tokens: {payload[0]?.value?.toLocaleString()}</p>
    </div>
  );
};

export default function AgentMetrics({ metrics }) {
  if (!metrics) return <EmptyState title="No metrics" className="py-16" />;

  const hasHistory = metrics.tokenHistory?.some((d) => d.tokens > 0);

  return (
    <div className="p-4 space-y-4">
      {/* KPIs */}
      <div className="grid grid-cols-5 gap-3">
        <StatCard label="Tasks Today" value={metrics.tasksToday} icon={Hash} />
        <StatCard label="Tokens Today" value={metrics.tokensToday.toLocaleString()} icon={Zap} />
        <StatCard label="Cost Today" value={`$${metrics.costToday.toFixed(2)}`} icon={Coins} />
        <StatCard label="Avg Task Time" value={metrics.avgTaskTime ? `${metrics.avgTaskTime}s` : '--'} icon={Clock} />
        <StatCard label="Error Rate" value={`${metrics.errorRate}%`} icon={AlertTriangle} />
      </div>

      {/* Token chart */}
      <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
        <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
          <h3 className="font-pixel text-[10px] text-ctp-subtext1">TOKENS / DAY (14d)</h3>
        </div>
        <div className="p-4">
          {hasHistory ? (
            <ResponsiveContainer width="100%" height={200}>
              <AreaChart data={metrics.tokenHistory}>
                <CartesianGrid strokeDasharray="3 3" stroke="#313244" />
                <XAxis
                  dataKey="date"
                  tick={{ fill: '#6c7086', fontSize: 10, fontFamily: 'JetBrains Mono' }}
                  tickFormatter={(v) => v.slice(5)}
                  stroke="#313244"
                />
                <YAxis
                  tick={{ fill: '#6c7086', fontSize: 10, fontFamily: 'JetBrains Mono' }}
                  stroke="#313244"
                />
                <Tooltip content={<CustomTooltip />} />
                <Area
                  type="stepAfter"
                  dataKey="tokens"
                  stroke="#89b4fa"
                  fill="#89b4fa"
                  fillOpacity={0.15}
                  strokeWidth={2}
                />
              </AreaChart>
            </ResponsiveContainer>
          ) : (
            <div className="h-[200px] flex items-center justify-center text-xs text-ctp-overlay0">
              No token data yet
            </div>
          )}
        </div>
      </div>

      {/* Recent tasks table */}
      <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
        <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
          <h3 className="font-pixel text-[10px] text-ctp-subtext1">RECENT TASKS (10)</h3>
        </div>
        <div className="p-4">
          {metrics.recentTasks?.length > 0 ? (
            <table className="w-full text-xs">
              <thead>
                <tr className="text-ctp-overlay0 font-mono text-left border-b border-ctp-surface0">
                  <th className="pb-2 font-normal">Task</th>
                  <th className="pb-2 font-normal">Status</th>
                  <th className="pb-2 font-normal">Tokens</th>
                  <th className="pb-2 font-normal">Time</th>
                </tr>
              </thead>
              <tbody>
                {metrics.recentTasks.map((task, i) => (
                  <tr key={i} className="border-b border-ctp-surface0/50">
                    <td className="py-2 text-ctp-text">{task.title}</td>
                    <td className="py-2 text-ctp-subtext0">{task.status}</td>
                    <td className="py-2 font-mono text-ctp-subtext0">{task.tokens}</td>
                    <td className="py-2 font-mono text-ctp-subtext0">{task.time}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p className="text-xs text-ctp-overlay0 text-center py-4">No tasks recorded yet</p>
          )}
        </div>
      </div>
    </div>
  );
}
