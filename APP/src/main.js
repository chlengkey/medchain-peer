import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/index.css'
import Axios from 'axios'

Vue.prototype.$http = Axios;
createApp(App).use(router).mount('#app')
