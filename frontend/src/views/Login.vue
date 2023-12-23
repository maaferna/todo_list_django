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
            <div class="col">
              <input v-model="password" type="password" id="password" required class="form-control">
            </div>
          </div>
          <div class="row text-center">
            <div class="col">
              <button type="submit" class="submitButton">Sign Up</button>
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
 import axios from 'axios';

 export default {
  name: 'LoginView',
  data() {
     return {
       username: '',
       password: '',
       errors: [],
     }
  },
  mounted() {
    document.title = 'Log In | To-Do'
  },
  methods: {
    async submitForm() {
            axios.defaults.headers.common["Authorization"] = "";

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("http://127.0.0.1:8000/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
  },
 };
 </script>
  