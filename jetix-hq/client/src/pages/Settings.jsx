import { useState, useEffect, useCallback } from 'react';
import {
  Settings as SettingsIcon, Save, RotateCcw, CheckCircle, XCircle,
  Download, Database, Info, Bell, Bot, FolderOpen, Palette,
} from 'lucide-react';
import { Card, Button, Badge } from '../components/ui';
import useFetch from '../hooks/useFetch';

const API = import.meta.env.VITE_API_URL || '';

const SECTIONS = [
  { id: 'general', label: 'General', icon: Palette },
  { id: 'agents', label: 'Agent Defaults', icon: Bot },
  { id: 'paths', label: 'Paths', icon: FolderOpen },
  { id: 'notifications', label: 'Notifications', icon: Bell },
  { id: 'backup', label: 'Backup', icon: Database },
  { id: 'about', label: 'About', icon: Info },
];

export default function Settings() {
  const [activeSection, setActiveSection] = useState('general');
  const { data: config, loading, refetch } = useFetch('/api/v1/system/config');
  const [form, setForm] = useState(null);
  const [dirty, setDirty] = useState(false);
  const [saving, setSaving] = useState(false);
  const [pathResults, setPathResults] = useState(null);

  useEffect(() => {
    if (config && !form) setForm(config);
  }, [config, form]);

  // Warn on leave if dirty
  useEffect(() => {
    if (!dirty) return;
    const handler = (e) => { e.preventDefault(); e.returnValue = ''; };
    window.addEventListener('beforeunload', handler);
    return () => window.removeEventListener('beforeunload', handler);
  }, [dirty]);

  function updateField(section, key, value) {
    setForm((prev) => ({
      ...prev,
      [section]: { ...prev[section], [key]: value },
    }));
    setDirty(true);
  }

  async function handleSave() {
    setSaving(true);
    try {
      await fetch(`${API}/api/v1/system/config`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });
      setDirty(false);
      refetch();
    } catch { /* ignore */ }
    setSaving(false);
  }

  function handleReset() {
    setForm(config);
    setDirty(false);
  }

  async function verifyPaths() {
    const res = await fetch(`${API}/api/v1/system/verify-paths`);
    setPathResults(await res.json());
  }

  async function createBackup() {
    await fetch(`${API}/api/v1/system/backup`, { method: 'POST' });
  }

  if (loading || !form) {
    return (
      <div className="flex items-center justify-center h-64">
        <p className="text-xs text-ctp-overlay0 animate-pulse">Loading settings...</p>
      </div>
    );
  }

  return (
    <div className="flex h-[calc(100vh-5rem)] -m-6">
      {/* Left nav */}
      <div className="w-52 shrink-0 border-r-2 border-ctp-surface0 bg-ctp-mantle/30 py-2">
        {SECTIONS.map(({ id, label, icon: Icon }) => (
          <button
            key={id}
            onClick={() => setActiveSection(id)}
            className={`w-full flex items-center gap-2.5 px-4 py-2 text-xs transition-colors ${
              activeSection === id
                ? 'bg-ctp-surface0 text-ctp-mauve border-l-[3px] border-ctp-mauve pl-[13px]'
                : 'text-ctp-subtext0 hover:bg-ctp-surface0/40 border-l-[3px] border-transparent pl-[13px]'
            }`}
          >
            <Icon size={14} />
            {label}
          </button>
        ))}
      </div>

      {/* Content */}
      <div className="flex-1 overflow-y-auto p-6">
        {/* Save bar */}
        {dirty && (
          <div className="mb-4 bg-ctp-surface0 border-2 border-ctp-yellow rpg-clip px-4 py-2 flex items-center justify-between">
            <span className="text-xs text-ctp-yellow">Unsaved changes</span>
            <div className="flex gap-2">
              <Button variant="secondary" size="sm" onClick={handleReset}>
                <RotateCcw size={12} /> Discard
              </Button>
              <Button variant="primary" size="sm" onClick={handleSave} disabled={saving}>
                <Save size={12} /> {saving ? 'Saving...' : 'Save'}
              </Button>
            </div>
          </div>
        )}

        {activeSection === 'general' && (
          <SectionGeneral form={form.general} onChange={(k, v) => updateField('general', k, v)} />
        )}
        {activeSection === 'agents' && (
          <SectionAgentDefaults form={form.agentDefaults} onChange={(k, v) => updateField('agentDefaults', k, v)} />
        )}
        {activeSection === 'paths' && (
          <SectionPaths paths={form.paths} results={pathResults} onVerify={verifyPaths} />
        )}
        {activeSection === 'notifications' && (
          <SectionNotifications form={form.notifications} onChange={(k, v) => updateField('notifications', k, v)} />
        )}
        {activeSection === 'backup' && (
          <SectionBackup onBackup={createBackup} />
        )}
        {activeSection === 'about' && <SectionAbout />}
      </div>
    </div>
  );
}

