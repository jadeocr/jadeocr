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
    <div class='slide grid grid-rows-1'>
      <!-- Make it scroll down or something -->
      <div class="row-span-1 m-auto opacity-75 mt-8 md:mt-0">
        <svg class="bi bi-chevron-down" width="3em" height="3em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 01.708 0L8 10.293l5.646-5.647a.5.5 0 01.708.708l-6 6a.5.5 0 01-.708 0l-6-6a.5.5 0 010-.708z" clip-rule="evenodd"/>
        </svg>
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