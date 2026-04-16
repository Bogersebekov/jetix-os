import { Badge } from '@/components/ui/badge'
import { Skeleton } from '@/components/ui/skeleton'
import type { Project } from '@/lib/api'

const PRIORITY_COLORS: Record<number, { label: string; className: string }> = {
  1: { label: 'P1', className: 'bg-red-500 text-white' },
  2: { label: 'P2', className: 'bg-orange-500 text-white' },
  3: { label: 'P3', className: 'bg-yellow-500 text-black' },
  4: { label: 'P4', className: 'bg-muted text-muted-foreground' },
}

function prioBadge(p: number) {
  const s = PRIORITY_COLORS[p] || { label: `P${p}`, className: 'bg-muted text-muted-foreground' }
  return (
    <span className={`inline-flex items-center rounded px-1.5 py-0.5 text-[11px] font-bold leading-none ${s.className}`}>
      {s.label}
    </span>
  )
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
      <div className='space-y-2'>
        {Array.from({ length: 4 }).map((_, i) => (
          <Skeleton key={i} className='h-8 w-full' />
        ))}
      </div>
    )
  }

  const active = [...(projects || [])]
    .filter((p) => p.status === 'Активный' || p.status === 'Active')
    .sort((a, b) => a.priority - b.priority)

  if (!active.length)
    return <p className='text-muted-foreground text-sm'>Нет активных проектов</p>

  return (
    <div className='space-y-1'>
      {active.map((p) => (
        <div
          key={p.name}
          className='flex items-center gap-3 rounded-md px-2 py-1.5 text-sm hover:bg-muted/50'
        >
          {prioBadge(p.priority)}
          <span className='font-medium flex-1 truncate'>{p.name}</span>
          <span className='text-muted-foreground text-xs truncate max-w-[160px]'>
            {p.current_phase}
          </span>
          <Badge variant='outline' className='text-[11px]'>
            {p.status}
          </Badge>
        </div>
      ))}
    </div>
  )
}
