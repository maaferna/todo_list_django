import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomePage.vue';
import Login from '../views/Login.vue';
import SignUp from '../views/SignUp.vue';
import TaskListComponent from '../components/TaskListComponent.vue'
import store from '../store'


const routes = [
 { path: '/', name: 'Home', component: Home },
 { path: '/login', name: 'Login', component: Login },
 { path: '/sign-up', name: 'SignUp', component:SignUp },
 {
  path: '/api/v1/serializer_tasks/',
  name: 'SerializerTasks', 
  component: TaskListComponent,
  },
  {
    path: '/api/v1/tasks/create', // Define the desired URL for creating a new task
    name: 'CreateTask', // Define a unique name for the route
    component: TaskListComponent, // You can choose the appropriate component here
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
