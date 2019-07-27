import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Dashboard',
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
    icon: 'shopping-cart-outline',
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
    title: 'My Policies',
    icon: 'folder-outline',
    children: [
      {
        title: 'Auto Insurance Policies',
        link: '/pages/my-policies'
      },
      {
        title: 'Health Insurance Policies',
        link: '/pages/health-policies'
      },
      {
        title: 'Life Insurance Policies',
        link: '/pages/life-policies'
      }
    ]
  },
  {
    title: 'Make Claims',
    icon: 'checkmark-square-outline',
    children: [
      {
        title: 'Auto Insurance Claims',
        link: '/pages/claims/auto-claims'
      },
      {
        title: 'Health Insurance Claims',
        link: '/pages/claims/health-claims'
      },
      {
        title: 'Life Insurance Claims',
        link: '/pages/claims/life-claims'
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
  },
  {
    title: 'Edit Profile Information',
    icon: 'folder-outline',
    children: [
      {
        title: 'Profile',
        link: '/biodata-form'
      },
      {
        title: 'Add New Bank Details',
        link: '/bank-form'
      },
      {
        title: 'Add New Work Details',
        link: '/work-form'
      }
    ]
  }
];
