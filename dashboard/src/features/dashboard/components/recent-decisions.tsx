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
      <div className='space-y-3'>
        {Array.from({ length: 5 }).map((_, i) => (
          <Skeleton key={i} className='h-10 w-full' />
        ))}
      </div>
    )
  }

  const decisions = data?.decisions || []
  const date = data?.updated_at ? new Date(data.updated_at).toISOString().slice(0, 10) : '—'

  if (!decisions.length)
    return <p className='text-muted-foreground text-sm'>Нет решений</p>

  return (
    <div className='space-y-4'>
      {decisions.map((d, i) => (
        <div key={i} className='flex items-start gap-3 text-sm'>
          <div className='text-muted-foreground min-w-[2rem] text-xs font-mono'>
            #{decisions.length - i}
          </div>
          <div className='flex-1'>
            <p className='leading-snug'>{d}</p>
            <p className='text-muted-foreground text-xs mt-1'>{date}</p>
          </div>
        </div>
      ))}
    </div>
  )
}
