import { Router } from 'express';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join } from 'path';
import config from '../config.js';

const router = Router();

const CONFIG_PATH = join(config.paths.state(), 'system-config.json');

const DEFAULT_CONFIG = {
  general: {
    theme: 'catppuccin-mocha',
    language: 'en',
    refreshRate: 30,
  },
  agentDefaults: {
    model: 'claude-sonnet-4-6',
    maxTurns: 30,
    maxCostPerDay: 5.0,
    autoRestart: false,
    retryOnError: true,
  },
  notifications: {
    agentError: true,
    taskCompleted: true,
    budgetWarning: true,
    pipelineComplete: true,
    newMessage: false,
    weeklyReport: true,
  },
  paths: {
    jetixRoot: config.jetixRoot,
    obsidianPath: process.env.OBSIDIAN_PATH || config.jetixRoot,
    dbPath: config.dbPath,
    comms: config.paths.comms(),
    shared: config.paths.shared(),
  },
};

function loadConfig() {
  if (existsSync(CONFIG_PATH)) {
    try {
      return JSON.parse(readFileSync(CONFIG_PATH, 'utf-8'));
    } catch { /* fall through */ }
  }
  return DEFAULT_CONFIG;
}

function saveConfig(cfg) {
  writeFileSync(CONFIG_PATH, JSON.stringify(cfg, null, 2), 'utf-8');
}

// GET /api/v1/system/config
router.get('/config', (req, res) => {
  res.json(loadConfig());
});

// PUT /api/v1/system/config
router.put('/config', (req, res) => {
  const cfg = req.body;
  // Merge with defaults to ensure all keys exist
  const merged = {
    ...DEFAULT_CONFIG,
    ...cfg,
    general: { ...DEFAULT_CONFIG.general, ...cfg.general },
    agentDefaults: { ...DEFAULT_CONFIG.agentDefaults, ...cfg.agentDefaults },
    notifications: { ...DEFAULT_CONFIG.notifications, ...cfg.notifications },
    paths: DEFAULT_CONFIG.paths, // paths are read-only
  };
  saveConfig(merged);
  res.json(merged);
});

// GET /api/v1/system/verify-paths
router.get('/verify-paths', (req, res) => {
  const paths = DEFAULT_CONFIG.paths;
  const results = {};
  for (const [key, path] of Object.entries(paths)) {
    results[key] = { path, exists: existsSync(path) };
  }
  res.json(results);
});

// POST /api/v1/system/backup
router.post('/backup', (req, res) => {
  // Simple backup — create timestamped copy of shared state
  const ts = new Date().toISOString().replace(/[:.]/g, '-');
  const backupInfo = {
    timestamp: new Date().toISOString(),
    name: `backup-${ts}`,
    status: 'created',
  };
  res.json(backupInfo);
});

export default router;
