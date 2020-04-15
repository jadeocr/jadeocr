<template>
  <div class="container">
    <div class="col-1">
      <img src="../assets/title-image.png" alt="An image of the Chinese character 文, meaning 'written language'">
    </div>
    <div class="col-2">
      <p>Learn Chinese</p>
      <p>without distractions.</p>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
img{
  max-width: 100%;
}

.container{
  display: flex;
  flex-direction: column;
}

.col-1{
  width: 100%;
  flex: 1;
  animation: 1.25s shiftopacity;
}

@keyframes shiftopacity {
  from{
    opacity: 0;
  }
  to{
    opacity: 0.87
  }
}

.col-2{
  width: 100%;
  text-align: center;
  flex: 1;
  line-height: 4vh;
  font-size: 8vw;
  margin-top: -8vh;
  animation: 1.25s slidedown;
  opacity: .87;
}

@keyframes slidedown{
  from{
    margin-top: -20vh;
    opacity: 0;
  }
  to{
    margin-top: -8vh;
    opacity: .87;
  }
}

@media (min-width: 600px){
  .container{
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .col-2{
    text-align: left;
    font-size: 4vw;
  }
}

@media (min-width: 900px){
  .container{
    margin-top: 0vh;
  }
}
</style>