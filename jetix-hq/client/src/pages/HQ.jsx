import { Building2, Users, DollarSign, Zap } from 'lucide-react';
import { Card, StatCard, ProgressBar, Badge } from '../components/ui';

export default function HQ() {
  return (
    <div className="space-y-6">
      <div className="flex items-center gap-3">
        <Building2 size={24} className="text-ctp-mauve" />
        <h2 className="font-pixel text-sm text-ctp-text">HEADQUARTERS</h2>
        <Badge status="active" label="online" />
      </div>

      {/* Stats row */}
      <div className="grid grid-cols-4 gap-4">
        <StatCard label="Revenue" value="$0" trend="flat" trendLabel="target: $50K" icon={DollarSign} />
        <StatCard label="Agents" value="0/12" trend="flat" trendLabel="Phase 1" icon={Users} />
        <StatCard label="Tasks Today" value="0" trend="flat" icon={Zap} />
        <StatCard label="Company Level" value="1" trend="flat" trendLabel="Garage" icon={Building2} />
      </div>

      {/* Company XP */}
      <Card title="COMPANY PROGRESS" pixel>
        <ProgressBar value={0} max={5000} color="mauve" label="XP to Level 2: Small Office" showValue size="lg" />
        <p className="text-xs text-ctp-overlay1 mt-3">
          Reach $5,000 revenue to unlock Level 2
        </p>
      </Card>

      {/* Department grid placeholder */}
      <div className="grid grid-cols-3 gap-4">
        {['MGMT', 'SALES', 'BRAIN', 'OPS', 'LIFE', 'META'].map((dept) => (
          <Card key={dept} pixel>
            <p className="font-pixel text-[10px] text-ctp-overlay1 mb-2">{dept}</p>
            <p className="text-sm text-ctp-subtext0">No agents online</p>
          </Card>
        ))}
      </div>
    </div>
  );
}
