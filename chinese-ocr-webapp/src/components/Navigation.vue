<template>
  <div
    class="container text-base sm:text-lg md:text-2xl lg:text-3xl xl:text-4xl"
  >
    <nav>
      <a href="/" id="nav-title">chinese-ocr</a>
    </nav>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.container {
  margin: auto;
  width: 50%;
  text-align: center;
  padding-top: 2vh;
}

#nav-title {
  text-decoration: none;
  color: #ffffff;
  opacity: 0.5;
  animation: 1.25s shiftopacity;
}

@keyframes shiftopacity {
  from {
    opacity: 0;
  }
  to {
    opacity: 0.5;
  }
}

#nav-title:hover {
  opacity: 0.87;
}
</style>
