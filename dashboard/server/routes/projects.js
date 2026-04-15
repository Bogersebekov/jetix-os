import { Router } from 'express';
import fs from 'node:fs/promises';
import path from 'node:path';

export default function projectsRoute(JETIX_ROOT) {
  const router = Router();

  router.get('/', async (_req, res) => {
    try {
      const raw = await fs.readFile(path.join(JETIX_ROOT, 'config/projects.json'), 'utf-8');
      const data = JSON.parse(raw);
      const projects = (data.projects || []).map((p) => ({
        name: p.name,
        status: p.status,
        priority: p.priority,
        description: p.description,
        current_phase: p.current_phase,
        keywords: p.keywords || [],
      }));
      res.json({ updated_at: data.updated_at, projects });
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  return router;
}
