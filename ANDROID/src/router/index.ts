import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import Tabs from '../views/Tabs.vue'
import Dashboard from '../views/Main.vue'
import Login from '@/account/Login.vue'
import Register from '@/account/Register.vue'
import Account from '@/account/Account.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/account/register',
    component: Register
  },
  {
    path: '/account/login',
    component: Login
  },
  {
    path: '/',
    component: Dashboard
  },
  {
    path: '/account',
    component: Account
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
