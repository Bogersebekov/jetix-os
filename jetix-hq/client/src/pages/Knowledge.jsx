import { BookOpen } from 'lucide-react';

export default function Knowledge() {
  return (
    <div>
      <div className="flex items-center gap-3 mb-6">
        <BookOpen size={24} className="text-ctp-teal" />
        <h2 className="text-xl font-bold text-ctp-text">Knowledge</h2>
      </div>
      <div className="bg-ctp-mantle border border-ctp-surface0 rounded-lg p-8 text-center">
        <p className="text-ctp-subtext0">
          Knowledge base browser, research summaries, and decision log will appear here.
        </p>
      </div>
    </div>
  );
}
