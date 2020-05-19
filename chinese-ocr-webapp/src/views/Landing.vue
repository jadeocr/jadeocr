<template>
	<div id='landing'>
		<div class='slide container opacity-87 font-light grid grid-cols-1 md:grid-cols-2 m-auto'>
			<div class='col-span-1'>
        <img src='../assets/title-image.png' alt='An image of the Chinese character 文, meaning "written language"'>
			</div>
			<div class='opacity-87 col-span-1 text-center md:text-left my-auto md:ml-8'>
        <div class='mb-6 text-2xl md:text-3xl lg:text-4xl xl:text-5xl'>
          <p>Learn Chinese</p>
          <p class=''>without distractions.</p>
        </div>
				<GetStartedButton/>
			</div>
		</div>
    <div>
      <!-- V arrow glowing -->
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
.slide {
  animation: .75s slidedown;
}

@keyframes slidedown{
  from{
    margin-top: -5vh;
    opacity: 0;
  }
  to{
    margin-top: 0vh;
    opacity: .87;
  }
}
</style>