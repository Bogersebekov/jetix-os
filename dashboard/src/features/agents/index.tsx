import { useMemo, useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { ProfileDropdown } from '@/components/profile-dropdown'
import { Search } from '@/components/search'
import { ThemeSwitch } from '@/components/theme-switch'
import { ConfigDrawer } from '@/components/config-drawer'
import { Badge } from '@/components/ui/badge'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Separator } from '@/components/ui/separator'
import { api, type Agent } from '@/lib/api'

const ROSTER: Record<string, { department: string; fn: string }> = {
  manager: { department: 'MGMT', fn: 'Coordination hub' },
  strategist: { department: 'MGMT', fn: 'Strategic decisions' },
  'personal-assistant': { department: 'OPS', fn: 'Productivity, OPS lead' },
  'system-admin': { department: 'OPS', fn: 'Infrastructure' },
  'sales-lead': { department: 'Sales', fn: 'Sales coordination' },
  'sales-researcher': { department: 'Sales', fn: 'Prospect research' },
  'sales-outreach': { department: 'Sales', fn: 'Outreach & community' },
  'sales-team': { department: 'Sales', fn: 'Sales team workspace' },
  'inbox-processor': { department: 'Brain', fn: 'Information triage' },
  'knowledge-synth': { department: 'Brain', fn: 'Deep synthesis, Brain lead' },
  'research-team': { department: 'Brain', fn: 'Research workspace' },
  'content-team': { department: 'Brain', fn: 'Content workspace' },
  'crazy-agent': { department: 'Meta', fn: 'Creative disruption' },
  'meta-agent': { department: 'Meta', fn: 'System auditing' },
  'life-coach': { department: 'Life', fn: 'Wellness optimization' },
}

const DEPT_ORDER = ['MGMT', 'OPS', 'Sales', 'Brain', 'Meta', 'Life', 'Other']

function modelShort(model?: string | null): string {
  if (!model) return '—'
  if (model.includes('opus')) return 'Opus'
  if (model.includes('sonnet')) return 'Sonnet'
  if (model.includes('haiku')) return 'Haiku'
  return model
}

function statusOf(a: Agent): 'idle' | 'working' | 'error' {
  const s = (a.status || '').toLowerCase()
  if (s === 'working' || s === 'busy' || s === 'active') return 'working'
  if (s === 'error' || s === 'failed') return 'error'
  return 'idle'
}

function StatusBadge({ status }: { status: 'idle' | 'working' | 'error' }) {
  const styles = {
    idle: 'bg-gray-500/20 text-gray-400',
    working: 'bg-green-500/20 text-green-400',
    error: 'bg-red-500/20 text-red-400',
  }[status]
  return <span className={`px-2 py-0.5 rounded text-xs ${styles}`}>{status}</span>
}

function deptOf(a: Agent): string {
  return a.department || ROSTER[a.id]?.department || 'Other'
}

function fnOf(a: Agent): string {
  return a.function || ROSTER[a.id]?.fn || '—'
}

function Mailbox({ name }: { name: string }) {
  const q = useQuery({
    queryKey: ['mailbox', name],
    queryFn: () => api.mailbox(name),
  })

  if (q.isLoading) return <p className='text-muted-foreground text-sm'>Загрузка…</p>
  if (q.isError) return <p className='text-red-400 text-sm'>Ошибка загрузки</p>
  const messages = q.data?.messages ?? []
  if (messages.length === 0) return <p className='text-muted-foreground text-sm'>Нет сообщений</p>

  return (
    <ScrollArea className='h-[420px] pr-3'>
      <div className='flex flex-col gap-2'>
        {messages.slice(0, 10).map((m) => (
          <div key={m.id} className='rounded-lg border p-3'>
            <div className='flex items-center justify-between text-xs text-muted-foreground'>
              <span>от {m.from || '—'}</span>
              <span>{m.timestamp ? new Date(m.timestamp).toLocaleString() : ''}</span>
            </div>
            <div className='mt-1 font-medium text-sm'>{m.subject || m.type || '(без темы)'}</div>
            {m.body && <div className='mt-1 text-sm text-muted-foreground'>{m.body}</div>}
          </div>
        ))}
      </div>
    </ScrollArea>
  )
}

