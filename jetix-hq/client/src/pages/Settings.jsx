import { Settings as SettingsIcon } from 'lucide-react';

export default function Settings() {
  return (
    <div>
      <div className="flex items-center gap-3 mb-6">
        <SettingsIcon size={24} className="text-ctp-overlay2" />
        <h2 className="text-xl font-bold text-ctp-text">Settings</h2>
      </div>
      <div className="bg-ctp-mantle border border-ctp-surface0 rounded-lg p-8 text-center">
        <p className="text-ctp-subtext0">
          System configuration, agent toggles, and API key management will appear here.
        </p>
      </div>
    </div>
  );
}
