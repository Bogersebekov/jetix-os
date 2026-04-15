import { useQuery } from '@tanstack/react-query'
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { ProfileDropdown } from '@/components/profile-dropdown'
import { Search } from '@/components/search'
import { ThemeSwitch } from '@/components/theme-switch'
import { ConfigDrawer } from '@/components/config-drawer'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { ScrollArea } from '@/components/ui/scroll-area'
import { api, type Agent } from '@/lib/api'

function modelShort(model?: string | null): string {
  if (!model) return '—'
  if (model.includes('opus')) return 'Opus'
  if (model.includes('sonnet')) return 'Sonnet'
  if (model.includes('haiku')) return 'Haiku'
  return model
}

function modelStyle(model?: string | null): React.CSSProperties {
  const m = modelShort(model)
  if (m === 'Opus') return { background: '#cba6f730', color: '#cba6f7' }
  if (m === 'Sonnet') return { background: '#89b4fa30', color: '#89b4fa' }
  if (m === 'Haiku') return { background: '#a6e3a130', color: '#a6e3a1' }
  return { background: '#71717a30', color: '#a1a1aa' }
}

function statusOf(a: Agent): 'idle' | 'working' | 'error' {
  const s = (a.status || '').toLowerCase()
  if (['working', 'busy', 'active'].includes(s)) return 'working'
  if (['error', 'failed'].includes(s)) return 'error'
  return 'idle'
}

function statusDot(s: 'idle' | 'working' | 'error'): string {
  return s === 'working' ? 'bg-green-500' : s === 'error' ? 'bg-red-500' : 'bg-gray-500'
}

function AgentCard({ agent }: { agent: Agent }) {
  const s = statusOf(agent)
  const last = agent.last_message as
    | { from?: string; subject?: string; type?: string; timestamp?: string }
    | null
  return (
    <Card className='h-[150px]'>
      <CardContent className='p-3 flex flex-col gap-1.5 h-full'>
        <div className='flex items-center justify-between gap-2'>
          <div className='font-semibold text-sm truncate'>{agent.id}</div>
          <div className='flex items-center gap-1.5 shrink-0'>
            <span
              className='px-1.5 py-0.5 rounded text-[10px] font-medium'
              style={modelStyle(agent.model)}
            >
              {modelShort(agent.model)}
            </span>
            <span className={`h-2 w-2 rounded-full ${statusDot(s)}`} title={s} />
          </div>
        </div>
        <div className='text-[11px] text-muted-foreground'>{agent.department || 'Other'}</div>
        <div className='mt-auto text-xs text-muted-foreground border-t pt-1.5'>
          {last ? (
            <>
              <div className='truncate'>
                <span className='text-foreground/80'>{last.from || '—'}:</span>{' '}
                {last.subject || last.type || '(без темы)'}
              </div>
              <div className='text-[10px]'>
                {last.timestamp ? new Date(last.timestamp).toLocaleString() : ''}
              </div>
            </>
          ) : (
            <div>Нет сообщений</div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}

export function Coordination() {
  const q = useQuery({
    queryKey: ['coordination'],
    queryFn: api.coordination,
    refetchInterval: 10000,
  })
  const data = q.data

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
          <h1 className='text-2xl font-bold tracking-tight'>Coordination</h1>
          <p className='text-muted-foreground text-sm'>
            Обзор всех агентов и их активности
          </p>
        </div>

        {q.isLoading && <p className='text-sm text-muted-foreground'>Загрузка…</p>}
        {q.isError && <p className='text-sm text-red-400'>Ошибка загрузки</p>}

        {data && (
          <>
            <div className='grid gap-3 grid-cols-2 md:grid-cols-3 lg:grid-cols-6 mb-6'>
              {data.departments.map((d) => (
                <Card key={d.name}>
                  <CardContent className='p-3'>
                    <div className='text-xs text-muted-foreground uppercase'>{d.name}</div>
                    <div className='mt-1 text-2xl font-bold'>{d.agents.length}</div>
                    <div className='text-[11px] text-muted-foreground'>
                      {d.active > 0 ? (
                        <span className='text-green-400'>{d.active} working</span>
                      ) : (
                        'все idle'
                      )}
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>

            {data.departments.map((d) => {
              const agentsOfDept = data.agents
                .filter((a) => d.agents.includes(a.id))
                .sort((a, b) => a.id.localeCompare(b.id))
              if (!agentsOfDept.length) return null
              return (
                <div key={d.name} className='mb-6'>
                  <h2 className='mb-2 text-sm font-semibold uppercase text-muted-foreground'>
                    {d.name}
                  </h2>
                  <div className='grid gap-3 grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4'>
                    {agentsOfDept.map((a) => (
                      <AgentCard key={a.id} agent={a} />
                    ))}
                  </div>
                </div>
              )
            })}

            <Card>
              <CardHeader>
                <CardTitle>Recent Activity</CardTitle>
              </CardHeader>
              <CardContent>
                <ScrollArea className='h-[320px] pr-3'>
                  {data.recent_activity.length === 0 && (
                    <p className='text-sm text-muted-foreground'>Нет активности</p>
                  )}
                  <div className='flex flex-col gap-2'>
                    {data.recent_activity.map((m, i) => (
                      <div
                        key={i}
                        className='flex items-center justify-between gap-3 rounded-md border px-3 py-2 text-sm'
                      >
                        <div className='flex items-center gap-2 min-w-0'>
                          <span className='text-xs text-muted-foreground shrink-0'>
                            {m.timestamp ? new Date(m.timestamp).toLocaleString() : '—'}
                          </span>
                          <span className='truncate'>
                            <span className='text-foreground/80'>{m.from}</span>
                            <span className='text-muted-foreground'> → </span>
                            <span className='text-foreground/80'>{m.to}</span>
                            {m.subject && (
                              <span className='text-muted-foreground'>: {m.subject}</span>
                            )}
                          </span>
                        </div>
                      </div>
                    ))}
                  </div>
                </ScrollArea>
              </CardContent>
            </Card>
          </>
        )}
      </Main>
    </>
  )
}
