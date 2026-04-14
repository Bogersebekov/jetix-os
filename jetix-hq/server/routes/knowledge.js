import { Router } from 'express';

const router = Router();

router.get('/', (req, res) => {
  res.json({ items: [], message: 'stub' });
});

export default router;
