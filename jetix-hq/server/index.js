import express from 'express';
import cors from 'cors';
import config from './config.js';
import { initDb } from './db/init.js';
import agentsRouter from './routes/agents.js';
import projectsRouter from './routes/projects.js';
import metricsRouter from './routes/metrics.js';
import kanbanRouter from './routes/kanban.js';
import knowledgeRouter from './routes/knowledge.js';

const app = express();

app.use(cors({ origin: 'http://localhost:3000' }));
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

// Init DB and start
const db = initDb(config.dbPath);

app.listen(config.port, '0.0.0.0', () => {
  console.log(`Jetix HQ server running on port ${config.port}`);
});
