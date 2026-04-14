import { Building2 } from 'lucide-react';

export default function HQ() {
  return (
    <div>
      <div className="flex items-center gap-3 mb-6">
        <Building2 size={24} className="text-ctp-blue" />
        <h2 className="text-xl font-bold text-ctp-text">Headquarters</h2>
      </div>
      <div className="bg-ctp-mantle border border-ctp-surface0 rounded-lg p-8 text-center">
        <p className="text-ctp-subtext0">
          Company overview, agent map, and live status will appear here.
        </p>
      </div>
    </div>
  );
}
