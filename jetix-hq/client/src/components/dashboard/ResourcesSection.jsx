import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  PieChart, Pie, Cell,
  AreaChart, Area,
} from 'recharts';
import { ProgressBar, StatCard } from '../ui';
import { Clock, DollarSign, Target, Fuel, AlertTriangle } from 'lucide-react';

const ChartTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div className="bg-ctp-mantle border-2 border-ctp-surface1 p-2 text-[10px] font-mono">
      <p className="text-ctp-subtext0">{label}</p>
      {payload.map((p, i) => (
        <p key={i} style={{ color: p.color || p.fill }}>{p.name}: {p.value}</p>
      ))}
    </div>
  );
};

const PieLabel = ({ cx, cy, midAngle, innerRadius, outerRadius, name, percent }) => {
  const RADIAN = Math.PI / 180;
  const radius = outerRadius + 18;
  const x = cx + radius * Math.cos(-midAngle * RADIAN);
  const y = cy + radius * Math.sin(-midAngle * RADIAN);
  if (percent < 0.05) return null;
  return (
    <text x={x} y={y} textAnchor={x > cx ? 'start' : 'end'} dominantBaseline="central"
      fill="#a6adc8" fontSize={10} fontFamily="JetBrains Mono">
      {name}
    </text>
  );
};

export default function ResourcesSection({ resources }) {
  if (!resources) return null;
  const { time, money, attention, runway } = resources;

  const moneyPct = money.budget > 0 ? (money.spent / money.budget) * 100 : 0;
  const moneyWarning = moneyPct > 80;

  return (
    <div className="space-y-4">
      {/* Row 1: Time + Money */}
      <div className="grid grid-cols-2 gap-4">
        {/* TIME */}
        <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
          <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
            <h3 className="font-pixel text-[10px] text-ctp-subtext1">TIME</h3>
          </div>
          <div className="p-4 space-y-3">
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs text-ctp-subtext0">{time.logged}h / {time.available}h</span>
              <Clock size={14} className="text-ctp-overlay1" />
            </div>
            <ProgressBar
              value={time.logged}
              max={time.available}
              color="blue"
              size="md"
            />
            <ResponsiveContainer width="100%" height={120}>
              <BarChart data={time.byProject}>
                <CartesianGrid strokeDasharray="3 3" stroke="#313244" />
                <XAxis dataKey="name" tick={{ fill: '#a6adc8', fontSize: 9, fontFamily: 'JetBrains Mono' }} stroke="#313244" />
                <YAxis tick={{ fill: '#a6adc8', fontSize: 9 }} stroke="#313244" tickFormatter={(v) => `${v}h`} />
                <Tooltip content={<ChartTooltip />} />
                <Bar dataKey="hours" name="Hours">
                  {time.byProject.map((entry, i) => (
                    <Cell key={i} fill={entry.color} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* MONEY */}
        <div className={`bg-ctp-mantle border-2 rpg-clip ${moneyWarning ? 'border-ctp-red' : 'border-ctp-surface1'}`}>
          <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30 flex items-center justify-between">
            <h3 className="font-pixel text-[10px] text-ctp-subtext1">MONEY</h3>
            {moneyWarning && <AlertTriangle size={12} className="text-ctp-red" />}
          </div>
          <div className="p-4 space-y-3">
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs text-ctp-subtext0">${money.spent.toFixed(2)} / ${money.budget}</span>
              <DollarSign size={14} className="text-ctp-overlay1" />
            </div>
            <ProgressBar
              value={money.spent}
              max={money.budget}
              color={moneyWarning ? 'red' : 'green'}
              size="md"
            />
            {moneyWarning && (
              <p className="text-[10px] text-ctp-red font-mono">Budget &gt;80% — consider reducing agent calls</p>
            )}
            <div className="flex justify-center">
              <ResponsiveContainer width={180} height={140}>
                <PieChart>
                  <Pie
                    data={money.byCategory}
                    dataKey="value"
                    nameKey="name"
                    cx="50%"
                    cy="50%"
                    outerRadius={50}
                    innerRadius={25}
                    label={PieLabel}
                    strokeWidth={2}
                    stroke="#1e1e2e"
                  >
                    {money.byCategory.map((entry, i) => (
                      <Cell key={i} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip content={<ChartTooltip />} />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>
      </div>

      {/* Row 2: Attention + Runway */}
      <div className="grid grid-cols-2 gap-4">
        {/* ATTENTION */}
        <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
          <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
            <h3 className="font-pixel text-[10px] text-ctp-subtext1">ATTENTION FOCUS</h3>
          </div>
          <div className="p-4">
            <div className="flex justify-center">
              <ResponsiveContainer width={200} height={160}>
                <PieChart>
                  <Pie
                    data={attention.areas}
                    dataKey="weight"
                    nameKey="name"
                    cx="50%"
                    cy="50%"
                    outerRadius={60}
                    label={PieLabel}
                    strokeWidth={2}
                    stroke="#1e1e2e"
                  >
                    {attention.areas.map((entry, i) => (
                      <Cell key={i} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip content={<ChartTooltip />} />
                </PieChart>
              </ResponsiveContainer>
            </div>
            <div className="flex flex-wrap gap-2 mt-2 justify-center">
              {attention.areas.map((a) => (
                <div key={a.name} className="flex items-center gap-1.5 text-[10px]">
                  <div className="w-2 h-2" style={{ backgroundColor: a.color }} />
                  <span className="text-ctp-subtext0">{a.name} {a.weight}%</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* RUNWAY */}
        <div className="bg-ctp-mantle border-2 border-ctp-surface1 rpg-clip">
          <div className="px-4 py-2 border-b-2 border-ctp-surface1 bg-ctp-surface0/30">
            <h3 className="font-pixel text-[10px] text-ctp-subtext1">RUNWAY</h3>
          </div>
          <div className="p-4 space-y-3">
            <div className="grid grid-cols-3 gap-2">
              <div>
                <p className="text-[10px] text-ctp-overlay0">Balance</p>
                <p className="text-sm font-mono font-bold text-ctp-text">${runway.balance}</p>
              </div>
              <div>
                <p className="text-[10px] text-ctp-overlay0">Burn/mo</p>
                <p className="text-sm font-mono font-bold text-ctp-text">${runway.burnRate}</p>
              </div>
              <div>
                <p className="text-[10px] text-ctp-overlay0">Months</p>
                <p className="text-sm font-mono font-bold text-ctp-green">{runway.months}</p>
              </div>
            </div>
            <ResponsiveContainer width="100%" height={100}>
              <AreaChart data={runway.projection}>
                <CartesianGrid strokeDasharray="3 3" stroke="#313244" />
                <XAxis dataKey="month" tick={{ fill: '#a6adc8', fontSize: 9, fontFamily: 'JetBrains Mono' }} stroke="#313244" tickFormatter={(v) => v.slice(5)} />
                <YAxis tick={{ fill: '#a6adc8', fontSize: 9 }} stroke="#313244" tickFormatter={(v) => `$${v}`} />
                <Tooltip content={<ChartTooltip />} />
                <Area type="monotone" dataKey="balance" stroke="#a6e3a1" fill="#a6e3a1" fillOpacity={0.1} strokeWidth={2} />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
