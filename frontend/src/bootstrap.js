// src/bootstrap.js
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

import { createApp } from 'vue';
import App from './App.vue'; // Adjust the path if needed
import router from './router'; // Adjust the path if needed

const app = createApp(App);

app.use(router);

// Optionally, you can register BootstrapVue components here

app.mount('#app');
