<template>
  <div class="container">
     <h1>Login</h1>
     <form @submit.prevent="login">
       <label for="username">Username:</label>
       <input v-model="username" type="text" id="username" required>
       <label for="password">Password:</label>
       <input v-model="password" type="password" id="password" required>
       <button type="submit">Login</button>
     </form>
     <p>{{ error }}</p>
     <p>If you don't have an account, <router-link to="/sign-up">register here</router-link>.</p>
  </div>
 </template>
 
 <script>
 // import store from '../store';
 
 export default {
  name: 'LoginView',
  data() {
     return {
       username: '',
       password: '',
       error: '',
     };
  },
  methods: {
     async login() {
       try {
         // Simulate login logic
         await new Promise((resolve) => setTimeout(resolve, 1000));
         this.$store.dispatch('authenticate', true);
         this.$router.push({ name: 'Home' });
       } catch (error) {
         // Handle the error, e.g., show an error message to the user
         this.error = 'Incorrect username or password. Please try again.';
       }
     },
  },
 };
 </script>
  