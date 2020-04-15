<template>
  <div class="container max-w-none mt-1 sm:mt-2 md:mt-3 lg:mt-5 xl:mt-6">
    <div class="col-1 mr-0 sm:-mr-2 md:-mr-3 lg:-mr-4 xl:-mr-5">
      <img
        src="../assets/title-image.png"
        alt="An image of the Chinese character 文, meaning 'written language'"
      />
    </div>
    <div
      class="col-2 text-base text-2xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl"
    >
      <p>Learn Chinese</p>
      <p>without distractions.</p>
      <a
        class="btn bg-purple-500 hover:bg-purple-600 mt-5 px-3 py-1 
      text-base sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl rounded-lg"
        href="/"
      >
        Get Started | 开始
      </a>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.btn {
  animation: 3s btnopacity;
}

@keyframes btnopacity {
  from {
    opacity: 0;
  }
  to {
    opacity: 0.87;
  }
}
.container {
  display: flex;
  flex-direction: column;
}

.col-1 {
  flex: 1;
  animation: 1.25s shiftopacity;
  opacity: 0.87;
}

@keyframes shiftopacity {
  from {
    opacity: 0;
  }
  to {
    opacity: 0.87;
  }
}

.col-2 {
  text-align: center;
  flex: 1;
  animation: 1.25s slidedown;
  margin-top: -8vh;
  opacity: 0.87;
}

@keyframes slidedown {
  from {
    margin-top: -20vh;
    opacity: 0;
  }
  to {
    margin-top: -8vh;
    opacity: 0.87;
  }
}

@media (min-width: 600px) {
  .container {
    flex-direction: row;
    align-items: center;
  }
  .col-2 {
    text-align: left;
  }
}
</style>
