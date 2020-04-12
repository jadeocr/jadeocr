<template>
  <div id="#navigation" class="nav-container">
    <nav>
      <ul>
        <a href="#" id="nav-title">chinese-ocr</a>
        <a href="#" id="nav-login">log in</a>
        <a href="#" id="nav-signup">sign up</a>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.nav-container a{
  display: inline-block;
  padding-top: 2em;
  padding-bottom: 2em;
  text-decoration: none;
  color: #ffffff;
  opacity: 0.87;
  font-size: 1em;
}

#nav-title{
  margin-left: 1.5em;
  margin-right: 5em;
}

#nav-login{
  margin-right: 5em;
}

#nav-signup{
  margin-right: 1.5em;
}

@media (min-width: 600px) {
  #nav-title{
    margin-right: 15em;
  }
}

@media (min-width: 900px) {
  .nav-container a{
    font-size: 1.25em;
  }

  #nav-title{
    margin-right: 20em;
  }
}

@media (min-width: 1200px) {
  .nav-container a{
    font-size: 1.25em;
  }

  #nav-title{
    margin-right: 38em;
  }
}

@media (min-width: 1800px) {
  .nav-container a{
    font-size: 1.5em;
  }

  #nav-title{
    margin-right: 50em;
  }

  #nav-login{
    margin-right: 5em;
  }
}
</style>