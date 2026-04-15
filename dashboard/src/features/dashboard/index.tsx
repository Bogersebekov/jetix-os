import { useQuery } from '@tanstack/react-query'
import { Rocket, Users, CheckCircle2, ListTodo } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { ProfileDropdown } from '@/components/profile-dropdown'
import { Search } from '@/components/search'
import { ThemeSwitch } from '@/components/theme-switch'
import { ConfigDrawer } from '@/components/config-drawer'
import { api } from '@/lib/api'
import { ProjectList } from './components/project-list'
import { RecentDecisions } from './components/recent-decisions'

function KpiCard({
  title,
  value,
  icon: Icon,
  loading,
  hint,
}: {
  title: string
  value: string | number
  icon: React.ComponentType<{ className?: string }>
  loading?: boolean
  hint?: string
}) {
  return (
    <Card>
      <CardHeader className='flex flex-row items-center justify-between space-y-0 pb-2'>
        <CardTitle className='text-sm font-medium'>{title}</CardTitle>
        <Icon className='text-muted-foreground h-4 w-4' />
      </CardHeader>
      <CardContent>
        <div className='text-2xl font-bold'>{loading ? '—' : value}</div>
        {hint && <p className='text-muted-foreground text-xs'>{hint}</p>}
      </CardContent>
    </Card>
  )
}

export function Dashboard() {
  const projectsQ = useQuery({ queryKey: ['projects'], queryFn: api.projects })
  const agentsQ = useQuery({ queryKey: ['agents'], queryFn: api.agents })
  const decisionsQ = useQuery({ queryKey: ['decisions'], queryFn: api.decisions })

  const activeProjects =
    projectsQ.data?.projects.filter((p) => p.status === 'Активный').length ?? 0
  const agentsOnline = agentsQ.data?.agents.length ?? 0
  const decisionsCount = decisionsQ.data?.decisions.length ?? 0

  return (
    <>
      <Header>
        <div className='ms-auto flex items-center space-x-4'>
          <Search />
          <ThemeSwitch />
          <ConfigDrawer />
          <ProfileDropdown />
        </div>
      </Header>

      <Main>
        <div className='mb-4 flex items-center justify-between'>
          <div>
            <h1 className='text-2xl font-bold tracking-tight'>Command Center</h1>
            <p className='text-muted-foreground text-sm'>
              Jetix OS — обзор проектов, агентов и решений
            </p>
          </div>
        </div>

        <div className='grid gap-4 sm:grid-cols-2 lg:grid-cols-4 mb-4'>
          <KpiCard
            title='Active Projects'
            value={activeProjects}
            icon={Rocket}
            loading={projectsQ.isLoading}
            hint={`всего ${projectsQ.data?.projects.length ?? 0}`}
          />
          <KpiCard
            title='Agents Online'
            value={agentsOnline}
            icon={Users}
            loading={agentsQ.isLoading}
          />
          <KpiCard
            title='Decisions Made'
            value={decisionsCount}
            icon={CheckCircle2}
            loading={decisionsQ.isLoading}
          />
          <KpiCard title='Pending Tasks' value={0} icon={ListTodo} />
        </div>

        <div className='grid grid-cols-1 gap-4 lg:grid-cols-7'>
          <Card className='col-span-1 lg:col-span-4'>
            <CardHeader>
              <CardTitle>Проекты</CardTitle>
            </CardHeader>
            <CardContent>
              <ProjectList
                projects={projectsQ.data?.projects}
                isLoading={projectsQ.isLoading}
              />
            </CardContent>
          </Card>
          <Card className='col-span-1 lg:col-span-3'>
            <CardHeader>
              <CardTitle>Recent Decisions</CardTitle>
            </CardHeader>
            <CardContent>
              <RecentDecisions
                data={decisionsQ.data}
                isLoading={decisionsQ.isLoading}
              />
            </CardContent>
          </Card>
        </div>
      </Main>
    </>
  )
}
