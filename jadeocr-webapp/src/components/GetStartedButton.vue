<template>
	<div>
		<router-link :to='{ name: getStartedLink }'
		class='chinese btn bg-teal-500 btn mt-8 px-3 py-1 text-base 
		sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl rounded-md'>
			Get Started | 开始
		</router-link>
	</div>
</template>

<script>
export default {
	name: 'GetStartedButton',
	data() {
		return {
			getStartedLink: 'login'
		}
	},
	mounted() {
		if (this.$store.state.signedIn) this.getStartedLink = 'learn'
		else this.getStartedLink = 'login'
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
