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

export type CoordinationActivity = {
  timestamp: string
  from: string
  to: string
  subject: string
}

export type CoordinationData = {
  departments: { name: string; agents: string[]; active: number }[]
  agents: Agent[]
  recent_activity: CoordinationActivity[]
}

export type ChatAgent = {
  name: string
  department: string
  unread: number
  total: number
}

export type ObservabilityData = {
  summary: {
    total_tokens: number
    total_cost: number
    total_sessions: number
    avg_tokens_per_session: number
  }
  daily: { date: string; tokens: number; cost: number; sessions: number }[]
  by_agent: { agent: string; tokens: number; cost: number }[]
}

export type FocusData = {
  global_goal: string
  week_focus: {
    week: string
    items: string[]
  }
  day_focus: {
    date: string
    items: string[]
  }
}

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
  focus: () => j<FocusData>('/api/v1/focus'),
  projects: () => j<{ updated_at?: string; projects: Project[] }>('/api/v1/projects'),
  decisions: () => j<DecisionsPayload>('/api/v1/decisions'),
  agents: () => j<{ agents: Agent[] }>('/api/v1/agents'),
  mailbox: (name: string) => j<MailboxPayload>(`/api/v1/agents/${encodeURIComponent(name)}/mailbox`),
  kanban: () => j<KanbanState>('/api/v1/kanban'),
  observability: () => j<ObservabilityData>('/api/v1/observability'),
  coordination: () => j<CoordinationData>('/api/v1/coordination'),
  chatAgents: () => j<{ agents: ChatAgent[] }>('/api/v1/chat/agents'),
  chatMailbox: (name: string) =>
    j<MailboxPayload>(`/api/v1/chat/mailbox/${encodeURIComponent(name)}`),
  chatHuman: () => j<MailboxPayload>('/api/v1/chat/human'),
  chatSend: (payload: { to: string; from?: string; subject?: string; content: string }) =>
    fetch(`${API_URL}/api/v1/chat/send`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    }).then((r) => {
      if (!r.ok) throw new Error(`send → ${r.status}`)
      return r.json() as Promise<{ ok: boolean; message: MailboxMessage }>
    }),
  saveKanban: (state: KanbanState) => jput<{ ok: boolean }, KanbanState>('/api/v1/kanban', state),
  health: () => j<{ status: string; jetix_root: string }>('/api/v1/health'),
}
