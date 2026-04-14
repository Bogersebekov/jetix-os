# Jetix HQ Dashboard

Gamified web dashboard for managing the Jetix OS multi-agent system.
Pixel-art RPG aesthetic + Catppuccin Mocha dark theme.

## Screens

| Screen | Description |
|--------|-------------|
| **HQ** | Virtual office with 8 rooms, agent avatars, projects, activity feed |
| **Agents** | Split view: agent list + detail with mailbox, metrics, queue, config |
| **Dashboard** | Resources + Observability analytics with 8+ chart types |
| **Kanban** | 3-view task board with drag-and-drop (Projects, Agent Tasks, Personal) |
| **Knowledge** | File tree + markdown preview + graph view + search |
| **Settings** | System config, agent defaults, paths, notifications, backup |

## Tech Stack

- **Frontend:** React 18, Vite, Tailwind CSS 3, Recharts, React Flow, @dnd-kit
- **Backend:** Express.js, better-sqlite3, ws (WebSocket), chokidar (file watcher)
- **Theme:** Catppuccin Mocha
- **Fonts:** Press Start 2P (pixel), Inter (UI), JetBrains Mono (code)

## Quick Start (Development)

```bash
# Install dependencies
cd client && npm install && cd ..
cd server && npm install && cd ..

# Start backend (terminal 1)
cd server
JETIX_ROOT=/path/to/jetix-os DB_PATH=./data/jetix-hq.db node index.js

# Start frontend (terminal 2)
cd client
npm run dev
```

Open http://localhost:3000

## Docker (Development)

```bash
docker compose up
```

## Docker (Production)

```bash
JETIX_ROOT=/path/to/jetix-os docker compose -f docker-compose.prod.yml up -d
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `3001` | Backend port |
| `JETIX_ROOT` | `../` | Path to jetix-os root |
| `OBSIDIAN_PATH` | same as JETIX_ROOT | Path to Obsidian vault |
| `DB_PATH` | `./data/jetix-hq.db` | SQLite database path |

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/v1/health` | Health check |
| `GET /api/v1/agents` | List all agents |
| `GET /api/v1/agents/:id` | Agent detail + mailbox + config |
| `GET /api/v1/metrics?period=` | Dashboard metrics (today/week/month) |
| `GET /api/v1/kanban?view=` | Kanban board (projects/agents/personal) |
| `POST/PATCH/DELETE /api/v1/kanban/cards` | Card CRUD |
| `GET /api/v1/knowledge/tree` | File tree |
| `GET /api/v1/knowledge/file?path=` | File content + metadata |
| `GET /api/v1/knowledge/search?q=` | Full-text search |
| `GET /api/v1/knowledge/graph` | Note graph (nodes + edges) |
| `GET/PUT /api/v1/system/config` | System configuration |
| `WS /ws` | WebSocket real-time updates |