function SectionGeneral({ form, onChange }) {
  return (
    <div className="space-y-4 max-w-lg">
      <h3 className="font-pixel text-[11px] text-ctp-text mb-4">GENERAL</h3>
      <Field label="Theme">
        <select value={form.theme} disabled className="settings-select">
          <option>catppuccin-mocha</option>
        </select>
        <span className="text-[9px] text-ctp-overlay0 mt-1 block">More themes coming soon</span>
      </Field>
      <Field label="Language">
        <select value={form.language} onChange={(e) => onChange('language', e.target.value)} className="settings-select">
          <option value="en">English</option>
          <option value="ru">Russian</option>
        </select>
      </Field>
      <Field label="Refresh Rate (seconds)">
        <input
          type="number"
          min={5}
          max={120}
          value={form.refreshRate}
          onChange={(e) => onChange('refreshRate', parseInt(e.target.value) || 30)}
          className="settings-input w-24"
        />
      </Field>
    </div>
  );
}

function SectionAgentDefaults({ form, onChange }) {
  return (
    <div className="space-y-4 max-w-lg">
      <h3 className="font-pixel text-[11px] text-ctp-text mb-4">AGENT DEFAULTS</h3>
      <Field label="Default Model">
        <select value={form.model} onChange={(e) => onChange('model', e.target.value)} className="settings-select">
          <option value="claude-sonnet-4-6">Sonnet 4.6</option>
          <option value="claude-haiku-4-5">Haiku 4.5</option>
          <option value="claude-opus-4-6">Opus 4.6</option>
        </select>
      </Field>
      <Field label="Max Turns">
        <input type="number" min={5} max={100} value={form.maxTurns} onChange={(e) => onChange('maxTurns', parseInt(e.target.value) || 30)} className="settings-input w-24" />
      </Field>
      <Field label="Max Cost/Day ($)">
        <input type="number" min={0.5} max={50} step={0.5} value={form.maxCostPerDay} onChange={(e) => onChange('maxCostPerDay', parseFloat(e.target.value) || 5)} className="settings-input w-24" />
      </Field>
      <Toggle label="Auto Restart on crash" checked={form.autoRestart} onChange={(v) => onChange('autoRestart', v)} />
      <Toggle label="Retry on error" checked={form.retryOnError} onChange={(v) => onChange('retryOnError', v)} />
    </div>
  );
}

function SectionPaths({ paths, results, onVerify }) {
  return (
    <div className="space-y-4 max-w-xl">
      <div className="flex items-center justify-between mb-4">
        <h3 className="font-pixel text-[11px] text-ctp-text">PATHS</h3>
        <Button variant="secondary" size="sm" onClick={onVerify}>Verify All</Button>
      </div>
      {Object.entries(paths).map(([key, path]) => {
        const result = results?.[key];
        return (
          <div key={key} className="flex items-center gap-3 py-2 border-b border-ctp-surface0/50">
            <span className="text-xs text-ctp-subtext0 w-28 shrink-0">{key}</span>
            <span className="text-xs font-mono text-ctp-overlay1 flex-1 truncate">{path}</span>
            {result && (
              result.exists
                ? <CheckCircle size={14} className="text-ctp-green shrink-0" />
                : <XCircle size={14} className="text-ctp-red shrink-0" />
            )}
          </div>
        );
      })}
    </div>
  );
}

