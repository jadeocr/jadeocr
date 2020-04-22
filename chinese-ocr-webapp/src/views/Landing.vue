<template>
	<div>
		<div class='container max-w-none mt-1 sm:mt-2 md:mt-3 lg:mt-5 xl:mt-6'>
			<div class='col-1 opacity-87 mr-0 sm:-mr-2 md:-mr-3 lg:-mr-4 xl:-mr-5'>
				<img src='../assets/title-image.png' alt='An image of the Chinese character 文, meaning "written language"'>
			</div>
			<div class='opacity-87 col-2 text-base text-2xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl'>
				<p>Learn Chinese</p>
				<p class='mb-4'>without distractions.</p>
				<GetStartedButton/>
			</div>
		</div>
	</div>
</template>

<script>
import GetStartedButton from '../components/GetStartedButton'

export default {
	name: 'Landing',
	components: {
		GetStartedButton
	}
}
</script>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
}

.col-1{
  flex: 1;
  animation: 1.25s shiftopacity;
}

@keyframes shiftopacity {
  from{
    opacity: 0;
  }
  to{
    opacity: 0.87;
  }
}

.col-2{
  text-align: center;
  flex: 1;
  animation: 1.25s slidedown;
  margin-top: -6vh;
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
    align-items: center;
  }
  .col-2{
    text-align: left;
    margin-top: -8vh;
  }
}
</style>