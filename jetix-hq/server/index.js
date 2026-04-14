import { createServer } from 'http';
import express from 'express';
import cors from 'cors';
import config from './config.js';
import { initDb } from './db/init.js';
import { createWsServer } from './ws/index.js';
import agentsRouter from './routes/agents.js';
import projectsRouter from './routes/projects.js';
import metricsRouter from './routes/metrics.js';
import kanbanRouter from './routes/kanban.js';
import knowledgeRouter from './routes/knowledge.js';
import systemRouter from './routes/system.js';

const app = express();
const server = createServer(app);

app.use(cors({ origin: ['http://localhost:3000', 'http://localhost:3001'] }));
app.use(express.json());

// Health check
app.get('/api/v1/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// API routes
app.use('/api/v1/agents', agentsRouter);
app.use('/api/v1/projects', projectsRouter);
app.use('/api/v1/metrics', metricsRouter);
app.use('/api/v1/kanban', kanbanRouter);
app.use('/api/v1/knowledge', knowledgeRouter);
app.use('/api/v1/system', systemRouter);

// Init DB
const db = initDb(config.dbPath);

// Attach WebSocket server
const { wss, broadcast } = createWsServer(server);

// Start
server.listen(config.port, '0.0.0.0', () => {
  console.log(`Jetix HQ server running on port ${config.port}`);
});
