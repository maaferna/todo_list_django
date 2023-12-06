<template>
    <div class="container">
      <h1>Register</h1>
      <form @submit.prevent="register">
        <!-- Form fields for registration -->
        <button type="submit">Register</button>
      </form>
      <p>If you already have an account, <router-link to="/login">login here</router-link>.</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RegisterView',
    methods: {
      register() {
        // Implement your registration logic here
        // Make an API request to your Django backend to create a new user
        // Upon successful registration, you can redirect the user or perform other actions
      },
    },
  };
  </script>
  