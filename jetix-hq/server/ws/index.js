import { WebSocketServer } from 'ws';
import chokidar from 'chokidar';
import { existsSync, readFileSync } from 'fs';
import { join, basename } from 'path';
import config from '../config.js';

const HEARTBEAT_INTERVAL = 30000;
const DEBOUNCE_MS = 500;

export function createWsServer(httpServer) {
  const wss = new WebSocketServer({ server: httpServer, path: '/ws' });

  // Track client subscriptions
  const clients = new Set();

  wss.on('connection', (ws) => {
    const client = { ws, channels: new Set(), alive: true };
    clients.add(client);
    console.log(`[ws] client connected (total: ${clients.size})`);

    ws.on('message', (raw) => {
      try {
        const msg = JSON.parse(raw);
        handleClientMessage(client, msg);
      } catch {
        ws.send(JSON.stringify({ type: 'error', message: 'Invalid JSON' }));
      }
    });

    ws.on('pong', () => {
      client.alive = true;
    });

    ws.on('close', () => {
      clients.delete(client);
      console.log(`[ws] client disconnected (total: ${clients.size})`);
    });

    // Send welcome
    ws.send(JSON.stringify({
      type: 'connected',
      channels: ['agents', 'kanban', 'resources', 'company', 'comms'],
    }));
  });

  // Heartbeat
  const heartbeat = setInterval(() => {
    for (const client of clients) {
      if (!client.alive) {
        client.ws.terminate();
        clients.delete(client);
        continue;
      }
      client.alive = false;
      client.ws.ping();
    }
  }, HEARTBEAT_INTERVAL);

  wss.on('close', () => clearInterval(heartbeat));

  // Handle client messages
  function handleClientMessage(client, msg) {
    switch (msg.type) {
      case 'subscribe': {
        const channels = Array.isArray(msg.channels) ? msg.channels : [];
        for (const ch of channels) client.channels.add(ch);
        client.ws.send(JSON.stringify({ type: 'subscribed', channels: [...client.channels] }));
        break;
      }
      case 'agent:command':
        // Placeholder — log and broadcast acknowledgment
        console.log(`[ws] agent command: ${msg.agent} ${msg.command}`);
        broadcast('agents', { type: 'agent:command:ack', agent: msg.agent, command: msg.command });
        break;
      case 'refresh':
        // Client requested full refresh — send current state
        broadcastTo(client, { type: 'refresh:ack' });
        break;
    }
  }

  // Broadcast to subscribed clients
  function broadcast(channel, payload) {
    const msg = JSON.stringify(payload);
    for (const client of clients) {
      if (client.channels.has(channel) && client.ws.readyState === 1) {
        client.ws.send(msg);
      }
    }
  }

  function broadcastTo(client, payload) {
    if (client.ws.readyState === 1) {
      client.ws.send(JSON.stringify(payload));
    }
  }

  // --- File Watcher ---
  const debounceTimers = new Map();
  function debounced(key, fn) {
    if (debounceTimers.has(key)) clearTimeout(debounceTimers.get(key));
    debounceTimers.set(key, setTimeout(() => {
      debounceTimers.delete(key);
      fn();
    }, DEBOUNCE_MS));
  }

  const watchers = [];

  // Watch shared/state/
  const statePath = config.paths.state();
  if (existsSync(statePath)) {
    const stateWatcher = chokidar.watch(statePath, {
      ignoreInitial: true,
      depth: 2,
      usePolling: true,
      interval: 500,
    });

    stateWatcher.on('change', (filePath) => {
      const file = basename(filePath);
      debounced(`state:${file}`, () => {
        console.log(`[watch] state changed: ${file}`);

        if (file.includes('agent') || file === 'system-health.json') {
          broadcast('agents', { type: 'agent:status', file, ts: Date.now() });
        }
        if (file.includes('priorities') || file.includes('active-projects')) {
          broadcast('resources', { type: 'resources:updated', file, ts: Date.now() });
        }
        if (file.includes('metrics') || file.includes('performance')) {
          broadcast('resources', { type: 'resources:updated', file, ts: Date.now() });
        }
      });
    });
    watchers.push(stateWatcher);
  }

  // Watch comms/mailboxes/
  const mailboxPath = config.paths.mailboxes();
  if (existsSync(mailboxPath)) {
    const commsWatcher = chokidar.watch(mailboxPath, {
      ignoreInitial: true,
      usePolling: true,
      interval: 300,
    });

    commsWatcher.on('change', (filePath) => {
      if (!filePath.endsWith('.jsonl')) return;
      const file = basename(filePath, '.jsonl');
      debounced(`comms:${file}`, () => {
        console.log(`[watch] mailbox changed: ${file}`);
        // Read last line
        try {
          const content = readFileSync(filePath, 'utf-8').trim();
          const lines = content.split('\n');
          const lastMsg = lines.length > 0 ? JSON.parse(lines[lines.length - 1]) : null;
          broadcast('comms', {
            type: 'comms:message',
            mailbox: file,
            message: lastMsg,
            ts: Date.now(),
          });
          // Also notify agents channel for unread count updates
          broadcast('agents', { type: 'agent:status', file: `${file}.jsonl`, ts: Date.now() });
        } catch {
          broadcast('comms', { type: 'comms:message', mailbox: file, ts: Date.now() });
        }
      });
    });
    watchers.push(commsWatcher);
  }

  console.log(`[ws] WebSocket server ready on /ws`);
  console.log(`[ws] Watching: ${statePath}, ${mailboxPath}`);

  return { wss, broadcast };
}
