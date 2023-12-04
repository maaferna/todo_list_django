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
     </nav>
  </header>
 </template>
 
 <script>
 export default {
  data() {
     return {
       isNavbarOpen: false,
     };
  },
  methods: {
     toggleNavbar() {
       this.isNavbarOpen = !this.isNavbarOpen;
     },
  },
 };
 </script>
 
 <style lang="css" scoped>
 @import "@/styles/components/header.css";
 </style>
  