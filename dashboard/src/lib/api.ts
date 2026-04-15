export const API_URL = import.meta.env.VITE_API_URL || ''

async function j<T>(path: string): Promise<T> {
  const res = await fetch(`${API_URL}${path}`)
  if (!res.ok) throw new Error(`${path} → ${res.status}`)
  return res.json() as Promise<T>
}

async function jput<T, B>(path: string, body: B): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
  if (!res.ok) throw new Error(`${path} → ${res.status}`)
  return res.json() as Promise<T>
}

export type KanbanCard = {
  id: string
  title: string
  description?: string
  priority: number
  assignee?: string
}

export type KanbanColumn = {
  id: string
  title: string
  cards: KanbanCard[]
}

export type KanbanState = { columns: KanbanColumn[] }

export type Project = {
  name: string
  status: string
  priority: number
  description: string
  current_phase: string
  keywords: string[]
}

export type Agent = {
  id: string
  name?: string
  model?: string | null
  department?: string | null
  function?: string | null
  status?: string | null
  last_message?: Record<string, unknown> | null
}

export type DecisionsPayload = {
  updated_at?: string
  decisions: string[]
}

export type MailboxMessage = {
  id: string
  timestamp?: string
  from?: string
  to?: string
  type?: string
  priority?: string
  subject?: string
  body?: string
  status?: string
}

export type MailboxPayload = {
  agent: string
  total: number
  messages: MailboxMessage[]
}

export const api = {
  projects: () => j<{ updated_at?: string; projects: Project[] }>('/api/projects'),
  decisions: () => j<DecisionsPayload>('/api/decisions'),
  agents: () => j<{ agents: Agent[] }>('/api/agents'),
  mailbox: (name: string) => j<MailboxPayload>(`/api/agents/${encodeURIComponent(name)}/mailbox`),
  kanban: () => j<KanbanState>('/api/kanban'),
  saveKanban: (state: KanbanState) => jput<{ ok: boolean }, KanbanState>('/api/kanban', state),
  health: () => j<{ status: string; jetix_root: string }>('/api/health'),
}
