export const API_URL = import.meta.env.VITE_API_URL || ''

async function j<T>(path: string): Promise<T> {
  const res = await fetch(`${API_URL}${path}`)
  if (!res.ok) throw new Error(`${path} → ${res.status}`)
  return res.json() as Promise<T>
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

export const api = {
  projects: () => j<{ updated_at?: string; projects: Project[] }>('/api/projects'),
  decisions: () => j<DecisionsPayload>('/api/decisions'),
  agents: () => j<{ agents: Agent[] }>('/api/agents'),
  health: () => j<{ status: string; jetix_root: string }>('/api/health'),
}
