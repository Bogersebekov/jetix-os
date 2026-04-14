import { Router } from 'express';
import { randomUUID } from 'crypto';
import Database from 'better-sqlite3';

const router = Router();

const VIEW_COLUMNS = {
  projects: [
    { id: 'backlog', label: 'Backlog', color: '#6c7086', wipLimit: 0 },
    { id: 'todo', label: 'To Do', color: '#89b4fa', wipLimit: 8 },
    { id: 'in_progress', label: 'In Progress', color: '#cba6f7', wipLimit: 5 },
    { id: 'review', label: 'Review', color: '#f9e2af', wipLimit: 3 },
    { id: 'done', label: 'Done', color: '#a6e3a1', wipLimit: 0 },
  ],
  agents: [
    { id: 'queued', label: 'Queued', color: '#6c7086', wipLimit: 0 },
    { id: 'assigned', label: 'Assigned', color: '#89b4fa', wipLimit: 0 },
    { id: 'running', label: 'Running', color: '#cba6f7', wipLimit: 6 },
    { id: 'completed', label: 'Completed', color: '#a6e3a1', wipLimit: 0 },
    { id: 'failed', label: 'Failed', color: '#f38ba8', wipLimit: 0 },
  ],
  personal: [
    { id: 'inbox', label: 'Inbox', color: '#6c7086', wipLimit: 0 },
    { id: 'today', label: 'Today', color: '#f38ba8', wipLimit: 5 },
    { id: 'this_week', label: 'This Week', color: '#fab387', wipLimit: 10 },
    { id: 'waiting', label: 'Waiting', color: '#f9e2af', wipLimit: 0 },
    { id: 'done', label: 'Done', color: '#a6e3a1', wipLimit: 0 },
  ],
};

function openDb() {
  return new Database(process.env.DB_PATH || './data/jetix-hq.db');
}

function seedIfEmpty(db, view) {
  const count = db.prepare('SELECT COUNT(*) as n FROM kanban_cards WHERE view = ?').get(view);
  if (count.n > 0) return;

  const seeds = {
    projects: [
      { column_id: 'todo', title: 'Design ICP v2 persona', priority: 'high', project: 'quick-money', assignee: 'sales-lead', tags: '["sales","icp"]' },
      { column_id: 'todo', title: 'Research Berlin AI meetups', priority: 'medium', project: 'quick-money', assignee: 'sales-researcher', tags: '["research"]' },
      { column_id: 'in_progress', title: 'Build outreach sequence for coaches', priority: 'high', project: 'quick-money', assignee: 'sales-outreach', tags: '["outreach"]' },
      { column_id: 'backlog', title: 'Set up Notion CRM integration', priority: 'low', project: 'quick-money', tags: '["infra"]' },
      { column_id: 'backlog', title: 'Write case study template', priority: 'medium', project: 'brand', tags: '["content"]' },
      { column_id: 'review', title: 'LinkedIn profile optimization', priority: 'medium', project: 'brand', assignee: 'sales-outreach', tags: '["brand"]' },
    ],
    agents: [
      { column_id: 'queued', title: 'Weekly prospect research batch', priority: 'high', assignee: 'sales-researcher', tags: '["automated"]' },
      { column_id: 'assigned', title: 'Process voice memos from inbox/', priority: 'medium', assignee: 'inbox-processor', tags: '["inbox"]' },
      { column_id: 'running', title: 'Morning pipeline execution', priority: 'high', assignee: 'manager', tags: '["pipeline"]' },
      { column_id: 'completed', title: 'System health check', priority: 'low', assignee: 'system-admin', tags: '["ops"]' },
    ],
    personal: [
      { column_id: 'today', title: 'Review Crazy Agent ideas', priority: 'medium', tags: '["review"]' },
      { column_id: 'today', title: 'Call with potential partner', priority: 'high', tags: '["sales","call"]', due_date: '2026-04-14' },
      { column_id: 'this_week', title: 'Record Jetix demo video', priority: 'medium', tags: '["content"]' },
      { column_id: 'inbox', title: 'Idea: AI audit productized service', priority: 'low', tags: '["idea"]' },
      { column_id: 'waiting', title: 'Waiting for Anton feedback on pricing', priority: 'medium', tags: '["mentor"]' },
    ],
  };

  const insert = db.prepare(`
    INSERT INTO kanban_cards (id, view, column_id, title, priority, project, assignee, due_date, tags, position)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);

  const cards = seeds[view] || [];
  cards.forEach((c, i) => {
    insert.run(
      `card-${view}-${randomUUID().slice(0, 8)}`,
      view, c.column_id, c.title, c.priority || 'medium',
      c.project || null, c.assignee || null, c.due_date || null,
      c.tags || '[]', i * 1000
    );
  });
}

function parseCard(c) {
  return {
    ...c,
    tags: JSON.parse(c.tags || '[]'),
    subtasks: JSON.parse(c.subtasks || '[]'),
    comments: JSON.parse(c.comments || '[]'),
  };
}

// GET /api/v1/kanban?view=projects|agents|personal
router.get('/', (req, res) => {
  const view = req.query.view || 'projects';
  const columns = VIEW_COLUMNS[view];
  if (!columns) return res.status(400).json({ error: 'Invalid view' });

  const db = openDb();
  seedIfEmpty(db, view);

  const cards = db.prepare(
    'SELECT * FROM kanban_cards WHERE view = ? ORDER BY position ASC'
  ).all(view).map(parseCard);

  const columnData = columns.map((col) => ({
    ...col,
    cards: cards.filter((c) => c.column_id === col.id),
  }));

  db.close();
  res.json({ view, columns: columnData });
});

// POST /api/v1/kanban/cards
router.post('/cards', (req, res) => {
  const { view, column_id, title, priority, assignee, project, due_date, tags } = req.body;
  if (!title || !column_id) return res.status(400).json({ error: 'title and column_id required' });

  const db = openDb();
  const maxPos = db.prepare(
    'SELECT MAX(position) as m FROM kanban_cards WHERE view = ? AND column_id = ?'
  ).get(view || 'projects', column_id);

  const id = `card-${randomUUID().slice(0, 8)}`;
  db.prepare(`
    INSERT INTO kanban_cards (id, view, column_id, title, priority, assignee, project, due_date, tags, position)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).run(id, view || 'projects', column_id, title,
    priority || 'medium', assignee || null, project || null, due_date || null,
    JSON.stringify(tags || []), (maxPos?.m || 0) + 1000
  );

  const card = db.prepare('SELECT * FROM kanban_cards WHERE id = ?').get(id);
  db.close();
  res.json(parseCard(card));
});

