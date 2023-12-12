<template>
  <div class="main mt-4">
    <div class="container border p-3 mb-3 mt-3 bg-light text-dark">
      <div class="row mb-4 text-center">
        <div class="col">
          <h1>Login</h1>
        </div>
      </div>
      <div class="container mb-4">
        <form @submit.prevent="submitForm">
          <div class="row mb-4">
            <div class="col-md-2 text-md-right col-md-auto">
              <label for="username">Username:</label>
            </div>
            <div class="col">
              <input v-model="username" type="text" id="username" required class="form-control">
            </div>
          </div>

          <div class="row mb-4">
            <div class="col-md-2 text-md-right">
              <label for="password">Password:</label>
            </div>
            <div class="col-md-4">
              <input v-model="password" type="password" id="password" required class="form-control">
            </div>
          </div>
          <div class="row text-center">
            <div class="col">
              <button type="submit" class="button-submit">Sign Up</button>
            </div>
          </div>
        </form>
      </div>
      <div v-if="errors.length" class="row mb-4">
        <div class="col">
          <div class="alert alert-danger" role="alert">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>
        </div>
      </div>
      <div class="row text-center">
        <div class="col">
          <p>If you already have an account, <router-link to="/login">login here</router-link>.</p>
        </div>
      </div>
    </div>
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
     async submitForm() {
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
  