import express from 'express';
import cors from 'cors';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';

import projectsRoute from './routes/projects.js';
import decisionsRoute from './routes/decisions.js';
import agentsRoute from './routes/agents.js';
import stateRoute from './routes/state.js';
import kanbanRoute from './routes/kanban.js';
import observabilityRoute from './routes/observability.js';
import chatRoute from './routes/chat.js';
import coordinationRoute from './routes/coordination.js';
import focusRoute from './routes/focus.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const JETIX_ROOT = process.env.JETIX_ROOT
  ? path.resolve(process.env.JETIX_ROOT.replace(/^~/, os.homedir()))
  : path.resolve(__dirname, '..', '..');
const PORT = Number(process.env.PORT || 3001);

const app = express();
app.use(cors({ origin: '*' }));
app.use((_req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  next();
});
app.use(express.json());

app.get('/api/v1/health', (_req, res) => {
  res.json({ status: 'ok', jetix_root: JETIX_ROOT, timestamp: new Date().toISOString() });
});

app.use('/api/v1/projects', projectsRoute(JETIX_ROOT));
app.use('/api/v1/decisions', decisionsRoute(JETIX_ROOT));
app.use('/api/v1/agents', agentsRoute(JETIX_ROOT));
app.use('/api/v1/state', stateRoute(JETIX_ROOT));
app.use('/api/v1/kanban', kanbanRoute(JETIX_ROOT));
app.use('/api/v1/observability', observabilityRoute());
app.use('/api/v1/chat', chatRoute(JETIX_ROOT));
app.use('/api/v1/coordination', coordinationRoute(JETIX_ROOT));
app.use('/api/v1/focus', focusRoute(JETIX_ROOT));

app.listen(PORT, '0.0.0.0', () => {
  console.log(`[jetix-dashboard-server] :${PORT} JETIX_ROOT=${JETIX_ROOT}`);
});
