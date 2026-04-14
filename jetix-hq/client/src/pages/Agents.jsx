import { useState } from 'react';
import { Users } from 'lucide-react';
import useFetch from '../hooks/useFetch';
import { useWs } from '../hooks/useWebSocket';
import AgentList from '../components/agents/AgentList';
import AgentDetail from '../components/agents/AgentDetail';

export default function Agents() {
  const [selectedId, setSelectedId] = useState('manager');
  const { on } = useWs();
  const { data, loading } = useFetch('/api/v1/agents', {
    interval: 30000,
    wsEvents: ['agent:status', 'comms:message'],
    onWs: on,
  });

  const agents = data?.agents || [];

  return (
    <div className="flex h-[calc(100vh-5rem)] -m-6">
      {/* Left panel: agent list */}
      <div className="w-80 shrink-0 border-r-2 border-ctp-surface0 bg-ctp-mantle/30 overflow-hidden">
        {loading && agents.length === 0 ? (
          <div className="flex items-center justify-center h-full">
            <p className="text-xs text-ctp-overlay0">Loading agents...</p>
          </div>
        ) : (
          <AgentList
            agents={agents}
            selectedId={selectedId}
            onSelect={setSelectedId}
          />
        )}
      </div>

      {/* Right panel: agent detail */}
      <div className="flex-1 overflow-hidden bg-ctp-base">
        {selectedId ? (
          <AgentDetail agentId={selectedId} />
        ) : (
          <div className="flex items-center justify-center h-full">
            <div className="text-center">
              <Users size={32} className="text-ctp-overlay0 mx-auto mb-3" />
              <p className="text-sm text-ctp-overlay1">Select an agent to view details</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
