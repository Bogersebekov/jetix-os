import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend,
} from 'recharts';

const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 p-2 text-[10px] font-mono">
      <p className="text-ctp-subtext0 mb-1">{label}</p>
      {payload.map((p) => (
        <div key={p.dataKey} className="flex justify-between gap-3">
          <span style={{ color: p.fill }}>{p.dataKey}</span>
          <span className="text-ctp-text">{p.value?.toLocaleString()}</span>
        </div>
      ))}
    </div>
  );
};

export default function AgentTokensChart({ data }) {
  if (!data || data.length === 0) return null;

  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
      <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
        <h3 className="font-pixel text-[10px] text-ctp-subtext1">TOKEN USAGE BY AGENT</h3>
      </div>
      <div className="p-4">
        <ResponsiveContainer width="100%" height={Math.max(200, data.length * 36)}>
          <BarChart data={data} layout="vertical" margin={{ left: 20 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#313244" horizontal={false} />
            <XAxis
              type="number"
              tick={{ fill: '#a6adc8', fontSize: 10, fontFamily: 'JetBrains Mono' }}
              tickFormatter={(v) => v >= 1000 ? `${(v / 1000).toFixed(0)}k` : v}
              stroke="#313244"
            />
            <YAxis
              dataKey="name"
              type="category"
              tick={{ fill: '#a6adc8', fontSize: 10, fontFamily: 'JetBrains Mono' }}
              width={120}
              stroke="#313244"
            />
            <Tooltip content={<CustomTooltip />} />
            <Legend
              wrapperStyle={{ fontSize: 10, fontFamily: 'JetBrains Mono' }}
            />
            <Bar dataKey="inputTokens" name="Input" fill="#89b4fa" stackId="tokens" />
            <Bar dataKey="outputTokens" name="Output" fill="#cba6f7" stackId="tokens" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
