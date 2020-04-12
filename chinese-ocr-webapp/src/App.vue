<template>
  <div id="app">
    <Navigation/>
  </div>
</template>

<script>
import Navigation from './components/Navigation.vue'

export default {
  name: 'App',
  components: {
    Navigation
  }
}
</script>

<style>
#app{
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: "Open Sans", sans-serif;
  font-style: normal;
  font-weight: 300;
  text-align: center;
  overflow: scroll;
  background-size: cover;
  background-color: #121212;
  color: #ffffff;
}
</style>
