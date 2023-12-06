<template>
  <header class="sticky-header">
     <nav class="navbar navbar-expand-lg navbar-light bg-light p-3">
       <a class="navbar-brand" href="#">To Do List</a>
       <button class="navbar-toggler" type="button" @click="toggleNavbar" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" :class="{ show: isNavbarOpen }" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="#">Inicio</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Agregar</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Mostrar Contacto</a>
          </li>
        </ul>
      </div>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <!-- Check if user is authenticated -->
          <li v-if="isAuthenticated" class="nav-item">
            <a class="nav-link" @click="logout">Salir</a>
          </li>
          <li v-if="isAuthenticated" class="nav-item">
            <a class="nav-link" href="#">Hola, {{ username }}</a>
          </li>
          <!-- If user is not authenticated, show login and register links -->
          <li v-else-if="!isAuthenticated">
            <router-link to="/login" class="nav-link">Login</router-link>
          </li>
          <li v-else>
            <router-link to="/register" class="nav-link">Register</router-link>
          </li>
        </ul>
      </div>
     </nav>
  </header>
 </template>
 
 <script>
 export default {
  data() {
     return {
       isNavbarOpen: false,
       isAuthenticated: true,
       username: "",
     };
  },
  methods: {
     toggleNavbar() {
       this.isNavbarOpen = !this.isNavbarOpen;
     },
     logout() {
      // Implement your logout logic here
      // For example, make an API call to log the user out on the server
      // and then update the component state accordingly
      this.isAuthenticated = false;
      this.username = "";
    },

  },
 };
 </script>
 
 <style lang="css" scoped>
 @import "@/styles/components/header.css";
 </style>
  