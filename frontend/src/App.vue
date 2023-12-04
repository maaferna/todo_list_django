<template>
   <div id="app">
    <Home />
  </div>
</template>

<script>
import Home from './views/HomePage.vue';

export default {
  name: 'App',
  components: {
    Home
  }
}
</script>

<style lang="css" scoped>
@import "@/styles/base.css";
</style>
