import { useState } from 'react';
import { BarChart3, Layers, Eye } from 'lucide-react';
import useFetch from '../hooks/useFetch';
import { useWs } from '../hooks/useWebSocket';
import PeriodSelector from '../components/dashboard/PeriodSelector';
import KpiRow from '../components/dashboard/KpiRow';
import CostTrendChart from '../components/dashboard/CostTrendChart';
import AgentTokensChart from '../components/dashboard/AgentTokensChart';
import ActiveSessions from '../components/dashboard/ActiveSessions';
import ErrorLog from '../components/dashboard/ErrorLog';
import ResourcesSection from '../components/dashboard/ResourcesSection';

export default function Dashboard() {
  const [period, setPeriod] = useState('week');
  const [section, setSection] = useState('both'); // resources | observability | both
  const { on } = useWs();
  const { data, loading } = useFetch(`/api/v1/metrics?period=${period}`, {
    interval: 30000,
    wsEvents: ['resources:updated', 'agent:status'],
    onWs: on,
  });

  const showResources = section === 'resources' || section === 'both';
  const showObservability = section === 'observability' || section === 'both';

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <BarChart3 size={24} className="text-ctp-green" />
          <h2 className="font-pixel text-sm text-ctp-text">ANALYTICS</h2>
          {loading && (
            <span className="text-[10px] text-ctp-overlay0 font-mono animate-pulse">updating...</span>
          )}
        </div>
        <div className="flex items-center gap-3">
          {/* Section toggle */}
          <div className="flex border-2 border-ctp-surface1 overflow-hidden">
            {[
              { id: 'both', label: 'Both', icon: Layers },
              { id: 'resources', label: 'Resources', icon: Layers },
              { id: 'observability', label: 'Observe', icon: Eye },
            ].map(({ id, label }) => (
              <button
                key={id}
                onClick={() => setSection(id)}
                className={`px-3 py-1.5 text-[10px] font-mono transition-colors ${
                  section === id
                    ? 'bg-ctp-surface1 text-ctp-text'
                    : 'bg-ctp-surface0 text-ctp-overlay0 hover:text-ctp-text'
                }`}
              >
                {label}
              </button>
            ))}
          </div>
          <PeriodSelector value={period} onChange={setPeriod} />
        </div>
      </div>

      {/* Resources section */}
      {showResources && (
        <div>
          {section === 'both' && (
            <h3 className="font-pixel text-[10px] text-ctp-overlay1 mb-3">RESOURCES</h3>
          )}
          <ResourcesSection resources={data?.resources} />
        </div>
      )}

      {/* Observability section */}
      {showObservability && (
        <div className="space-y-4">
          {section === 'both' && (
            <h3 className="font-pixel text-[10px] text-ctp-overlay1 mb-3 mt-2">OBSERVABILITY</h3>
          )}

          {/* KPI Row */}
          <KpiRow kpi={data?.kpi} costTrend={data?.costTrend} />

          {/* Charts */}
          <div className="grid grid-cols-2 gap-4">
            <CostTrendChart data={data?.costTrend} />
            <AgentTokensChart data={data?.agentTokens} />
          </div>

          {/* Sessions + Errors */}
          <div className="grid grid-cols-2 gap-4">
            <ActiveSessions sessions={data?.activeSessions} />
            <ErrorLog errors={data?.errorLog} />
          </div>
        </div>
      )}
    </div>
  );
}
