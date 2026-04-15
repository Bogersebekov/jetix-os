import { Router } from 'express';
import fs from 'node:fs/promises';
import path from 'node:path';

const DEFAULT_STATE = {
  columns: [
    {
      id: 'backlog',
      title: 'Backlog',
      cards: [
        { id: 'c-1', title: 'Ревью 380 заметок', description: 'Разобрать накопленные голосовые заметки', priority: 1, assignee: 'inbox-processor' },
        { id: 'c-2', title: 'Настроить Miro-борд', description: 'Визуализация архитектуры Jetix OS', priority: 2, assignee: 'system-admin' },
      ],
    },
    {
      id: 'todo',
      title: 'To Do',
      cards: [
        { id: 'c-3', title: 'Описать ICP для клиентов', description: 'Идеальный профиль клиента для AI-услуг', priority: 1, assignee: 'sales-lead' },
        { id: 'c-4', title: 'Создать веб-сайт', description: 'Лендинг под quick-money проект', priority: 2, assignee: 'brand' },
      ],
    },
    {
      id: 'in-progress',
      title: 'In Progress',
      cards: [
        { id: 'c-5', title: 'Внедрение дашборда', description: 'Command Center + Agents + Kanban', priority: 1, assignee: 'system-admin' },
      ],
    },
    { id: 'review', title: 'Review', cards: [] },
    { id: 'done', title: 'Done', cards: [] },
  ],
};

export default function kanbanRoute(JETIX_ROOT) {
  const router = Router();
  const filePath = path.join(JETIX_ROOT, 'shared/state/kanban.json');

  async function readState() {
    try {
      const raw = await fs.readFile(filePath, 'utf-8');
      return JSON.parse(raw);
    } catch (e) {
      if (e.code === 'ENOENT') {
        await fs.mkdir(path.dirname(filePath), { recursive: true });
        await fs.writeFile(filePath, JSON.stringify(DEFAULT_STATE, null, 2), 'utf-8');
        return DEFAULT_STATE;
      }
      throw e;
    }
  }

  router.get('/', async (_req, res) => {
    try {
      res.json(await readState());
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  router.put('/', async (req, res) => {
    try {
      const body = req.body;
      if (!body || !Array.isArray(body.columns)) {
        return res.status(400).json({ error: 'Invalid body: expected { columns: [...] }' });
      }
      await fs.mkdir(path.dirname(filePath), { recursive: true });
      await fs.writeFile(filePath, JSON.stringify(body, null, 2), 'utf-8');
      res.json({ ok: true });
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  });

  return router;
}
