<template>
	<div id='deck-list'>
		<div v-if='$store.state.numOfDecks' class='mt-8 grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 font-normal text-center'>
				<div v-for='(n, i) in $store.state.numOfDecks' :key='i.key' class='mr-4 md:mr-12 mt-4 mb-8	 col-span-1'>
					<div class='bg-black rounded-md px-12 py-12 decklist'>
						<div>
							<router-link id='edit-link' class="font-normal"
							:to='{ path: `/edit/${$store.state.decks[i].name}` }'>
								{{ $store.state.decks[i].name }}
							</router-link>
						</div>
						<router-link :to='{ path: `/review/${$store.state.decks[i].name}` }'>
							<div class='btn btn-purple opacity-87 text-white py-1 text-sm mt-2 rounded w-full'>
								Learn
							</div>
						</router-link>
						<div class="mt-3 -mb-3 text-sm font-light" v-if='view == "learn"' :class="dueInfoColor[i]">
							<span v-if="untilDue[i] >= 0">Due in</span> 
							<span v-else>Overdue by</span>
							{{ Math.abs(untilDue[i]) }}
							<span v-if='untilDue[i] == 1'>day</span>
							<span v-else>days</span>
						</div>
						<!-- TODO: Sort by due date -->
					</div>
				</div>
			</div>
	</div>
</template>

<script>
import * as moment from 'moment'
export default {
	name: 'DeckList',
	props: {
		view: String
	},
	data() {
		return {
			dueInfoColor: [],
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
	beforeCreate() {
	},
	mounted() {
		this.$store.commit('addError', '')
		this.$store.dispatch('getServerTime')
		.then(this.$store.dispatch('getDecks'))
		.then(this.dueInfo())
	}
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap');

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