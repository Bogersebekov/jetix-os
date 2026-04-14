import { Settings as SettingsIcon } from 'lucide-react';
import { Card, Button, Badge } from '../components/ui';

export default function Settings() {
  return (
    <div className="space-y-6">
      <div className="flex items-center gap-3">
        <SettingsIcon size={24} className="text-ctp-overlay2" />
        <h2 className="font-pixel text-sm text-ctp-text">SETTINGS</h2>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <Card title="SYSTEM" pixel>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm text-ctp-subtext0">Jetix Root</span>
              <span className="font-mono text-xs text-ctp-overlay1">/jetix</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-ctp-subtext0">API</span>
              <Badge status="offline" label="not connected" />
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-ctp-subtext0">Database</span>
              <Badge status="active" label="sqlite" />
            </div>
          </div>
        </Card>

        <Card title="AGENTS" pixel>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm text-ctp-subtext0">Total Agents</span>
              <span className="font-mono text-sm text-ctp-text">12</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-ctp-subtext0">Active</span>
              <span className="font-mono text-sm text-ctp-text">0</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-ctp-subtext0">A/B Tests</span>
              <Badge status="offline" label="none" />
            </div>
          </div>
        </Card>

        <Card title="ACTIONS" pixel>
          <div className="flex flex-wrap gap-2">
            <Button variant="primary" size="sm">Run Health Check</Button>
            <Button variant="secondary" size="sm">Clear Mailboxes</Button>
            <Button variant="danger" size="sm">Reset Metrics</Button>
          </div>
        </Card>

        <Card title="THEME" pixel>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm text-ctp-subtext0">Color Scheme</span>
              <span className="font-mono text-xs text-ctp-mauve">Catppuccin Mocha</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-ctp-subtext0">Pixel Mode</span>
              <Badge status="active" label="on" />
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
}
