import { useState } from 'react';
import useFetch from '../hooks/useFetch';
import { useWs } from '../hooks/useWebSocket';
import { rooms } from '../data/rooms';
import CompanyHeader from '../components/hq/CompanyHeader';
import OfficeRoom from '../components/hq/OfficeRoom';
import AgentPopup from '../components/hq/AgentPopup';
import ProjectCards from '../components/hq/ProjectCards';
import ActivityFeed from '../components/hq/ActivityFeed';
import ResourceBar from '../components/hq/ResourceBar';

export default function HQ() {
  const [popupAgent, setPopupAgent] = useState(null);
  const { on } = useWs();

  const { data } = useFetch('/api/v1/agents', {
    interval: 30000,
    wsEvents: ['agent:status', 'comms:message'],
    onWs: on,
  });

  const agents = data?.agents || [];
  const agentMap = Object.fromEntries(agents.map((a) => [a.id, a]));
  const activeCount = agents.filter((a) => a.status === 'active').length;

  // Mock company data
  const companyXp = 1250;
  const streak = 3;
  const budget = { spent: 4.20, total: 150 };

  return (
    <div className="space-y-4 -m-6 p-6 min-h-[calc(100vh-5rem)]">
      {/* Company Header */}
      <CompanyHeader
        companyXp={companyXp}
        streak={streak}
        budget={budget}
        activeAgents={activeCount}
        totalAgents={agents.length || 12}
      />

      {/* Virtual Office: CSS Grid 4x2 */}
      <div className="grid grid-cols-4 grid-rows-2 gap-3">
        {rooms.map((room) => {
          const roomAgents = room.agents.map((id) => agentMap[id]).filter(Boolean);
          return (
            <OfficeRoom
              key={room.id}
              room={room}
              agents={roomAgents}
              onAgentClick={setPopupAgent}
            />
          );
        })}
      </div>

      {/* Bottom: Projects + Activity Feed */}
      <div className="grid grid-cols-3 gap-3">
        <div className="col-span-2">
          <div className="mb-2">
            <h3 className="font-pixel text-[9px] text-ctp-overlay1">PROJECTS</h3>
          </div>
          <ProjectCards />
        </div>
        <div className="h-64">
          <ActivityFeed />
        </div>
      </div>

      {/* Resource Bar */}
      <ResourceBar
        time={{ used: 2, total: 5 }}
        money={{ spent: budget.spent, budget: budget.total }}
        focus={[
          { name: 'Sales', weight: 35, color: '#a6e3a1' },
          { name: 'Ops', weight: 25, color: '#89b4fa' },
          { name: 'Research', weight: 20, color: '#94e2d5' },
          { name: 'Strategy', weight: 12, color: '#cba6f7' },
          { name: 'Other', weight: 8, color: '#585b70' },
        ]}
      />

      {/* Agent popup */}
      {popupAgent && (
        <AgentPopup agent={popupAgent} onClose={() => setPopupAgent(null)} />
      )}
    </div>
  );
}
