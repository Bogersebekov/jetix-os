import { useState } from 'react';
import {
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend,
} from 'recharts';

const AGENT_COLORS = {
  manager: '#cba6f7',
  strategist: '#f5c2e7',
  'sales-lead': '#a6e3a1',
  'sales-researcher': '#94e2d5',
  'sales-outreach': '#89dcfe',
  'inbox-processor': '#89b4fa',
  'knowledge-synth': '#74c7ec',
  'personal-assistant': '#fab387',
  'system-admin': '#f9e2af',
  'life-coach': '#f5e0dc',
  'meta-agent': '#b4befe',
  'crazy-agent': '#eba0ac',
};

const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 p-2 text-[10px] font-mono max-w-[200px]">
      <p className="text-ctp-subtext0 mb-1">{label}</p>
      {payload.map((p) => (
        <div key={p.dataKey} className="flex justify-between gap-3">
          <span style={{ color: p.color }}>{p.dataKey}</span>
          <span className="text-ctp-text">${p.value?.toFixed(4)}</span>
        </div>
      ))}
    </div>
  );
};

export default function CostTrendChart({ data }) {
  const [range, setRange] = useState('all');

  if (!data || data.length === 0) {
    return (
      <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip p-4">
        <p className="text-xs text-ctp-overlay0 text-center py-8">No cost trend data</p>
      </div>
    );
  }

  const sliced = range === '7d' ? data.slice(-7) : data;

  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
      <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30 flex items-center justify-between">
        <h3 className="font-pixel text-[10px] text-ctp-subtext1">COST TREND</h3>
        <div className="flex gap-1">
          {['7d', 'all'].map((r) => (
            <button
              key={r}
              onClick={() => setRange(r)}
              className={`px-2 py-0.5 text-[10px] font-mono border ${
                range === r ? 'border-ctp-mauve text-ctp-text' : 'border-ctp-surface1 text-ctp-overlay0'
              }`}
            >
              {r === 'all' ? 'All' : '7d'}
            </button>
          ))}
        </div>
      </div>
      <div className="p-4">
        <ResponsiveContainer width="100%" height={240}>
          <AreaChart data={sliced}>
            <CartesianGrid strokeDasharray="3 3" stroke="#313244" />
            <XAxis
              dataKey="date"
              tick={{ fill: '#a6adc8', fontSize: 10, fontFamily: 'JetBrains Mono' }}
              tickFormatter={(v) => v.slice(5)}
              stroke="#313244"
            />
            <YAxis
              tick={{ fill: '#a6adc8', fontSize: 10, fontFamily: 'JetBrains Mono' }}
              tickFormatter={(v) => `$${v}`}
              stroke="#313244"
            />
            <Tooltip content={<CustomTooltip />} />
            <Area
              type="monotone"
              dataKey="cost"
              stroke="#cba6f7"
              fill="#cba6f7"
              fillOpacity={0.15}
              strokeWidth={2}
              name="cost"
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
