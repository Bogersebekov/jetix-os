import { useState, useCallback } from 'react';
import useFetch from '../hooks/useFetch';
import { useWs } from '../hooks/useWebSocket';
import { rooms } from '../data/rooms';
import { getCompanyLevel } from '../data/rooms';
import CompanyHeader from '../components/hq/CompanyHeader';
import PixelOffice from '../components/pixel/PixelOffice';
import AgentPopup from '../components/hq/AgentPopup';
import ProjectCards from '../components/hq/ProjectCards';
import ActivityFeed from '../components/hq/ActivityFeed';
import ResourceBar from '../components/hq/ResourceBar';
import XpPopup from '../components/pixel/XpPopup';
import LevelUpOverlay from '../components/pixel/LevelUpOverlay';

export default function HQ() {
  const [popupAgent, setPopupAgent] = useState(null);
  const [xpPopups, setXpPopups] = useState([]);
  const [levelUp, setLevelUp] = useState(null);
  const [companyXp, setCompanyXp] = useState(1250);
  const { on } = useWs();

  const { data } = useFetch('/api/v1/agents', {
    interval: 30000,
    wsEvents: ['agent:status', 'comms:message'],
    onWs: on,
  });

  const agents = data?.agents || [];
  const activeCount = agents.filter((a) => a.status === 'active').length;

  const budget = { spent: 4.20, total: 150 };
  const streak = 3;

  // Demo XP gain on header XP bar click
  const handleXpClick = useCallback(() => {
    const amount = [25, 50, 100][Math.floor(Math.random() * 3)];
    const prevLevel = getCompanyLevel(companyXp);
    const newXp = companyXp + amount;
    const newLevel = getCompanyLevel(newXp);

    // XP popup
    const id = Date.now();
    setXpPopups((prev) => [...prev, { id, amount, x: window.innerWidth / 2, y: 80 }]);

    setCompanyXp(newXp);

    // Level up check
    if (newLevel.level > prevLevel.level) {
      setTimeout(() => {
        setLevelUp({ level: newLevel.level, name: newLevel.name, icon: newLevel.icon });
      }, 500);
    }
  }, [companyXp]);

  const removeXpPopup = useCallback((id) => {
    setXpPopups((prev) => prev.filter((p) => p.id !== id));
  }, []);

  return (
    <div className="space-y-4 -m-6 p-6 min-h-[calc(100vh-5rem)]">
      {/* Company Header */}
      <CompanyHeader
        companyXp={companyXp}
        streak={streak}
        budget={budget}
        activeAgents={activeCount}
        totalAgents={agents.length || 12}
        onXpClick={handleXpClick}
      />

      {/* Pixel Office */}
      <PixelOffice
        agents={agents}
        rooms={rooms}
        onAgentClick={setPopupAgent}
      />

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

      {/* XP popups */}
      {xpPopups.map((p) => (
        <XpPopup key={p.id} amount={p.amount} x={p.x} y={p.y} onDone={() => removeXpPopup(p.id)} />
      ))}

      {/* Level up overlay */}
      {levelUp && (
        <LevelUpOverlay
          level={levelUp.level}
          levelName={levelUp.name}
          levelIcon={levelUp.icon}
          onDone={() => setLevelUp(null)}
        />
      )}
    </div>
  );
}
