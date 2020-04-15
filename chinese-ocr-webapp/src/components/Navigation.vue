<template>
  <div class="container">
    <nav>
      <a href="#" id="nav-title">chinese-ocr</a>
    </nav>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.container{
  margin: auto;
  width: 50%;
  text-align: center;
  padding-top: 2vh;
  font-size: 5vw;
}

#nav-title{
  text-decoration: none;
  color: #ffffff;
  opacity: 0.5;
  animation: 1.25s shiftopacity;
}

@keyframes shiftopacity {
  from{
    opacity: 0;
  }
  to{
    opacity: 0.5;
  }
}

#nav-title:hover{
  opacity: 0.87;
}

@media(min-width: 600px){
  .container{
    font-size: 4vw;  
  }
}

@media(min-width: 900px){
  .container{
    font-size: 3vw;  
  }
}

@media(min-width: 1200px){
  .container{
    font-size: 2.5vw;  
  }
}

@media(min-width: 1800px){
  .container{
    font-size: 2vw;  
  }
}
</style>