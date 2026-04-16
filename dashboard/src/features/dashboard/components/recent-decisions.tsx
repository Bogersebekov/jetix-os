import { Skeleton } from '@/components/ui/skeleton'
import type { DecisionsPayload } from '@/lib/api'

export function RecentDecisions({
  data,
  isLoading,
}: {
  data: DecisionsPayload | undefined
  isLoading: boolean
}) {
  if (isLoading) {
    return (
      <div className='space-y-2'>
        {Array.from({ length: 3 }).map((_, i) => (
          <Skeleton key={i} className='h-6 w-full' />
        ))}
      </div>
    )
  }

  const decisions = (data?.decisions || []).slice(0, 5)
  const date = data?.updated_at ? new Date(data.updated_at).toISOString().slice(0, 10) : '—'

  if (!decisions.length)
    return <p className='text-muted-foreground text-sm'>Нет решений</p>

  return (
    <div className='space-y-1.5'>
      {decisions.map((d, i) => (
        <div key={i} className='flex items-baseline gap-2 text-sm'>
          <span className='text-muted-foreground text-xs font-mono shrink-0'>
            #{decisions.length - i}
          </span>
          <span className='flex-1 leading-snug'>{d}</span>
          <span className='text-muted-foreground text-xs shrink-0'>{date}</span>
        </div>
      ))}
    </div>
  )
}
