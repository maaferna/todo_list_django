<template>
  <div class="main mt-4 mb-4">
    <div class="container border p-3 mb-3 mt-3 bg-light text-dark">
      <div class="row mb-4 text-center">
        <div class="col">
          <h1>Sign-Up</h1> 
          <hr>
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
            <div class="col-md-2 text-md-right">
              <label for="password2">Confirm Password:</label>
            </div>
            <div class="col">
              <input v-model="password2" type="password" id="password2" required class="form-control">
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
import axios from 'axios';
import { Toast } from 'bootstrap';
//import { type } from 'os';
import store from '../store';
 
 export default {
  name: 'SignUp',
  data() {
     return {
       username: '',
       password: '',
       password2: '',
       errors: []
     };
  },
  methods: {
     submitForm() {
      this.errors = [];
      if (this.password !== this.password2) {
         this.errors.push('Passwords do not match. Please try again.');
       } 
      if (this.password === ''){
        this.errors.push('The password is too short');
      }
      if (this.username === '') {
        this.errors.push('The username is missing');
      }
      if (!this.errors.length) {
        this.$router.push({ name: 'Home' });
        const formData = {
          username: this.username,
          password: this.password
        }
        axios
          .post("http://127.0.0.1:8000/api/v1/users/", formData)
          .then(response => {
            if (response.status === 200 || response.status === 201) {
              // Extract user data from response
              const userData = response.data;

              // Store user data (e.g., using Vuex)
              store.commit('setUser', userData);

              // Display success message
              Toast({
                message: 'Account created, welcome!',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              });

              // Redirect to desired page
              this.$router.push('/login');
            } else {
              console.error('Error creating user:', response);
            }
          })
          .catch(error => {
            if(error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
              console.log(JSON.stringify(error.response.data))
            }
            else if (error.message) {
              this.errors.push("Something went wrong. Please try again")
              console.log(JSON.stringify(error))
            }
          });
        }
      },
    },
  }
 </script>