// PATCH /api/v1/kanban/cards/:id
router.patch('/cards/:id', (req, res) => {
  const { title, description, priority, assignee, project, due_date, tags, subtasks, comments, column_id, position } = req.body;

  const db = openDb();
  const existing = db.prepare('SELECT * FROM kanban_cards WHERE id = ?').get(req.params.id);
  if (!existing) { db.close(); return res.status(404).json({ error: 'Card not found' }); }

  db.prepare(`
    UPDATE kanban_cards SET
      title = ?, description = ?, priority = ?, assignee = ?, project = ?,
      due_date = ?, tags = ?, subtasks = ?, comments = ?, column_id = ?,
      position = ?, updated_at = datetime('now')
    WHERE id = ?
  `).run(
    title ?? existing.title,
    description ?? existing.description,
    priority ?? existing.priority,
    assignee !== undefined ? assignee : existing.assignee,
    project !== undefined ? project : existing.project,
    due_date !== undefined ? due_date : existing.due_date,
    tags ? JSON.stringify(tags) : existing.tags,
    subtasks ? JSON.stringify(subtasks) : existing.subtasks,
    comments ? JSON.stringify(comments) : existing.comments,
    column_id ?? existing.column_id,
    position ?? existing.position,
    req.params.id
  );

  const updated = db.prepare('SELECT * FROM kanban_cards WHERE id = ?').get(req.params.id);
  db.close();
  res.json(parseCard(updated));
});

// POST /api/v1/kanban/cards/reorder
router.post('/cards/reorder', (req, res) => {
  const { updates } = req.body;
  if (!Array.isArray(updates)) return res.status(400).json({ error: 'updates array required' });

  const db = openDb();
  const stmt = db.prepare("UPDATE kanban_cards SET column_id = ?, position = ?, updated_at = datetime('now') WHERE id = ?");
  const tx = db.transaction((items) => {
    for (const { id, column_id, position } of items) {
      stmt.run(column_id, position, id);
    }
  });
  tx(updates);
  db.close();
  res.json({ ok: true, updated: updates.length });
});

// DELETE /api/v1/kanban/cards/:id
router.delete('/cards/:id', (req, res) => {
  const db = openDb();
  db.prepare('DELETE FROM kanban_cards WHERE id = ?').run(req.params.id);
  db.close();
  res.json({ ok: true });
});

export default router;
