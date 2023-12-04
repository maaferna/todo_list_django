<template>
    <div>
      <Header />
      <!-- Your main content goes here -->
      <Footer />
    </div>
  </template>
  
  <script>
  import Header from '../components/partials/HeaderSection.vue';
  import Footer from '../components/partials/FooterSection.vue';
  
  export default {
    components: {
      Header,
      Footer,
    },
    // Component logic goes here
  };
  </script>
  
  <style scoped>
    /* Component-specific styles go here */
  </style>
  