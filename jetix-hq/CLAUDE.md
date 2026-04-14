# Jetix HQ Dashboard

Gamified web dashboard for managing AI agents in the Jetix OS multi-agent system.
Visual style: pixel-art Stardew Valley aesthetic + Catppuccin Mocha dark theme.

## Tech Stack

### Frontend (`client/`, port 3000)
- React 18 + Vite
- Tailwind CSS 3 (Catppuccin Mocha palette)
- Recharts (metrics & XP bars)
- React Flow (agent graph)
- React Router v6
- Zustand (state management)
- lucide-react (icons)

### Backend (`server/`, port 3001)
- Express.js
- better-sqlite3 (local DB)
- chokidar (file watcher for shared/ state)
- ws (WebSocket for real-time updates)

## API
- Base URL: `http://localhost:3001/api/v1`
- Health check: `GET /api/v1/health`
- All file paths configured via environment variables with mock data fallback

## Architecture
- Docker Compose: two services (client, server), hot reload in both
- SQLite files stored in `data/` (Docker volume)
- Backend reads Jetix OS shared state from `JETIX_ROOT` env var
- Frontend proxied to backend in dev mode

## Conventions
- Functional React components with hooks only
- CSS variables for Catppuccin colors in `globals.css`
- Tailwind extended with Catppuccin palette
- API routes namespaced under `/api/v1/`
