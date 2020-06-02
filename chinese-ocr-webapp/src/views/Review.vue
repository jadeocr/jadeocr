<template>
	<div id='review'>
		<div class="w-1/2 m-auto text-center lg:text-left mt-12 md:mt-16 
		opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">
			{{ name }}
		</div>
		<div class='w-3/5 lg:w-1/2 m-auto mt-8 text-center'>	
			<div
			class='bg-black rounded-md px-12 py-24 md:py-32 card'>
				{{ deck.cards[dueIndices[currentIndex]].pinyin }}
			</div>
			<div class="mt-10">
				<div class="md:w-2/3 mt-4 m-auto flex items-center justify-between opacity-87">
					<div class='btn btn-red rounded-md px-4 py-3'
						@click='cardCheck("wrong")'
					>
						<svg class="bi bi-x" width="1.25em" height="1.25em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
							<path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
						</svg>
					</div>
					<div class="btn btn-blue mx-auto rounded-md py-2 px-4 text-sm font-normal">
						{{ reviewedButton }}
					</div>
					<div class='btn btn-cyan rounded-md px-4 py-3'
						@click='cardCheck("correct")'
					>
						<svg class="bi bi-check2" width="1.25em" height="1.25em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
						</svg>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import * as moment from 'moment'

export default {
	name: 'Review',
	data() {
		return {
			deck: Object,
			untilDue: [],
			dueIndices: [], // Refers to which cards to review
			currentIndex: 0, // Iterator for dueIndices
			serverTime: null
		}
	},
	props: {
		name: String
	},
	computed: {
		reviewedButton() {
			if (this.deck.ocr) {
				return 'Check Writing'
			} else {
				return 'Flip Card'
			}
		}
	},
	methods: {
		calculateSuperMemo2(cardIndex, quality) { // Thanks to Suragch on Stack Overflow!
			let repetitions = this.deck.repetitions[cardIndex]
			let easiness = this.deck.easiness[cardIndex]
			let interval = this.deck.interval[cardIndex]

			let repetitionFormula = easiness + 0.1 - (5.0 - quality) * (0.08 + (5.0 - quality) * 0.02)
			easiness = Math.max(1.3, repetitionFormula)

			if (quality == 0) { // Modified for only 2 quality buttons (is either 0 or 5)
				this.deck.repetitions[cardIndex] = 0
			} else {
				this.deck.repetitions[cardIndex]++
			}

			if (repetitions <= 1) {
				this.deck.interval[cardIndex] = 1;
			} else if (repetitions == 2) {
				this.deck.interval[cardIndex] = 6;
			} else {
				this.deck.interval[cardIndex] = Math.round(interval * easiness);
			}

			// TODO: Check practice date calculation
			// TODO: Add enhancements
			this.deck.dueDates[cardIndex] = this.$store.state.serverTime.add(this.deck.interval[cardIndex], 'days')
		},
		submitFinished() {
			console.log('fin')
			console.log(this.deck)
			this.$store.dispatch('createDeck', {
				method: 'edit',
				name: this.name,
				deck: JSON.parse(JSON.stringify(this.deck))
			})
		},
		cardCheck(correctness) {
			if (correctness == 'correct') {
				this.calculateSuperMemo2(this.dueIndices[this.cardIndex], 5)
			} else {
				this.calculateSuperMemo2(this.dueIndices[this.cardIndex], 0)
			}
			this.currentIndex == this.dueIndices.length ? this.submitFinished() : this.currentIndex ++
		},
		getDueDifference(due) {
			due = moment(due, 'YYYY-MM-DD')
			let now = moment(this.$store.state.serverTime.format('YYYY-MM-DD'), 'YYYY-MM-DD') // Today's date
			return moment.duration(due.diff(now)).asDays()
		},
		randInt(min, max) {
			return Math.floor(Math.random() * (max - min) + min)
		},
		chooseCards() {
			for (let i = 0; i < this.deck.numOfWords; i++) {
				this.untilDue.push(this.getDueDifference(this.deck.dueDates[i]))
			}
			let mostDue = Math.min(...this.untilDue)
			for (let i = 0; i < this.untilDue.length; i++) { // Check for all cards due today
				if (this.untilDue[i] == mostDue) this.dueIndices.push(i)
			}
		},
	},
	mounted() {
		this.$store.dispatch('getServerTime')
		.then(() => {
			this.deck = this.$store.state.decks.find(obj => {
				return obj.name == this.name
			})
			this.chooseCards() // TODO: Testing this and all called functions
		})
	},
	updated() {
		console.clear()
	}
}
</script>

<style scoped>
.card {
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255,255,255,0.07);
	z-index: 2;
}

.btn:hover {
	opacity: 0.75;
}

.btn-cyan {
	background-color: #26a69a;
	opacity: 0.87;
}

.btn-review-red {
	background-color: #ff7043;
	opacity: 0.87;
}
</style>