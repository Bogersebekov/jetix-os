import { useEffect, useMemo, useRef, useState } from 'react'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { Inbox, Send } from 'lucide-react'
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { ProfileDropdown } from '@/components/profile-dropdown'
import { Search } from '@/components/search'
import { ThemeSwitch } from '@/components/theme-switch'
import { ConfigDrawer } from '@/components/config-drawer'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Textarea } from '@/components/ui/textarea'
import { api, type ChatAgent, type MailboxMessage } from '@/lib/api'

const DEPT_ORDER = ['MGMT', 'OPS', 'Sales', 'Brain', 'Meta', 'Life', 'Other']

type Selection = { kind: 'human' } | { kind: 'agent'; name: string }

function MessageBubble({ msg, isMine }: { msg: MailboxMessage; isMine: boolean }) {
  return (
    <div className={`flex ${isMine ? 'justify-end' : 'justify-start'}`}>
      <Card className={`max-w-[75%] ${isMine ? 'bg-primary/10' : 'bg-muted'}`}>
        <CardContent className='p-3'>
          <div className='flex items-center justify-between gap-3 text-xs text-muted-foreground'>
            <span>{msg.from || '—'}</span>
            <span>{msg.timestamp ? new Date(msg.timestamp).toLocaleString() : ''}</span>
          </div>
          {msg.subject && <div className='mt-1 text-sm font-medium'>{msg.subject}</div>}
          {msg.body && <div className='mt-1 text-sm whitespace-pre-wrap'>{msg.body}</div>}
        </CardContent>
      </Card>
    </div>
  )
}

export function Chats() {
  const qc = useQueryClient()
  const agentsQ = useQuery({
    queryKey: ['chat-agents'],
    queryFn: api.chatAgents,
    refetchInterval: 10000,
  })
  const [selection, setSelection] = useState<Selection>({ kind: 'human' })
  const [subject, setSubject] = useState('')
  const [content, setContent] = useState('')
  const scrollRef = useRef<HTMLDivElement>(null)

  const mailboxKey =
    selection.kind === 'human' ? ['chat-human'] : ['chat-mailbox', selection.name]

  const mailboxQ = useQuery({
    queryKey: mailboxKey,
    queryFn: () =>
      selection.kind === 'human' ? api.chatHuman() : api.chatMailbox(selection.name),
    refetchInterval: 5000,
  })

  const grouped = useMemo(() => {
    const agents = agentsQ.data?.agents ?? []
    const g = new Map<string, ChatAgent[]>()
    for (const a of agents) {
      if (!g.has(a.department)) g.set(a.department, [])
      g.get(a.department)!.push(a)
    }
    return DEPT_ORDER.filter((d) => g.has(d)).map((d) => ({
      dept: d,
      list: g.get(d)!.sort((a, b) => a.name.localeCompare(b.name)),
    }))
  }, [agentsQ.data])

  const messages = mailboxQ.data?.messages ?? []

  useEffect(() => {
    const el = scrollRef.current
    if (el) el.scrollTop = el.scrollHeight
  }, [messages.length, selection])

  const send = useMutation({
    mutationFn: (payload: { to: string; subject: string; content: string }) =>
      api.chatSend({ from: 'human', ...payload }),
    onSuccess: () => {
      setContent('')
      setSubject('')
      qc.invalidateQueries({ queryKey: mailboxKey })
      qc.invalidateQueries({ queryKey: ['chat-agents'] })
    },
  })

  function handleSend() {
    if (selection.kind !== 'agent') return
    if (!content.trim()) return
    send.mutate({ to: selection.name, subject: subject.trim(), content: content.trim() })
  }

  const title = selection.kind === 'human' ? 'Inbox (human)' : selection.name

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
          <h1 className='text-2xl font-bold tracking-tight'>Chat</h1>
          <p className='text-muted-foreground text-sm'>
            Переписка с агентами через JSONL mailboxes
          </p>
        </div>

        <div className='flex gap-4 h-[calc(100vh-200px)]'>
          <Card className='w-[300px] shrink-0'>
            <CardContent className='p-2'>
              <ScrollArea className='h-[calc(100vh-220px)]'>
                <button
                  onClick={() => setSelection({ kind: 'human' })}
                  className={`flex w-full items-center justify-between gap-2 rounded-md px-2 py-2 text-left text-sm hover:bg-accent ${
                    selection.kind === 'human' ? 'bg-accent' : ''
                  }`}
                >
                  <div className='flex items-center gap-2'>
                    <Inbox className='h-4 w-4' />
                    <span className='font-medium'>Inbox (human)</span>
                  </div>
                </button>

                <div className='my-2 h-px bg-border' />

                {agentsQ.isLoading && (
                  <p className='p-2 text-sm text-muted-foreground'>Загрузка…</p>
                )}

                {grouped.map((g) => (
                  <div key={g.dept} className='mb-2'>
                    <div className='px-2 py-1 text-xs font-semibold uppercase text-muted-foreground'>
                      {g.dept}
                    </div>
                    {g.list.map((a) => {
                      const active =
                        selection.kind === 'agent' && selection.name === a.name
                      return (
                        <button
                          key={a.name}
                          onClick={() => setSelection({ kind: 'agent', name: a.name })}
                          className={`flex w-full items-center justify-between gap-2 rounded-md px-2 py-2 text-left text-sm hover:bg-accent ${
                            active ? 'bg-accent' : ''
                          }`}
                        >
                          <span className='truncate'>{a.name}</span>
                          {a.unread > 0 && <Badge variant='secondary'>{a.unread}</Badge>}
                        </button>
                      )
                    })}
                  </div>
                ))}
              </ScrollArea>
            </CardContent>
          </Card>

          <Card className='flex flex-1 flex-col overflow-hidden'>
            <div className='border-b p-3'>
              <div className='font-semibold'>{title}</div>
              <div className='text-xs text-muted-foreground'>
                {mailboxQ.data?.total ?? 0} сообщений
              </div>
            </div>

            <div ref={scrollRef} className='flex-1 overflow-y-auto p-4'>
              {mailboxQ.isLoading && (
                <p className='text-sm text-muted-foreground'>Загрузка…</p>
              )}
              {!mailboxQ.isLoading && messages.length === 0 && (
                <p className='text-sm text-muted-foreground'>Нет сообщений</p>
              )}
              <div className='flex flex-col gap-3'>
                {messages.map((m) => (
                  <MessageBubble key={m.id} msg={m} isMine={(m.from || '') === 'human'} />
                ))}
              </div>
            </div>

            {selection.kind === 'agent' && (
              <div className='border-t p-3'>
                <div className='flex flex-col gap-2'>
                  <Input
                    placeholder='Тема (опционально)'
                    value={subject}
                    onChange={(e) => setSubject(e.target.value)}
                  />
                  <div className='flex gap-2'>
                    <Textarea
                      placeholder={`Сообщение для ${selection.name}…`}
                      value={content}
                      onChange={(e) => setContent(e.target.value)}
                      rows={2}
                      onKeyDown={(e) => {
                        if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) {
                          e.preventDefault()
                          handleSend()
                        }
                      }}
                    />
                    <Button
                      onClick={handleSend}
                      disabled={!content.trim() || send.isPending}
                    >
                      <Send className='h-4 w-4 mr-1' />
                      Отправить
                    </Button>
                  </div>
                </div>
              </div>
            )}
          </Card>
        </div>
      </Main>
    </>
  )
}
