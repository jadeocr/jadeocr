<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-20 p-8 md:px-8 overflow-y-scroll page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Stats</p>
			<div class="mt-8 md:mt-10 opacity-87 text-sm lg:text-md xl:text-lg">
				<div>{{ $store.state.decks.length }} deck{{plural[1]}}</div>
				<div>{{ totalSeen.reduce((a, b) => a+b, 0) }} / {{ totalCards }} card{{plural[2]}} learned</div>
			</div>
			<div v-if='$store.state.numOfDecks' class='my-8 grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 text-center'>
				<div v-for='(n, i) in $store.state.numOfDecks' :key='i.key' class='mr-4 md:mr-12 mt-4 mb-8 col-span-1'>
					<div class='bg-black rounded-md px-12 py-12 decklist'>
						<div>
							<router-link id='edit-link' class="font-normal"
							:to='{ path: `/edit/${$store.state.decks[i].name}` }'>
								{{ $store.state.decks[i].name }}
							</router-link>
						</div>
						<div class="text-sm">
							<DueDate :untilDue='untilDue[i]' :color='dueInfoColor[i]' class="mt-3 mb-1"/>
							<p>{{ totalSeen[i] }} / {{ $store.state.decks[i].numOfWords }} cards learned</p>
							<p class='pt-2'> Easiness: {{ easinessAverage[i] }} </p>
						</div>
						<!-- TODO: Sort by due date, show stats -->
					</div>
				</div>
			</div>
			<div v-else>
				<CreateNewDeckMsg/>
			</div>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
import DueDate from '../components/DueDate'
import CreateNewDeckMsg from '../components/CreateNewDeckMsg'
import * as moment from 'moment'
export default {
    components: {
			Sidebar,
			DueDate,
			CreateNewDeckMsg
    },
    data () {
      return {
				totalCards: 0,
				totalSeen: [],
				plural: [[], 's', 's'],
				dueInfoColor: [],
				easinessAverage: [],
				untilDue: [],
      }
    },
    methods: {
			getDueDifference(due) {
				due = moment(due, 'YYYY-MM-DD')
				let now = moment(this.$store.state.serverTime.format('YYYY-MM-DD'), 'YYYY-MM-DD')
				return moment.duration(due.diff(now)).asDays()
			},
			dueInfo() {
				let dues = []
				for (let i = 0; i < this.$store.state.decks.length; i++) {
					for (let duedate in this.$store.state.decks[i].dueDates) {
						dues.push(this.getDueDifference(this.$store.state.decks[i].dueDates[duedate]))
					}
					this.untilDue.push(Math.min(...dues))
					if (this.untilDue[i] > 0) {
						this.dueInfoColor.push('text-green-300')
					} else {
						this.dueInfoColor.push('text-red-400')
					}
					dues = []
				}
			}
		},
		created() {
			this.$store.dispatch('getDecks')
			.then(this.$store.dispatch('getServerTime'))
			.then(() => {
				for (let i = 0; i < this.$store.state.decks.length; i++) {
					this.totalSeen.push(0)
					this.easinessAverage.push(
						(this.$store.state.decks[i].easiness.reduce((a, b) => Number(a)+Number(b)) / this.$store.state.decks[i].easiness.length).toFixed(1)
					)
					this.totalCards += this.$store.state.decks[i].numOfWords
					for (let j = 0; j <= this.$store.state.decks[i].repetitions.length; j++) {
						if (this.$store.state.decks[i].repetitions[j] > 0) this.totalSeen[i]++
					}
				}

				if (this.$store.state.decks.length == 1) this.plural[1] = ''
				if (this.totalCards == 1) this.plural[2] = ''
			})
			
		},
		mounted() {
			this.dueInfo()
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
	background-color: rgba(255,255,255,0.08);
	z-index: 2;
}

#edit-link:hover {
	opacity: 0.75;
}
</style>
