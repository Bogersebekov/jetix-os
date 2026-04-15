import { useEffect, useMemo, useState } from 'react'
import {
  DndContext,
  DragOverlay,
  PointerSensor,
  useSensor,
  useSensors,
  closestCorners,
  type DragEndEvent,
  type DragStartEvent,
  type DragOverEvent,
} from '@dnd-kit/core'
import {
  SortableContext,
  useSortable,
  verticalListSortingStrategy,
  arrayMove,
} from '@dnd-kit/sortable'
import { CSS } from '@dnd-kit/utilities'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { Plus } from 'lucide-react'
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { ProfileDropdown } from '@/components/profile-dropdown'
import { Search } from '@/components/search'
import { ThemeSwitch } from '@/components/theme-switch'
import { ConfigDrawer } from '@/components/config-drawer'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { api, type KanbanCard, type KanbanColumn, type KanbanState } from '@/lib/api'

function priorityStyle(p: number): string {
  if (p === 1) return 'bg-red-500/20 text-red-400'
  if (p === 2) return 'bg-orange-500/20 text-orange-400'
  if (p === 3) return 'bg-yellow-500/20 text-yellow-400'
  return 'bg-gray-500/20 text-gray-400'
}

function findColumnId(state: KanbanState, cardId: string): string | null {
  for (const col of state.columns) {
    if (col.cards.some((c) => c.id === cardId)) return col.id
  }
  return null
}

