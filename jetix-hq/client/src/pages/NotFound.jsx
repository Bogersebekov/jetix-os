import { useNavigate } from 'react-router-dom';
import { MapPin, Home } from 'lucide-react';

export default function NotFound() {
  const navigate = useNavigate();

  return (
    <div className="flex items-center justify-center h-[calc(100vh-8rem)]">
      <div className="text-center">
        <div className="p-6 bg-ctp-surface0 rpg-clip inline-block mb-6">
          <MapPin size={48} className="text-ctp-overlay1" />
        </div>
        <h1 className="font-pixel text-lg text-ctp-text mb-2">404</h1>
        <p className="font-pixel text-[10px] text-ctp-overlay1 mb-6">ROOM NOT FOUND</p>
        <p className="text-sm text-ctp-subtext0 mb-6 max-w-xs mx-auto">
          This area of the HQ hasn't been built yet, or you've wandered off the map.
        </p>
        <button
          onClick={() => navigate('/hq')}
          className="inline-flex items-center gap-2 px-6 py-3 bg-ctp-mauve text-ctp-crust font-semibold rpg-clip hover:brightness-110 transition-all"
        >
          <Home size={16} /> Return to HQ
        </button>
      </div>
    </div>
  );
}