export function Agents() {
  const q = useQuery({ queryKey: ['agents'], queryFn: api.agents })
  const agents = q.data?.agents ?? []
  const [selected, setSelected] = useState<string | null>(null)

  const grouped = useMemo(() => {
    const g = new Map<string, Agent[]>()
    for (const a of agents) {
      const d = deptOf(a)
      if (!g.has(d)) g.set(d, [])
      g.get(d)!.push(a)
    }
    return DEPT_ORDER.filter((d) => g.has(d)).map((d) => ({
      dept: d,
      list: g.get(d)!.sort((a, b) => a.id.localeCompare(b.id)),
    }))
  }, [agents])

  const current = agents.find((a) => a.id === selected) || agents[0]

  return (
    <>
      <Header fixed>
        <Search />
        <div className='ms-auto flex items-center space-x-4'>
          <ThemeSwitch />
          <ConfigDrawer />
          <ProfileDropdown />
        </div>
      </Header>

      <Main>
        <div className='mb-4'>
          <h1 className='text-2xl font-bold tracking-tight'>Agents</h1>
          <p className='text-muted-foreground text-sm'>
            {agents.length} агентов · данные из /api/agents
          </p>
        </div>

        <div className='flex gap-4'>
          <Card className='w-[300px] shrink-0'>
            <CardContent className='p-2'>
              <ScrollArea className='h-[calc(100vh-220px)]'>
                {q.isLoading && <p className='p-3 text-sm text-muted-foreground'>Загрузка…</p>}
                {grouped.map((g) => (
                  <div key={g.dept} className='mb-3'>
                    <div className='px-2 py-1 text-xs font-semibold uppercase text-muted-foreground'>
                      {g.dept}
                    </div>
                    <div className='flex flex-col gap-1'>
                      {g.list.map((a) => {
                        const isActive = current?.id === a.id
                        return (
                          <button
                            key={a.id}
                            onClick={() => setSelected(a.id)}
                            className={`flex flex-col items-start gap-1 rounded-md px-2 py-2 text-left text-sm transition-colors hover:bg-accent ${
                              isActive ? 'bg-accent' : ''
                            }`}
                          >
                            <div className='flex w-full items-center justify-between'>
                              <span className='font-medium'>{a.id}</span>
                              <StatusBadge status={statusOf(a)} />
                            </div>
                            <div className='flex gap-2 text-xs text-muted-foreground'>
                              <Badge variant='outline'>{modelShort(a.model)}</Badge>
                            </div>
                          </button>
                        )
                      })}
                    </div>
                  </div>
                ))}
              </ScrollArea>
            </CardContent>
          </Card>

          <Card className='flex-1'>
            {current ? (
              <>
                <CardHeader>
                  <div className='flex items-center justify-between'>
                    <div>
                      <CardTitle className='text-xl'>{current.id}</CardTitle>
                      <p className='text-muted-foreground text-sm mt-1'>{fnOf(current)}</p>
                    </div>
                    <StatusBadge status={statusOf(current)} />
                  </div>
                  <div className='mt-3 flex gap-2'>
                    <Badge variant='outline'>{modelShort(current.model)}</Badge>
                    <Badge variant='secondary'>{deptOf(current)}</Badge>
                  </div>
                </CardHeader>
                <Separator />
                <CardContent className='pt-4'>
                  <h3 className='mb-2 text-sm font-semibold'>Mailbox</h3>
                  <Mailbox name={current.id} />
                </CardContent>
              </>
            ) : (
              <CardContent className='p-6 text-muted-foreground text-sm'>
                {q.isLoading ? 'Загрузка…' : 'Нет агентов'}
              </CardContent>
            )}
          </Card>
        </div>
      </Main>
    </>
  )
}
