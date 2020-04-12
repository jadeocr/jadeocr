<template>
  <div id="title">
    <img src="../assets/title-image.png" alt="An image of the Chinese character 文, meaning 'written language'">
    <div id="title-text">
      <span>
        <p>Learn Chinese.</p>
      </span>
      <span>
        <p>Without Distractions.</p>
      </span>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
#title{
  display: inline-block;
  box-sizing: border-box;
}
img{
  max-width: 33%;
  float: left;
  margin-left: 20%;
  margin-top: 2.5%;
}

#title-text{
  font-size: 1em;
  text-align: left;
  line-height: 0.5em;
  margin-top: 15%;
}

@media (min-width: 600px){
  #title-text{
    font-size: 1.5em;
    margin-top: 15%;
  }
}

@media (min-width: 900px){
  #title-text{
    font-size: 2em;
    margin-top: 15%;
  }
}

@media (min-width: 1200px){
  #title-text{
    font-size: 2.5em;
    margin-top: 15%;
  }
}

@media (min-width: 1800px){
  #title-text{
    font-size: 3em;
    margin-top: 15%;
  }
}
</style>