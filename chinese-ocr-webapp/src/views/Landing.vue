<template>
	<div id='landing'>
    <div id='intro' class='overflow-y-hidden md:overflow-y-auto'>
      <div class='slide container opacity-87 font-light grid grid-cols-1 lg:grid-cols-2 m-auto'>
        <div class='col-span-1'>
          <img src='../assets/title-image.png' alt='An image of the Chinese character 文, meaning "written language"'>
        </div>
        <div class='opacity-87 col-span-1 text-center lg:text-left -mt-16 md:-mt-24 lg:my-auto lg:ml-8'>
          <div class='mb-6 text-2xl md:text-3xl lg:text-4xl xl:text-5xl'>
            <p>Learn Chinese</p>
            <p class=''>without distractions.</p>
          </div>
          <GetStartedButton/>
        </div>
      </div>
      <div class='slide grid grid-rows-1'>
        <!-- Make it scroll down or something -->
        <div @click='scrollDown'
        class="row-span-1 m-auto opacity-75 mt-8 lg:-mt-8">
          <svg class="bi bi-chevron-down" width="3em" height="3em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 01.708 0L8 10.293l5.646-5.647a.5.5 0 01.708.708l-6 6a.5.5 0 01-.708 0l-6-6a.5.5 0 010-.708z" clip-rule="evenodd"/>
          </svg>
        </div>
      </div>
    </div>
    <div id='about' class='py-4'>
      <div class="mt-4 md:mt-12">
        <div class="text-lg md:text-2xl lg:text-3xl opacity-87 px-8 text-center">
          <p>The perfect language learning system didn't exist...</p>
          <p>until now.</p>
        </div>
        <div class="lg:mt-10 w-1/2 m-auto flex justify-center items-center
        grid grid-rows-8 grid-cols-1 lg:grid-cols-2 text-md md:text-xl">
          <div class="col-span-1">
            <Feature name='minimalist' :isFirstElement='true'
              title='Minimalist Design'
              body='
                hello world
              '
            />
            <Feature name='ocr' :isFirstElement='false'
              title='Handwriting OCR'
              body='
                hello world
              '
            />
            <Feature name='cloud' :isFirstElement='false'
              title='Cloud Sync'
              body='
                hello world
              '
            />
          </div>
          <div class="col-span-1 ">
            <Feature name='reactive' :isFirstElement='true'
              title='Reactive UI'
              body='
                hello world
              '
            />
            <Feature name='spaced-repetition' :isFirstElement='false'
              title='SRS Cards'
              body='
                hello world
              '
            />
            <Feature name='open-source' :isFirstElement='false'
              title='Open Source'
              body='
                hello world
              '
            />
          </div>
        </div>
      </div>
    </div>
    <!-- <div id="footer">
      <div class="text-center">
        Footer
      </div>
    </div> -->
	</div>
</template>

<script>
import GetStartedButton from '../components/GetStartedButton'
import Feature from '../components/Feature'
export default {
	name: 'Landing',
	components: {
    GetStartedButton,
    Feature
  },
  methods: {
    scrollDown() {
      document.querySelector('#about').scrollIntoView({ 
        behavior: 'smooth',
      })
    }
  }
}
</script>

<style scoped>
#about, #intro {
  height: 100vh;
}

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