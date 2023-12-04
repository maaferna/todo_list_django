<template>
    <Header />
    <main>
      <div class="container">
        <p>Some main section</p>
      </div>
    </main>
    <Footer />
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
  
  <style lang="css" scoped>
  @import "@/styles/base.css";
  </style>
  