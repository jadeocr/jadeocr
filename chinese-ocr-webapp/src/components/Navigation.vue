<template>
  <div id="#navigation" class="nav-container">
    <a href="#" id="nav-title">chinese-ocr</a>
    <a href="#" id="nav-login">log in</a>
    <a href="#" id="nav-signup">sign up</a>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.nav-container a{
  display: inline-block flex;
  padding-top: 2rem;
  padding-bottom: 2rem;
  text-decoration: none;
  color: #ffffff;
  opacity: 0.87;
  font-size: 1rem;
}

#nav-title{
  margin-left: 1.5rem;
  margin-right: 5rem;
  flex-grow: 3;
}

#nav-login{
  margin-right: 3rem;
  flex-grow: 1;
}

#nav-signup{
  margin-right: 1.5rem;
  flex-grow: 1;
}

@media (min-width: 600px) {
  #nav-title{
    margin-right: 18rem;
  }
}

@media (min-width: 900px) {
  .nav-container a{
    font-size: 1.25rem;
  }

  #nav-title{
    margin-right: 32.5rem;
  }
}

@media (min-width: 1200px) {
  .nav-container a{
    font-size: 1.25rem;
  }

  #nav-title{
    margin-right: 52.5rem;
  }
}

@media (min-width: 1800px) {
  .nav-container a{
    font-size: 1.5rem;
  }

  #nav-title{
    margin-right: 85rem;
  }

  #nav-login{
    margin-right: 5rem;
  }
}
</style>