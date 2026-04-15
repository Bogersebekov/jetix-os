import { createFileRoute } from '@tanstack/react-router'
import { Kanban } from '@/features/kanban'

export const Route = createFileRoute('/_authenticated/kanban/')({
  component: Kanban,
})
