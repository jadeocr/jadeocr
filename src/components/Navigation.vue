<template>
  <div id="#navigation">
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
#navigation{
  align-self: center;
}

nav a{
  display: inline-block;
  padding-top: 2em;
  padding-bottom: 2em;
  text-decoration: none;
  color: #ffffff;
  opacity: 0.87;
  font-size: 1em;
}

#nav-title{
  margin-right: 5%;
}

#nav-login{
  margin-right: 3%;
}

@media (min-width: 600px){
  nav a{
    font-size: 1.25em;
  }
}

@media (min-width: 900px){
  nav a{
    font-size: 1.5em;
  }
}
</style>