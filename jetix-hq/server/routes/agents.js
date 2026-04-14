import { Router } from 'express';

const router = Router();

router.get('/', (req, res) => {
  res.json({ agents: [], message: 'stub' });
});

router.get('/:name', (req, res) => {
  res.json({ agent: req.params.name, message: 'stub' });
});

export default router;
