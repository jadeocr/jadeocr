<template>
	<div>
		<router-link :to='{ name: "login" }'
		class='btn mt-8 px-3 py-1 text-base sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl rounded-lg'>
			Get Started | 开始
		</router-link>
	</div>
</template>

<script>
export default {
	name: 'GetStartedButton'
}
</script>

<style scoped>
.btn{
  animation: 3s btnopacity;
  background-color: #bb86fc;
  opacity: 0.87;
}

.btn:hover {
	opacity: 0.75;
}

@keyframes btnopacity{
  from{
    opacity: 0;
  }
  to{
    opacity: 0.87;
  }
}
</style>