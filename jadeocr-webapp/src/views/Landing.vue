<template>
	<div id='landing'>
    <div id='intro' class='h-screen'>
      <div class='container m-auto font-light title-container slide opacity-87 grid grid-cols-1 lg:grid-cols-2'>
        <div class='col-span-1'>
          <img src='../assets/title-image.png' alt='An image of the Chinese character 文, meaning "written language"'>
        </div>
        <div class='-mt-16 text-center opacity-87 col-span-1 lg:text-left md:-mt-24 lg:my-auto lg:ml-8'>
          <div class='mb-6 text-2xl md:text-3xl lg:text-4xl xl:text-5xl'>
            <p>Learn languages</p>
            <p class=''>without distractions.</p>
          </div>
          <GetStartedButton/>
        </div>
      </div>
      <div class='slide grid grid-rows-1'>
        <div @click='scrollDown' id='scroll-cue'
        class="m-auto mt-8 opacity-75 row-span-1 lg:-mt-8 hoverlink">
          <svg class="bi bi-chevron-down" width="3em" height="3em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 01.708 0L8 10.293l5.646-5.647a.5.5 0 01.708.708l-6 6a.5.5 0 01-.708 0l-6-6a.5.5 0 010-.708z" clip-rule="evenodd"/>
          </svg>
        </div>
      </div>
    </div>
    <div id='about' class='py-4'>
      <div class="mt-4 md:mt-12">
        <div class="px-8 text-lg text-center md:text-2xl lg:text-3xl opacity-87">
          <p>The perfect language learning system didn't exist...</p>
          <p>until now.</p>
        </div>
        <div class='px-3 mt-6 text-sm text-center md:text-lg lg:text-xl opacity-87'>
          <div>
            Learn languages with 
            <a href="https://en.wikipedia.org/wiki/Spaced_repetition" target="_blank" class="font-normal hoverlink">spaced repetition</a>
            flashcards
          </div>
          <p>and practice writing with built-in handwriting recognition.</p>
        </div>
        <div class="flex items-center justify-center w-1/2 m-auto lg:mt-10 grid grid-rows-8 grid-cols-1 lg:grid-cols-2 text-md md:text-lg">
          <div class="col-span-1 lg:pr-8">
            <Feature name='minimalist' :isFirstElement='true'
              title='Minimalist Design'
              body="
                A modern, simple design inspired by Material Dark 
                makes jadeocr fun and intuitive.
              "
            />
            <Feature name='ocr' :isFirstElement='false'
              title='Handwriting OCR'
              body='
                Computer vision delivers powerful optical character recognition 
                to help you practice writing.
              '
            />
            <Feature name='cloud' :isFirstElement='false'
              title='Cloud Sync'
              body='
                Jadeocr safely stores your decks in the cloud so you 
                can review no matter where you are.
              '
            />
          </div>
          <div class="col-span-1 lg:pl-8">
            <Feature name='reactive' :isFirstElement='true'
              title='Reactive UI'
              body="
                Vue.js powers jadeocr's snappy experience, making 
                learning new languages a joy.
              "
            />
            <Feature name='spaced-repetition' :isFirstElement='false'
              title='SRS Cards'
              body='
                Spaced repetition allows you to learn more efficiently 
                and promotes long-term retention.
              '
            />
            <Feature name='open-source' :isFirstElement='false'
              title='Open Source'
              body='
                In the open-source spirit, the
                code is public on GitHub. Thus,  
                jadeocr will remain free, forever.
              '
            />
          </div>
        </div>
      </div>
    </div>
    <div class="footer mt-24">
    <div class="mt-24 footer">
      <div id="footer-content" class='py-8 text-xs lg:text-sm'>
        <div class="text-center grid grid-cols-1 lg:grid-cols-2 opacity-87">
          <div class="col-span-1 w-1/2 m-auto text-center">
          <div class="w-1/2 m-auto text-center col-span-1">
            <p>
              This project is licensed under the 
              <a href='https://github.com/TanayB11/jadeocr/blob/master/LICENSE' target="_blank" class='font-normal hoverlink'>
                MIT License.
              </a>
            </p>
          </div>
          <!-- Make 2 more cols on small displays -->
          <div class="col-span-1 w-1/2 m-auto mt-4 lg:mt-0 text-center font-normal">
          <div class="w-1/2 m-auto mt-4 font-normal text-center col-span-1 lg:mt-0">
              <div class='col-span-1'>
                <div>
                  <a href='https://github.com/TanayB11/jadeocr' target="_blank" class="hoverlink">GitHub</a>
                </div>
                <div>
                  <a href="https://github.com/TanayB11/jadeocr#Donations" target="_blank" class="hoverlink">Donate</a>
                </div>
              </div>
              <div class="col-span-1">
                <div>
                  <a href='/terms' target="_blank" class="hoverlink">Terms</a>
                </div>
                <div>
                  <a href='mailto: devs@jadeocr.com' class="hoverlink">Contact</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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
.hoverlink:hover {
  opacity: 0.60;
}

.slide {
  animation: .75s slidedown;
}

#scroll-cue {
  animation: pulse 3s 5s ease-in-out infinite;
}

@keyframes pulse {
  50% {
    transform: scale(.8);
  }

  100% {
    transform: none;
  }
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

/* To deal with weird landscape bug on phones */
@media (max-width: 800px) and (orientation:landscape) {
  #intro {
    height: 200vh;
    margin-bottom: 8rem;
  }
}
</style>