function SectionNotifications({ form, onChange }) {
  return (
    <div className="space-y-4 max-w-lg">
      <h3 className="font-pixel text-[11px] text-ctp-text mb-4">NOTIFICATIONS</h3>
      {Object.entries(form).map(([key, value]) => (
        <Toggle
          key={key}
          label={key.replace(/([A-Z])/g, ' $1').replace(/^./, (s) => s.toUpperCase())}
          checked={value}
          onChange={(v) => onChange(key, v)}
        />
      ))}
    </div>
  );
}

function SectionBackup({ onBackup }) {
  const [created, setCreated] = useState(false);
  return (
    <div className="space-y-4 max-w-lg">
      <h3 className="font-pixel text-[11px] text-ctp-text mb-4">BACKUP</h3>
      <Card>
        <div className="space-y-3">
          <p className="text-xs text-ctp-subtext0">Create a snapshot of the current system state.</p>
          <div className="flex gap-2">
            <Button variant="primary" size="sm" onClick={async () => { await onBackup(); setCreated(true); }}>
              <Database size={12} /> Create Now
            </Button>
            <Button variant="secondary" size="sm" disabled>
              <Download size={12} /> Download Latest
            </Button>
          </div>
          {created && <p className="text-[10px] text-ctp-green">Backup created successfully</p>}
        </div>
      </Card>
    </div>
  );
}

function SectionAbout() {
  return (
    <div className="space-y-4 max-w-lg">
      <h3 className="font-pixel text-[11px] text-ctp-text mb-4">ABOUT</h3>
      <Card>
        <div className="space-y-2">
          <div className="flex justify-between"><span className="text-xs text-ctp-subtext0">Version</span><span className="font-mono text-xs text-ctp-text">0.1.0</span></div>
          <div className="flex justify-between"><span className="text-xs text-ctp-subtext0">Frontend</span><span className="font-mono text-xs text-ctp-text">React 18 + Vite + Tailwind</span></div>
          <div className="flex justify-between"><span className="text-xs text-ctp-subtext0">Backend</span><span className="font-mono text-xs text-ctp-text">Express + SQLite + WebSocket</span></div>
          <div className="flex justify-between"><span className="text-xs text-ctp-subtext0">Theme</span><span className="font-mono text-xs text-ctp-mauve">Catppuccin Mocha</span></div>
          <div className="flex justify-between"><span className="text-xs text-ctp-subtext0">Agents</span><span className="font-mono text-xs text-ctp-text">12 configured</span></div>
          <div className="flex justify-between"><span className="text-xs text-ctp-subtext0">Style</span><span className="font-mono text-xs text-ctp-text">Pixel RPG + Modern UI</span></div>
        </div>
      </Card>
    </div>
  );
}

function Field({ label, children }) {
  return (
    <div>
      <label className="text-[10px] text-ctp-overlay0 block mb-1">{label}</label>
      {children}
    </div>
  );
}

function Toggle({ label, checked, onChange }) {
  return (
    <div className="flex items-center justify-between py-1">
      <span className="text-xs text-ctp-subtext0">{label}</span>
      <button
        onClick={() => onChange(!checked)}
        className={`w-10 h-5 border-2 flex items-center transition-colors ${
          checked ? 'bg-ctp-green/20 border-ctp-green' : 'bg-ctp-surface0 border-ctp-surface1'
        }`}
      >
        <div className={`w-3 h-3 transition-transform ${
          checked ? 'translate-x-5 bg-ctp-green' : 'translate-x-0.5 bg-ctp-overlay0'
        }`} />
      </button>
    </div>
  );
}
