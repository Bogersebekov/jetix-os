import { Badge } from '@/components/ui/badge'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Skeleton } from '@/components/ui/skeleton'
import type { Project } from '@/lib/api'

const PRIORITY_COLORS: Record<number, { label: string; bg: string; fg: string }> = {
  1: { label: 'P1', bg: '#f38ba8', fg: '#1e1e2e' },
  2: { label: 'P2', bg: '#fab387', fg: '#1e1e2e' },
  3: { label: 'P3', bg: '#f9e2af', fg: '#1e1e2e' },
  4: { label: 'P4', bg: '#6c7086', fg: '#ffffff' },
}

function prioStyle(p: number) {
  return PRIORITY_COLORS[p] || { label: `P${p}`, bg: '#6c7086', fg: '#ffffff' }
}

export function ProjectList({
  projects,
  isLoading,
}: {
  projects: Project[] | undefined
  isLoading: boolean
}) {
  if (isLoading) {
    return (
      <div className='space-y-3'>
        {Array.from({ length: 4 }).map((_, i) => (
          <Skeleton key={i} className='h-24 w-full' />
        ))}
      </div>
    )
  }

  const sorted = [...(projects || [])].sort((a, b) => a.priority - b.priority)

  return (
    <div className='space-y-3'>
      {sorted.map((p) => {
        const s = prioStyle(p.priority)
        return (
          <Card key={p.name}>
            <CardHeader className='pb-2'>
              <div className='flex items-center gap-2'>
                <span
                  className='rounded px-2 py-0.5 text-xs font-bold'
                  style={{ backgroundColor: s.bg, color: s.fg }}
                >
                  {s.label}
                </span>
                <CardTitle className='text-base'>{p.name}</CardTitle>
                <Badge variant='outline' className='ms-auto'>
                  {p.status}
                </Badge>
              </div>
            </CardHeader>
            <CardContent className='space-y-1 pt-0'>
              <p className='text-muted-foreground text-xs'>
                <span className='font-medium'>Фаза:</span> {p.current_phase}
              </p>
              <p className='text-sm'>{p.description}</p>
            </CardContent>
          </Card>
        )
      })}
      {sorted.length === 0 && (
        <p className='text-muted-foreground text-sm'>Нет проектов</p>
      )}
    </div>
  )
}
