import { createRouter, createWebHashHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import DataPasien from '@/views/DataPasien.vue'
import DataDokter from '@/views/DataDokter.vue'
import PeriksaPasien from '@/views/PeriksaPasien.vue'
import Pengaturan from '@/mining/index.vue'
import Login from '@/account/login.vue'

const routes = [
  {
  	path : '/',
  	name : "Dashboard",
  	component: Dashboard
  },
  {
    path : '/pasien/:token',
    name : "Data Pasien",
    component : DataPasien
  },
  {
    path : '/pasien/periksa/:token',
    name : "Periksa Pasien",
    component : PeriksaPasien
  },
  {
    path : '/dataDokter',
    name : "Data Dokter",
    component : DataDokter
  },
  {
    path : '/pengaturan',
    name : "Pengaturan",
    component : Pengaturan
  },
  {
    path : '/login',
    name : "Login",
    component : Login
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
