// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import Bootstrap from './bootstrap';

createApp(App).use(router).use(Bootstrap).mount('#app');



