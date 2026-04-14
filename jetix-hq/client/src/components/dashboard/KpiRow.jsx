import { Zap, Coins, Radio, AlertTriangle, Clock } from 'lucide-react';
import { LineChart, Line, ResponsiveContainer } from 'recharts';

const kpiDefs = [
  { key: 'tokens', label: 'Tokens', icon: Zap, format: (v) => v.toLocaleString(), color: '#89b4fa' },
  { key: 'cost', label: 'Cost', icon: Coins, format: (v) => `$${v.toFixed(2)}`, color: '#a6e3a1' },
  { key: 'sessions', label: 'Sessions', icon: Radio, format: (v) => String(v), color: '#cba6f7' },
  { key: 'errorRate', label: 'Error Rate', icon: AlertTriangle, format: (v) => `${v}%`, color: '#f38ba8' },
  { key: 'avgTime', label: 'Avg Time', icon: Clock, format: (v) => `${v}s`, color: '#fab387' },
];

// Mini sparkline data (last 7 points from costTrend or synthetic)
function makeSparkline(costTrend, key) {
  if (!costTrend || costTrend.length === 0) return Array(7).fill({ v: 0 });
  const slice = costTrend.slice(-7);
  const field = key === 'cost' ? 'cost' : key === 'sessions' ? 'sessions' : key === 'errorRate' ? 'errors' : 'tokens';
  return slice.map((d) => ({ v: d[field] || 0 }));
}

export default function KpiRow({ kpi, costTrend }) {
  if (!kpi) return null;

  return (
    <div className="grid grid-cols-5 gap-3">
      {kpiDefs.map(({ key, label, icon: Icon, format, color }) => {
        const data = kpi[key];
        if (!data) return null;
        const sparkData = makeSparkline(costTrend, key);
        const deltaPositive = data.delta > 0;
        const deltaColor =
          key === 'errorRate'
            ? deltaPositive ? 'text-ctp-red' : 'text-ctp-green'
            : deltaPositive ? 'text-ctp-green' : data.delta < 0 ? 'text-ctp-red' : 'text-ctp-overlay0';

        return (
          <div
            key={key}
            className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip p-3"
          >
            <div className="flex items-center justify-between mb-1">
              <span className="text-[10px] text-ctp-subtext0">{label}</span>
              <Icon size={14} className="text-ctp-overlay1" />
            </div>
            <div className="flex items-end justify-between">
              <div>
                <p className="text-xl font-bold font-mono text-ctp-text">{format(data.value)}</p>
                {data.delta !== 0 && (
                  <span className={`text-[10px] font-mono ${deltaColor}`}>
                    {data.delta > 0 ? '+' : ''}{key === 'cost' ? `$${data.delta}` : data.delta}
                  </span>
                )}
              </div>
              <div className="w-16 h-8">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={sparkData}>
                    <Line type="monotone" dataKey="v" stroke={color} strokeWidth={1.5} dot={false} />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}
