import { BarChart3 } from 'lucide-react';

export default function Dashboard() {
  return (
    <div>
      <div className="flex items-center gap-3 mb-6">
        <BarChart3 size={24} className="text-ctp-green" />
        <h2 className="text-xl font-bold text-ctp-text">Dashboard</h2>
      </div>
      <div className="bg-ctp-mantle border border-ctp-surface0 rounded-lg p-8 text-center">
        <p className="text-ctp-subtext0">
          Revenue charts, task metrics, cost analytics, and achievements will appear here.
        </p>
      </div>
    </div>
  );
}
