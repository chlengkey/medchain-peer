import { createRouter, createWebHashHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import DaftarPasien from '@/views/DaftarPasien.vue'

const routes = [
  {
  	path : '/',
  	name : "Dashboard",
  	component: Dashboard
  },
  {
    path : '/DaftarPasien',
    name : "DaftarPasien",
    component : DaftarPasien
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
