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
/* Styling the background */
body{
  background-size: cover;
  background: #121212;
}

#app{
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: "Open Sans", sans-serif;
  font-weight: 300;
  text-align: center;
  overflow: scroll; /* might have to move to body section */
  color: #ffffff;
}
</style>
