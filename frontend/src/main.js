import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import 'bootstrap'; // Import Bootstrap JavaScript
import '@fortawesome/fontawesome-free/css/all.css';
import store from './store'

createApp(App).use(store).use(router).mount('#app');
