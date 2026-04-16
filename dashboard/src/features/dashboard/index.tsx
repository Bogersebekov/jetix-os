import { useQuery } from '@tanstack/react-query'
import { CalendarDays } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Separator } from '@/components/ui/separator'
import { Skeleton } from '@/components/ui/skeleton'
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { ProfileDropdown } from '@/components/profile-dropdown'
import { Search } from '@/components/search'
import { ThemeSwitch } from '@/components/theme-switch'
import { ConfigDrawer } from '@/components/config-drawer'
import { api } from '@/lib/api'
import { ProjectList } from './components/project-list'
import { RecentDecisions } from './components/recent-decisions'

export function Dashboard() {
  const focusQ = useQuery({ queryKey: ['focus'], queryFn: api.focus })
  const projectsQ = useQuery({ queryKey: ['projects'], queryFn: api.projects })
  const decisionsQ = useQuery({ queryKey: ['decisions'], queryFn: api.decisions })

  const focus = focusQ.data

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
        <div className='mb-4'>
          <h1 className='text-2xl font-bold tracking-tight'>Command Center</h1>
          <p className='text-muted-foreground text-sm'>
            Jetix OS — стратегия, фокус, проекты
          </p>
        </div>

        {/* Стратегия */}
        <Card className='mb-4'>
          <CardContent className='pt-6'>
            {focusQ.isLoading ? (
              <div className='space-y-3'>
                <Skeleton className='h-8 w-3/4' />
                <Skeleton className='h-4 w-1/2' />
              </div>
            ) : (
              <div className='flex flex-col gap-4 md:flex-row md:gap-8'>
                <div className='flex-[2] min-w-0'>
                  <p className='text-xl font-bold tracking-tight md:text-2xl'>
                    {focus?.global_goal ?? '—'}
                  </p>
                  <p className='text-muted-foreground text-xs mt-1'>Глобальная цель</p>
                </div>
                <Separator orientation='vertical' className='hidden md:block h-auto' />
                <div className='flex-1 min-w-0'>
                  <p className='text-muted-foreground text-xs mb-2'>Фокус недели</p>
                  <ol className='list-decimal list-inside space-y-0.5 text-sm'>
                    {focus?.week_focus.items.map((item, i) => (
                      <li key={i} className='leading-snug'>{item}</li>
                    ))}
                  </ol>
                  <p className='text-muted-foreground text-[11px] mt-2'>
                    Неделя: {focus?.week_focus.week ?? '—'}
                  </p>
                </div>
              </div>
            )}
          </CardContent>
        </Card>

        {/* Фокус дня */}
        <Card className='mb-4 border-l-4 border-l-amber-500'>
          <CardContent className='flex items-start gap-3 py-3'>
            <CalendarDays className='text-amber-500 mt-0.5 h-5 w-5 shrink-0' />
            <div className='flex-1 min-w-0'>
              {focusQ.isLoading ? (
                <Skeleton className='h-5 w-1/2' />
              ) : (
                <>
                  <div className='flex items-baseline gap-2 flex-wrap'>
                    <span className='font-semibold text-sm'>Фокус дня</span>
                    <span className='text-muted-foreground text-xs'>
                      {focus?.day_focus.date ?? '—'}
                    </span>
                  </div>
                  <div className='flex flex-wrap gap-x-3 gap-y-0.5 mt-1 text-sm'>
                    {focus?.day_focus.items.map((item, i) => (
                      <span key={i} className='flex items-center gap-1.5'>
                        {i > 0 && (
                          <span className='text-muted-foreground hidden sm:inline'>·</span>
                        )}
                        {item}
                      </span>
                    ))}
                  </div>
                </>
              )}
            </div>
          </CardContent>
        </Card>

        {/* Активные проекты */}
        <Card className='mb-4'>
          <CardHeader className='pb-3'>
            <CardTitle className='text-base'>Активные проекты</CardTitle>
          </CardHeader>
          <CardContent>
            <ProjectList
              projects={projectsQ.data?.projects}
              isLoading={projectsQ.isLoading}
            />
          </CardContent>
        </Card>

        {/* Последние решения */}
        <Card>
          <CardHeader className='pb-3'>
            <CardTitle className='text-base'>Последние решения</CardTitle>
          </CardHeader>
          <CardContent>
            <RecentDecisions
              data={decisionsQ.data}
              isLoading={decisionsQ.isLoading}
            />
          </CardContent>
        </Card>
      </Main>
    </>
  )
}
