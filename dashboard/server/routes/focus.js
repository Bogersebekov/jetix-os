import { Router } from 'express';
import fs from 'node:fs/promises';
import path from 'node:path';

export default function focusRoute(JETIX_ROOT) {
  const router = Router();

  router.get('/', async (_req, res) => {
    try {
      const raw = await fs.readFile(path.join(JETIX_ROOT, 'shared/state/focus.json'), 'utf-8');
      res.json(JSON.parse(raw));
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  return router;
}
