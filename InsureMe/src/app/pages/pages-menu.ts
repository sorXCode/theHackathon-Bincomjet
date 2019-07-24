import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'IoT Dashboard',
    icon: 'home-outline',
    link: '/pages/iot-dashboard'
  },
  {
    title: 'Policies',
    icon: 'folder-outline',
    link: '/pages/insurance-types'
  },
  {
    title: 'Buy Products',
    icon: 'checkmark-square-outline',
    children: [
      {
        title: 'Auto Insurance',
        link: '/pages/auto-create'
      },
      {
        title: 'Health Insurance',
        link: '/pages/health-create'
      },
      {
        title: 'Life Insurance',
        link: '/pages/life-create'
      }
    ]
  },
  {
    title: 'Auth',
    icon: 'lock-outline',
    children: [
      {
        title: 'Login',
        link: '/login'
      },
      {
        title: 'Register',
        link: '/register'
      }
    ]
  }
];
