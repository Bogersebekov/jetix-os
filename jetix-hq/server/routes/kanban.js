import { Router } from 'express';

const router = Router();

router.get('/', (req, res) => {
  res.json({ columns: [], message: 'stub' });
});

export default router;
