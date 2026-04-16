import {
  LayoutDashboard,
  Monitor,
  ListTodo,
  Bell,
  Palette,
  Settings,
  Wrench,
  UserCog,
  Users,
  MessagesSquare,
  Activity,
  Network,
  Rocket,
} from 'lucide-react'
import { type SidebarData } from '../types'

export const sidebarData: SidebarData = {
  user: {
    name: 'Руслан',
    email: 'xoshdlsp@gmail.com',
    avatar: '/avatars/shadcn.jpg',
  },
  teams: [
    {
      name: 'Jetix OS',
      logo: Rocket,
      plan: 'Command Center',
    },
  ],
  navGroups: [
    {
      title: 'General',
      items: [
        {
          title: 'Command Center',
          url: '/',
          icon: LayoutDashboard,
        },
        {
          title: 'Kanban',
          url: '/kanban',
          icon: ListTodo,
        },
        {
          title: 'Chat',
          url: '/chats',
          icon: MessagesSquare,
        },
        {
          title: 'Agents',
          url: '/agents',
          icon: Users,
        },
        {
          title: 'Coordination',
          url: '/coordination',
          icon: Network,
        },
        {
          title: 'Observability',
          url: '/observability',
          icon: Activity,
        },
        {
          title: 'Settings',
          icon: Settings,
          items: [
            {
              title: 'Profile',
              url: '/settings',
              icon: UserCog,
            },
            {
              title: 'Account',
              url: '/settings/account',
              icon: Wrench,
            },
            {
              title: 'Appearance',
              url: '/settings/appearance',
              icon: Palette,
            },
            {
              title: 'Notifications',
              url: '/settings/notifications',
              icon: Bell,
            },
            {
              title: 'Display',
              url: '/settings/display',
              icon: Monitor,
            },
          ],
        },
      ],
    },
  ],
}
