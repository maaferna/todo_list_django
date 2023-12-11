<template>
  <div class="container">
     <h1>Register</h1>
     <form @submit.prevent="register">
       <label for="username">Username:</label>
       <input v-model="username" type="text" id="username" required>
       <label for="password">Password:</label>
       <input v-model="password" type="password" id="password" required>
       <label for="password2">Confirm Password:</label>
       <input v-model="password2" type="password" id="password2" required>
       <button type="submit">Register</button>
     </form>
     <p>{{ error }}</p>
     <p>If you already have an account, <router-link to="/login">login here</router-link>.</p>
  </div>
 </template>
 
 <script>
 //import store from '../store';
 
 export default {
  name: 'SignUp',
  data() {
     return {
       username: '',
       password: '',
       password2: '',
       error: '',
     };
  },
  methods: {
     register() {
       if (this.password !== this.password2) {
         this.error = 'Passwords do not match. Please try again.';
       } else {
         // Simulate registration logic
         // ...
 
         // If the registration is successful, update the Vuex store
         this.$store.dispatch('authenticate', true);
 
         // Navigate to the Home page
         this.$router.push({ name: 'Home' });
       }
     },
  },
 };
 </script>
  