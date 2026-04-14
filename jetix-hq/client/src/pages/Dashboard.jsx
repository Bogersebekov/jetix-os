import { BarChart3, DollarSign, Cpu, TrendingUp, Clock } from 'lucide-react';
import { Card, StatCard, ProgressBar, EmptyState } from '../components/ui';

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <div className="flex items-center gap-3">
        <BarChart3 size={24} className="text-ctp-green" />
        <h2 className="font-pixel text-sm text-ctp-text">ANALYTICS</h2>
      </div>

      <div className="grid grid-cols-4 gap-4">
        <StatCard label="Revenue (total)" value="$0" trend="flat" icon={DollarSign} />
        <StatCard label="API Cost (today)" value="$0.00" trend="flat" icon={Cpu} />
        <StatCard label="Tasks (today)" value="0" trend="flat" icon={TrendingUp} />
        <StatCard label="Uptime" value="--" trend="flat" icon={Clock} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <Card title="REVENUE PROGRESS" pixel>
          <ProgressBar value={0} max={50000} color="green" label="$0 / $50,000" showValue size="lg" />
          <p className="text-xs text-ctp-overlay1 mt-2">Target: June 30, 2026</p>
        </Card>

        <Card title="API COST BREAKDOWN" pixel>
          <EmptyState title="No cost data" description="Costs will appear after first agent run" />
        </Card>
      </div>

      <Card title="TASK HISTORY" pixel>
        <EmptyState title="No tasks yet" description="Task metrics will populate as agents complete work" />
      </Card>
    </div>
  );
}
