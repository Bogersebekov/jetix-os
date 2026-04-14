import { BookOpen } from 'lucide-react';
import { Card, EmptyState } from '../components/ui';

const sections = [
  { id: 'research', label: 'Research Summaries', count: 0 },
  { id: 'clients', label: 'Client Insights', count: 0 },
  { id: 'decisions', label: 'Decision Log', count: 0 },
  { id: 'crazy', label: 'Crazy Ideas', count: 0 },
  { id: 'life', label: 'Life & Wellness', count: 0 },
  { id: 'lessons', label: 'Lessons Learned', count: 0 },
];

export default function Knowledge() {
  return (
    <div className="space-y-6">
      <div className="flex items-center gap-3">
        <BookOpen size={24} className="text-ctp-teal" />
        <h2 className="font-pixel text-sm text-ctp-text">KNOWLEDGE BASE</h2>
      </div>

      <div className="grid grid-cols-3 gap-4">
        {sections.map((sec) => (
          <Card key={sec.id} className="hover:border-ctp-surface2 transition-colors cursor-pointer">
            <div className="flex items-center justify-between mb-2">
              <p className="font-pixel text-[10px] text-ctp-subtext1">{sec.label}</p>
              <span className="font-mono text-xs text-ctp-overlay0">{sec.count}</span>
            </div>
            <p className="text-xs text-ctp-overlay1">No entries yet</p>
          </Card>
        ))}
      </div>

      <Card title="RECENT ENTRIES" pixel>
        <EmptyState title="No entries" description="Knowledge will appear as agents synthesize information" />
      </Card>
    </div>
  );
}
