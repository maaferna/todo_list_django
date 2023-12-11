<template>
  <div id="app">
    <Header />
    <router-view></router-view> 
    <Footer />
  </div>
</template>

<script>
import Header from './components/partials/HeaderSection.vue';
import Footer from './components/partials/FooterSection.vue';

export default {
  name: 'App',
  components: {
  Header, 
  Footer,
  }
}
</script>

<style lang="css" scoped>
@import "@/styles/base.css";
</style>
