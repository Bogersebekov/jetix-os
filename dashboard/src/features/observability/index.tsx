import { useQuery } from '@tanstack/react-query'
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Legend,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts'
import { Activity, Coins, Layers, Zap } from 'lucide-react'
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { ProfileDropdown } from '@/components/profile-dropdown'
import { Search } from '@/components/search'
import { ThemeSwitch } from '@/components/theme-switch'
import { ConfigDrawer } from '@/components/config-drawer'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { api } from '@/lib/api'

const PIE_COLORS = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#64748b']

function fmtNum(n: number): string {
  if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(2)}M`
  if (n >= 1_000) return `${(n / 1_000).toFixed(1)}K`
  return String(n)
}

function fmtUsd(n: number): string {
  return `$${n.toFixed(2)}`
}

function Kpi({
  title,
  value,
  icon: Icon,
}: {
  title: string
  value: string
  icon: React.ComponentType<{ className?: string }>
}) {
  return (
    <Card>
      <CardHeader className='flex flex-row items-center justify-between space-y-0 pb-2'>
        <CardTitle className='text-sm font-medium'>{title}</CardTitle>
        <Icon className='text-muted-foreground h-4 w-4' />
      </CardHeader>
      <CardContent>
        <div className='text-2xl font-bold'>{value}</div>
      </CardContent>
    </Card>
  )
}

export function Observability() {
  const q = useQuery({ queryKey: ['observability'], queryFn: api.observability })
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
          <h1 className='text-2xl font-bold tracking-tight'>Observability</h1>
          <p className='text-muted-foreground text-sm'>
            Мониторинг Claude Code сессий — токены, стоимость, активность
          </p>
        </div>

        {q.isLoading && <p className='text-sm text-muted-foreground'>Загрузка…</p>}
        {q.isError && <p className='text-sm text-red-400'>Ошибка загрузки</p>}

        {data && (
          <>
            <div className='grid gap-4 sm:grid-cols-2 lg:grid-cols-4 mb-4'>
              <Kpi
                title='Total Tokens'
                value={fmtNum(data.summary.total_tokens)}
                icon={Zap}
              />
              <Kpi
                title='Total Cost'
                value={fmtUsd(data.summary.total_cost)}
                icon={Coins}
              />
              <Kpi
                title='Sessions'
                value={String(data.summary.total_sessions)}
                icon={Activity}
              />
              <Kpi
                title='Avg Tokens / Session'
                value={fmtNum(data.summary.avg_tokens_per_session)}
                icon={Layers}
              />
            </div>

            <Card className='mb-4'>
              <CardHeader>
                <CardTitle>Токены по дням</CardTitle>
              </CardHeader>
              <CardContent>
                <div className='h-[280px]'>
                  <ResponsiveContainer width='100%' height='100%'>
                    <AreaChart data={data.daily}>
                      <defs>
                        <linearGradient id='tokenFill' x1='0' y1='0' x2='0' y2='1'>
                          <stop offset='0%' stopColor='#3b82f6' stopOpacity={0.6} />
                          <stop offset='100%' stopColor='#3b82f6' stopOpacity={0} />
                        </linearGradient>
                      </defs>
                      <CartesianGrid strokeDasharray='3 3' stroke='#27272a' />
                      <XAxis dataKey='date' stroke='#a1a1aa' fontSize={12} />
                      <YAxis
                        stroke='#a1a1aa'
                        fontSize={12}
                        tickFormatter={(v) => fmtNum(Number(v))}
                      />
                      <Tooltip
                        contentStyle={{
                          background: '#18181b',
                          border: '1px solid #3f3f46',
                          borderRadius: 6,
                        }}
                        formatter={(v) => fmtNum(Number(v))}
                      />
                      <Area
                        type='monotone'
                        dataKey='tokens'
                        stroke='#3b82f6'
                        strokeWidth={2}
                        fill='url(#tokenFill)'
                      />
                    </AreaChart>
                  </ResponsiveContainer>
                </div>
              </CardContent>
            </Card>

            <div className='grid gap-4 grid-cols-1 lg:grid-cols-2'>
              <Card>
                <CardHeader>
                  <CardTitle>Стоимость по дням</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className='h-[280px]'>
                    <ResponsiveContainer width='100%' height='100%'>
                      <BarChart data={data.daily}>
                        <CartesianGrid strokeDasharray='3 3' stroke='#27272a' />
                        <XAxis dataKey='date' stroke='#a1a1aa' fontSize={12} />
                        <YAxis
                          stroke='#a1a1aa'
                          fontSize={12}
                          tickFormatter={(v) => `$${v}`}
                        />
                        <Tooltip
                          contentStyle={{
                            background: '#18181b',
                            border: '1px solid #3f3f46',
                            borderRadius: 6,
                          }}
                          formatter={(v) => fmtUsd(Number(v))}
                        />
                        <Bar dataKey='cost' fill='#3b82f6' radius={[4, 4, 0, 0]} />
                      </BarChart>
                    </ResponsiveContainer>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle>Токены по агентам</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className='h-[280px]'>
                    <ResponsiveContainer width='100%' height='100%'>
                      <PieChart>
                        <Pie
                          data={data.by_agent}
                          dataKey='tokens'
                          nameKey='agent'
                          innerRadius={55}
                          outerRadius={95}
                          paddingAngle={2}
                        >
                          {data.by_agent.map((_, i) => (
                            <Cell key={i} fill={PIE_COLORS[i % PIE_COLORS.length]} />
                          ))}
                        </Pie>
                        <Tooltip
                          contentStyle={{
                            background: '#18181b',
                            border: '1px solid #3f3f46',
                            borderRadius: 6,
                          }}
                          formatter={(v) => fmtNum(Number(v))}
                        />
                        <Legend wrapperStyle={{ fontSize: 12 }} />
                      </PieChart>
                    </ResponsiveContainer>
                  </div>
                </CardContent>
              </Card>
            </div>
          </>
        )}
      </Main>
    </>
  )
}