function CardView({ card }: { card: KanbanCard }) {
  const { attributes, listeners, setNodeRef, transform, transition, isDragging } = useSortable({
    id: card.id,
    data: { type: 'card', card },
  })
  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    opacity: isDragging ? 0.4 : 1,
  }
  return (
    <div ref={setNodeRef} style={style} {...attributes} {...listeners}>
      <Card className='cursor-grab active:cursor-grabbing'>
        <CardContent className='p-3'>
          <div className='flex items-start justify-between gap-2'>
            <div className='font-medium text-sm'>{card.title}</div>
            <span className={`px-2 py-0.5 rounded text-xs shrink-0 ${priorityStyle(card.priority)}`}>
              P{card.priority}
            </span>
          </div>
          {card.description && (
            <div className='mt-1 text-xs text-muted-foreground line-clamp-2'>
              {card.description}
            </div>
          )}
          {card.assignee && (
            <div className='mt-2 text-xs text-muted-foreground'>@{card.assignee}</div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}

function Column({
  column,
  onAdd,
}: {
  column: KanbanColumn
  onAdd: (columnId: string) => void
}) {
  const { setNodeRef } = useSortable({
    id: column.id,
    data: { type: 'column', column },
  })

  return (
    <div
      ref={setNodeRef}
      className='flex w-[300px] shrink-0 flex-col rounded-lg bg-muted/50 p-2'
    >
      <div className='flex items-center justify-between px-2 py-1'>
        <div className='font-semibold text-sm'>{column.title}</div>
        <span className='text-xs text-muted-foreground'>{column.cards.length}</span>
      </div>
      <SortableContext
        items={column.cards.map((c) => c.id)}
        strategy={verticalListSortingStrategy}
      >
        <div className='flex min-h-[100px] flex-col gap-2 p-1'>
          {column.cards.map((c) => (
            <CardView key={c.id} card={c} />
          ))}
        </div>
      </SortableContext>
      <Button
        variant='ghost'
        size='sm'
        className='mt-2 justify-start text-muted-foreground'
        onClick={() => onAdd(column.id)}
      >
        <Plus className='h-4 w-4 mr-1' /> Добавить карточку
      </Button>
    </div>
  )
}

function AddCardDialog({
  columnId,
  open,
  onOpenChange,
  onSubmit,
}: {
  columnId: string | null
  open: boolean
  onOpenChange: (v: boolean) => void
  onSubmit: (card: KanbanCard) => void
}) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [priority, setPriority] = useState('3')
  const [assignee, setAssignee] = useState('')

  useEffect(() => {
    if (open) {
      setTitle('')
      setDescription('')
      setPriority('3')
      setAssignee('')
    }
  }, [open])

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Новая карточка</DialogTitle>
        </DialogHeader>
        <div className='grid gap-3'>
          <div>
            <Label>Заголовок</Label>
            <Input value={title} onChange={(e) => setTitle(e.target.value)} />
          </div>
          <div>
            <Label>Описание</Label>
            <Textarea value={description} onChange={(e) => setDescription(e.target.value)} />
          </div>
          <div>
            <Label>Приоритет</Label>
            <Select value={priority} onValueChange={setPriority}>
              <SelectTrigger>
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value='1'>P1</SelectItem>
                <SelectItem value='2'>P2</SelectItem>
                <SelectItem value='3'>P3</SelectItem>
                <SelectItem value='4'>P4</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <div>
            <Label>Исполнитель</Label>
            <Input value={assignee} onChange={(e) => setAssignee(e.target.value)} />
          </div>
        </div>
        <DialogFooter>
          <Button variant='outline' onClick={() => onOpenChange(false)}>
            Отмена
          </Button>
          <Button
            disabled={!title.trim() || !columnId}
            onClick={() => {
              onSubmit({
                id: `c-${Date.now()}`,
                title: title.trim(),
                description: description.trim() || undefined,
                priority: Number(priority),
                assignee: assignee.trim() || undefined,
              })
            }}
          >
            Создать
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}

export function Kanban() {
  const qc = useQueryClient()
  const q = useQuery({ queryKey: ['kanban'], queryFn: api.kanban })
  const [local, setLocal] = useState<KanbanState | null>(null)
  const [activeCard, setActiveCard] = useState<KanbanCard | null>(null)
  const [addColumnId, setAddColumnId] = useState<string | null>(null)

  useEffect(() => {
    if (q.data) setLocal(q.data)
  }, [q.data])

  const save = useMutation({
    mutationFn: (state: KanbanState) => api.saveKanban(state),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['kanban'] }),
  })

  const sensors = useSensors(useSensor(PointerSensor, { activationConstraint: { distance: 5 } }))

  const state = local

  const columnIds = useMemo(() => state?.columns.map((c) => c.id) ?? [], [state])

  function handleDragStart(e: DragStartEvent) {
    const card = e.active.data.current?.card as KanbanCard | undefined
    if (card) setActiveCard(card)
  }

  function handleDragOver(e: DragOverEvent) {
    if (!state) return
    const { active, over } = e
    if (!over) return
    const activeId = String(active.id)
    const overId = String(over.id)
    if (activeId === overId) return

    const activeCol = findColumnId(state, activeId)
    if (!activeCol) return

    const overIsColumn = state.columns.some((c) => c.id === overId)
    const overCol = overIsColumn ? overId : findColumnId(state, overId)
    if (!overCol || activeCol === overCol) return

    setLocal((prev) => {
      if (!prev) return prev
      const next = { columns: prev.columns.map((c) => ({ ...c, cards: [...c.cards] })) }
      const from = next.columns.find((c) => c.id === activeCol)!
      const to = next.columns.find((c) => c.id === overCol)!
      const idx = from.cards.findIndex((c) => c.id === activeId)
      if (idx === -1) return prev
      const [moved] = from.cards.splice(idx, 1)
      const overIdx = overIsColumn ? to.cards.length : to.cards.findIndex((c) => c.id === overId)
      to.cards.splice(overIdx === -1 ? to.cards.length : overIdx, 0, moved)
      return next
    })
  }

  function handleDragEnd(e: DragEndEvent) {
    setActiveCard(null)
    if (!state) return
    const { active, over } = e
    if (!over) return
    const activeId = String(active.id)
    const overId = String(over.id)

    let next = state
    if (activeId !== overId) {
      const col = findColumnId(state, activeId)
      const overCol = findColumnId(state, overId)
      if (col && overCol && col === overCol) {
        const column = state.columns.find((c) => c.id === col)!
        const oldIndex = column.cards.findIndex((c) => c.id === activeId)
        const newIndex = column.cards.findIndex((c) => c.id === overId)
        if (oldIndex !== -1 && newIndex !== -1 && oldIndex !== newIndex) {
          next = {
            columns: state.columns.map((c) =>
              c.id === col ? { ...c, cards: arrayMove(c.cards, oldIndex, newIndex) } : c
            ),
          }
          setLocal(next)
        }
      }
    }
    save.mutate(next)
  }

  function addCard(card: KanbanCard) {
    if (!state || !addColumnId) return
    const next: KanbanState = {
      columns: state.columns.map((c) =>
        c.id === addColumnId ? { ...c, cards: [...c.cards, card] } : c
      ),
    }
    setLocal(next)
    save.mutate(next)
    setAddColumnId(null)
  }

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
          <h1 className='text-2xl font-bold tracking-tight'>Kanban</h1>
          <p className='text-muted-foreground text-sm'>
            Состояние хранится в shared/state/kanban.json
          </p>
        </div>

        {q.isLoading && <p className='text-sm text-muted-foreground'>Загрузка…</p>}
        {q.isError && <p className='text-sm text-red-400'>Ошибка загрузки</p>}

        {state && (
          <DndContext
            sensors={sensors}
            collisionDetection={closestCorners}
            onDragStart={handleDragStart}
            onDragOver={handleDragOver}
            onDragEnd={handleDragEnd}
          >
            <div className='flex gap-4 overflow-x-auto pb-4'>
              <SortableContext items={columnIds}>
                {state.columns.map((col) => (
                  <Column key={col.id} column={col} onAdd={setAddColumnId} />
                ))}
              </SortableContext>
            </div>
            <DragOverlay>
              {activeCard ? <CardView card={activeCard} /> : null}
            </DragOverlay>
          </DndContext>
        )}

        <AddCardDialog
          open={addColumnId !== null}
          onOpenChange={(v) => !v && setAddColumnId(null)}
          columnId={addColumnId}
          onSubmit={addCard}
        />
      </Main>
    </>
  )
}
