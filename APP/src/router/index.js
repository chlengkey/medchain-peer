import { createRouter, createWebHashHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import DaftarPasien from '@/views/DaftarPasien.vue'
import DataDokter from '@/views/DataDokter.vue'
import PeriksaPasien from '@/views/PeriksaPasien.vue'
import Pengaturan from '@/views/Pengaturan.vue'

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
  },
  {
    path : '/pasien/dataDokter',
    name : "Data Dokter",
    component : DataDokter
  },
  {
    path : '/pengaturan',
    name : "Pengaturan",
    component : Pengaturan
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
