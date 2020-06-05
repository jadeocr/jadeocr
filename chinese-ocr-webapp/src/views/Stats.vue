<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 mt-12 md:mt-0 overflow-y-scroll' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Stats</p>
			<!-- <div hidden class="w-1/2 chart mt-8 opacity-87">
				<line-chart :options='options' :chart-data="datacollection"></line-chart>
			</div> -->
			<div class="mt-8 md:mt-10 opacity-87 text-sm lg:text-md xl:text-lg">
				<h1 class="mb-0 md:mb-2 text-lg lg:text-xl xl:text-2xl font-normal">General</h1>
				<p>{{ $store.state.decks.length }} decks</p>
				<p>{{ totalCards }} cards</p>
				<p>{{ totalSeen }} cards seen</p>
			</div>
			<div v-if='$store.state.numOfDecks' class='my-8 grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 font-normal text-center'>
				<div v-for='(n, i) in $store.state.numOfDecks' :key='i.key' class='w-4/5 mt-4 col-span-1'>
					<div class='bg-black rounded-md px-12 py-12 decklist'>
						<div>
							<router-link id='edit-link' class="font-normal"
							:to='{ path: `/edit/${$store.state.decks[i].name}` }'>
								{{ $store.state.decks[i].name }}
							</router-link>
						</div>
						<p>{{ $store.state.decks[i].numOfWords }} cards</p>
						<!-- TODO: Sort by due date, show stats -->
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
// import LineChart from '../chart/linechart'

 export default {
    components: {
			Sidebar,
			// LineChart
    },
    data () {
      return {  //TODO: Change font color, add more charts
				// datacollection: {},
				// datasets: [],
				// labels: ['Number of Cards'],
				// options: {
				// 		scales: {
				// 				yAxes: [{
				// 						ticks: {
				// 								beginAtZero: true
				// 						}
				// 				}]
				// 		},
				// 		defaultFontColor: '#fff',
				// 		responsive: true
				// },
				// chartBg: '#bb86fc',
				totalCards: 0,
				totalSeen: 0,
      }
    },
    methods: {
	// 		formatData() {
	// 			for (let i = 0; i < this.$store.state.decks.length; i++) {
	// 				this.datasets.push({
	// 					label: this.$store.state.decks[i].name,
	// 					data: [this.$store.state.decks[i].numOfWords],
	// 					backgroundColor: this.chartBg
	// 				})
	// 			}
	// 		},
    //   fillData () {
    //     this.datacollection = {
	// 				labels: this.labels,
    //       datasets: this.datasets
    //     }
    //   }
		},
		created() {
			this.$store.dispatch('getDecks')
			for (let i = 0; i < this.$store.state.decks.length; i++) {
				this.totalCards += this.$store.state.decks[i].numOfWords
				for (let repetition in this.$store.state.decks[i].repetitions) {
					if (repetition > 0) this.totalSeen++
				}
			}
		},
		mounted() {
			this.formatData()
      this.fillData()
    }
  }
</script>

<style scoped>
.chart {
	height: 50vh;
}

.decklist {
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255,255,255,0.07);
	z-index: 2;
}

#edit-link {
	font-weight: 600;
}

#edit-link:hover {
	opacity: 0.75;
}
</style>