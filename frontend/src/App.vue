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
import axios from 'axios';

export default {
  name: 'App',
  components: {
  Header, 
  Footer,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted(){

  },
  computed: {

  }
}
</script>

<style lang="css" scoped>
@import "@/styles/base.css";
</style>
