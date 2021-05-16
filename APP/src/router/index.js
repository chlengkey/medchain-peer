import { createRouter, createWebHashHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import DaftarPasien from '@/views/DaftarPasien.vue'
import PeriksaPasien from '@/views/PeriksaPasien.vue'

const routes = [
  {
  	path : '/',
  	name : "Dashboard",
  	component: Dashboard
  },
  {
    path : '/pasien',
    name : "Daftar Pasien",
    component : DaftarPasien
  },
  {
    path : '/pasien/periksa/:token',
    name : "Periksa Pasien",
    component : PeriksaPasien
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
