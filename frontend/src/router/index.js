import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomePage.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import TaskListComponent from '../components/TaskListComponent.vue'
import store from '../store'


const routes = [
 { path: '/', name: 'Home', component: Home },
 { path: '/login', name: 'Login', component: Login },
 { path: '/register', name: 'Register', component: Register },
 {
  path: '/api/v1/serializer_tasks/',
  name: 'SerializerTasks', 
  component: TaskListComponent,
},
];

const router = createRouter({
 history: createWebHistory(process.env.BASE_URL),
 routes,
});

router.beforeEach((to, from, next) => {
    console.log('Checking route:', to.name);
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
      console.log('User is not authenticated, redirecting to login');
      next({ name: 'Login' }); // Navigate to the Login route by name
    } else {
      console.log('User is authenticated or route does not require login');
      next();
    }
  });
  

export default router;
