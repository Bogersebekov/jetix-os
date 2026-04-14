import { Router } from 'express';

const router = Router();

router.get('/', (req, res) => {
  res.json({ projects: [], message: 'stub' });
});

export default router;
