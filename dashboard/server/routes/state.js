import { Router } from 'express';
import fs from 'node:fs/promises';
import path from 'node:path';

export default function stateRoute(JETIX_ROOT) {
  const router = Router();

  router.get('/:filename', async (req, res) => {
    const name = req.params.filename.replace(/[^a-zA-Z0-9._-]/g, '');
    const full = path.join(JETIX_ROOT, 'shared/state', name.endsWith('.json') ? name : `${name}.json`);
    try {
      const raw = await fs.readFile(full, 'utf-8');
      res.json(JSON.parse(raw));
    } catch (e) {
      if (e.code === 'ENOENT') return res.status(404).json({ error: 'not found', file: full });
      res.status(500).json({ error: e.message });
    }
  });

  return router;
}
