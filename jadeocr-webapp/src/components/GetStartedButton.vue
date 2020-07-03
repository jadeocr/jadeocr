<template>
	<div>
		<router-link :to='{ name: changeRoute }'
		class='chinese btn bg-teal-500 btn mt-8 px-3 py-1 text-base 
		sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl rounded-md'>
			Get Started | 开始
		</router-link>
	</div>
</template>

<script>
export default {
	name: 'GetStartedButton',
	computed: {
		changeRoute() {
			if (this.$store.state.signedIn) {
				return "learn"
			} else {
				return "login"
			}
		}
	}
}
</script>

<style scoped>
.btn{
  animation: 3s btnopacity;
  /* background-color: #bb86fc; */
}

.btn:hover {
	opacity: 0.75;
}

@keyframes btnopacity{
  from{
    opacity: 0;
  }
  to{
    opacity: 1;
  }
}
</style>
