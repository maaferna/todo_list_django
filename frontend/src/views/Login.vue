<template>
    <div>
      <Header />
      <br>
      <div class="container">
        <h1>Login</h1>
        <form @submit.prevent="login">
          <label for="username">Username:</label>
          <input v-model="username" type="text" id="username" required>
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required>
          <button type="submit">Login</button>
        </form>
        <p>If you don't have an account, <router-link to="/register">register here</router-link>.</p>
      </div>
      <Footer />
    </div>
  </template>
  
  <script>
  import Header from '../components/partials/HeaderSection.vue';
import Footer from '../components/partials/FooterSection.vue';
  
export default {
    name: 'LoginView',
    data() {
      return {
        username: 'Marco',
        password: '',
      };
    },
    methods: {
      async login() {
        try {
          // Send a request to your server to log in the user
          // ...

          // If the login is successful, update the Vuex store
          this.$store.dispatch('authenticate', true);

          // Navigate to the Home page
          this.$router.push({ name: 'Home' });
        } catch (error) {
          // Handle the error, e.g., show an error message to the user
          // ...
        }
      },

      logout() {
      // Simulate logout logic
      this.isAuthenticated = false;
        },
    },
    components: {
    Header,
    Footer,
    },
    mounted() {
  },
  };
  </script>
  