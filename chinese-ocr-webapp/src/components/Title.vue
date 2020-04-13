<template>
  <div class="container">
    <div>
      <img src="../assets/title-image.png" alt="An image of the Chinese character 文, meaning 'written language'">
    </div>
    <div class="greeting">
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
.container{
  margin: auto;
  padding-top: 2.5vh;
  display: flex;
  flex-direction: column;
}

img{
  max-width: 100%;
}

.greeting{
  flex: 1;
  text-align: center;
  line-height: 5vh;
  font-size: 7vw;
  margin-top: -7.5vh;
}

</style>