import Vue from 'vue'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'


import './assets/index.css'
import 'sweetalert2/dist/sweetalert2.min.css';

const app = createApp(App).use(router, axios).mount('#app')