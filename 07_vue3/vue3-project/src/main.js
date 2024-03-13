import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

// createApp(App).mount('#app')

// router 사용시 명시
createApp(App).use(router).mount('#app')
