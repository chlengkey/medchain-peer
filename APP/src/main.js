import Vue from 'vue'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/index.css'
import axios from 'axios'

const app = createApp(App).use(router, axios).mount('#app')