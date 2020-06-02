<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 mt-12 md:mt-0 overflow-y-scroll' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Stats</p>
			<div class="w-1/2 chart mt-8 opacity-87">
				<line-chart :options='options' :chart-data="datacollection"></line-chart>
			</div>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
import LineChart from '../chart/linechart'

 export default {
    components: {
			Sidebar,
			LineChart
    },
    data () {
      return {  //TODO: Change font color, add more charts
				datacollection: {},
				datasets: [],
				labels: ['Number of Cards'],
				options: {
						scales: {
								yAxes: [{
										ticks: {
												beginAtZero: true
										}
								}]
						},
						defaultFontColor: '#fff',
						responsive: true
				},
				chartBg: '#bb86fc',
      }
    },
    methods: {
			formatData() {
				for (let i = 0; i < this.$store.state.decks.length; i++) {
					this.datasets.push({
						label: this.$store.state.decks[i].name,
						data: [this.$store.state.decks[i].numOfWords],
						backgroundColor: this.chartBg
					})
				}
			},
      fillData () {
        this.datacollection = {
					labels: this.labels,
          datasets: this.datasets
        }
      }
		},
		created() {
			this.$store.dispatch('getDecks')
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
</style>