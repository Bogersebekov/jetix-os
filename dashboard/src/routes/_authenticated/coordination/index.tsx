import { createFileRoute } from '@tanstack/react-router'
import { Coordination } from '@/features/coordination'

export const Route = createFileRoute('/_authenticated/coordination/')({
  component: Coordination,
})
