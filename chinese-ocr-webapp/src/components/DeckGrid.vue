<template>
	<div id='deck-grid'>
		<div class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">
			<p v-if='view == "create"'>Create</p>
			<div v-else>
				<p>Edit</p>
				<p class="mt-2 text-lg lg:text-xl xl:text-2xl font-normal">{{ name }}</p>
			</div>
		</div>
		<div class='mt-6'>
			<div class="w-1/2 lg:w-1/4">
				<input v-model='deck.name' class="shadow appearance-none w-full py-2 px-2 text-gray-200 
				leading-tight focus:outline-none focus:shadow-outline-none" type="text" placeholder='Deck name'>
				<p v-if='$store.state.formError.length' class='text-red-300 text-sm mt-1 -mb-1'>{{ $store.state.formError }}</p>
			</div>
			<div class="w-4/5 lg:w-2/5 mt-4 mb-12">
				<input v-model='deck.description' class="shadow appearance-none w-full py-2 px-2 text-gray-200 
				leading-tight focus:outline-none focus:shadow-outline-none" type="text" placeholder='Description'>
				<div class="flex mt-3">
					<div class="text-xl mt-3 mr-3">
						Handwriting
					</div>
					<toggle-button class='mt-4 opacity-87 opacity-87' color='#4FD1C5' v-model="deck.ocr"/>
				</div>
			</div>
			<div class="mt-10 mb-6">
				<button @click='addWord("add")'
				class='btn bg-teal-500 opacity-87 text-white py-2 px-4 rounded mr-4'>
					<svg class="bi bi-plus" width="1.25em" height="1.25em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
						<path fill-rule="evenodd" d="M8 3.5a.5.5 0 01.5.5v4a.5.5 0 01-.5.5H4a.5.5 0 010-1h3.5V4a.5.5 0 01.5-.5z" clip-rule="evenodd"/>
						<path fill-rule="evenodd" d="M7.5 8a.5.5 0 01.5-.5h4a.5.5 0 010 1H8.5V12a.5.5 0 01-1 0V8z" clip-rule="evenodd"/>
					</svg>
				</button>
				<button @click='addWord("subtract")'
				class='btn btn-red opacity-87 text-white py-2 px-4 rounded mr-4'>
					<svg class="bi bi-dash" width="1.25em" height="1.25em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
						<path fill-rule="evenodd" d="M3.5 8a.5.5 0 01.5-.5h8a.5.5 0 010 1H4a.5.5 0 01-.5-.5z" clip-rule="evenodd"/>
					</svg>
				</button>
			</div>
			<div v-for='(n, i) in deck.numOfWords' :key='i.key'>
				<form>
					<div class="flex flex-wrap -mx-3 mb-6">
						<div class="w-1/3 lg:w-1/4 px-3">
							<input v-model='deck.cards[i].pinyin' class="shadow appearance-none w-full py-2 px-2 text-gray-200 
							leading-tight focus:outline-none focus:shadow-outline-none" type="text" :placeholder='(i+1) + ". " + placeholders[i%placeholders.length].front'>
						</div>
						<div class="w-1/3 lg:w-1/4 px-3">
							<input v-model='deck.cards[i].hanzi' class="shadow appearance-none w-full py-2 px-2 text-gray-200 
							leading-tight focus:outline-none focus:shadow-outline-none" type="text" :placeholder="placeholders[i%placeholders.length].back">
						</div>
						<div class="w-1/3 lg:w-1/4 px-3">
							<input v-model='deck.cards[i].definition' class="shadow appearance-none w-full py-2 px-2 text-gray-200 
							leading-tight focus:outline-none focus:shadow-outline-none" type="text" :placeholder="placeholders[i%placeholders.length].notes">
						</div>
					</div>
				</form>
			</div>
			<div class='mt-12'>
				<button @click='createDeck'
				class='btn btn-purple opacity-87 text-white py-2 px-4 rounded my-auto'>
					<p v-if='view == "create"'>Create Deck</p>
					<p v-else>Save Changes</p>
				</button>
			</div>
			<div v-if='view == "edit"' class='mt-8'>
				<button @click='deleteDeck'
				class='btn btn-red opacity-87 text-white py-2 px-4 rounded my-auto'>
					Delete Deck
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import { ToggleButton } from 'vue-js-toggle-button'
const sanitizer = require('sanitizer')
export default {
	name: 'DeckGrid',
	props: {
		view: String,
		name: String
	},
	components: {
		ToggleButton
	},
	data() {
		return {
			deck: {
				name: '',
				numOfWords: 3,			// Default when creating deck
				description: '',
				cards: [],
				ocr: false,
				dueDates: [],				// Used to show user when to review
				interval: [],				// In days, used to calculate dueDates
				repetitions: [],
				easiness: [],
				originalName: String
			},
			placeholders: [
				{
					front: 'huā',
					back: '花',
					notes: 'flower'
				},
				{
					front: 'flower',
					back: 'la flor',
					notes: 'N/A'
				},
				{
					front: 'flower',
					back: '꽃',
					notes: 'N/A'
				},
				{
					front: 'hana',
					back: '花',
					notes: 'flower'
				},
				{
					front: 'phool',
					back: 'फूल',
					notes: 'flower'
				},
				{
					front: 'zahra',
					back: 'زهرة',
					notes: 'flower'
				},
			]
		}
	},
	methods: {
		sanitize() {
			this.deck.name = sanitizer.escape(this.deck.name)
			this.deck.description = sanitizer.escape(this.deck.description)
			for (let card in this.deck.cards) {
				card = sanitizer.escape(card)
			}
		},
		loadDeck() {
			this.deck = this.$store.state.decks.find(obj => {
				return obj.name == this.name
			})
			this.originalName = this.deck.name
		},
		pushData(){
			this.deck.cards.push({
				pinyin: '',
				hanzi: '',
				definition: ''
			})
			this.deck.dueDates.push(this.$store.state.serverTime.format('YYYY-MM-DD'))
			this.deck.interval.push(1)
			this.deck.repetitions.push(0)
			this.deck.easiness.push(2.5)
		},
		spliceMetadata(index) {
			this.deck.cards.splice(index, 1)
			this.deck.dueDates.splice(index, 1)
			this.deck.interval.splice(index, 1)
			this.deck.repetitions.splice(index, 1)
			this.deck.easiness.splice(index, 1)
			this.deck.numOfWords--
		},
		resetDeck() {
			for(let i = 0; i < this.deck.numOfWords; i++) {
				this.pushData(today)
			}
			let today = this.$store.state.serverTime.format('YYYY-MM-DD')
			this.deck.ocr = false // Sets metadata
			this.deck.dueDates = Array.apply(null, Array(this.deck.numOfWords)).map(String.prototype.valueOf, today)
			this.deck.interval = Array.apply(null, Array(this.deck.numOfWords)).map(Number.prototype.valueOf, 1)
			this.deck.repetitions = Array.apply(null, Array(this.deck.numOfWords)).map(Number.prototype.valueOf, 0)
			this.deck.easiness = Array.apply(null, Array(this.deck.numOfWords)).map(Number.prototype.valueOf, 2.5) // Easiest
		},
		trimDeck() {
			this.sanitize()
			for(let i = 0; i < this.deck.numOfWords; i++) {
				if (!(this.deck.cards[i].pinyin || this.deck.cards[i].hanzi || this.deck.cards[i].definition)) {
					this.spliceMetadata(i)
				}
			}
		},
		createDeck() {
			this.trimDeck()
			this.$store.commit('addSuccess', '')
			this.$store.dispatch('createDeck', {
				method: this.view,
				originalName: this.originalName,
				name: this.deck.name,
				deck: JSON.parse(JSON.stringify(this.deck))
			})
				.then(() => {
					if (this.view == 'create') {
						this.$store.dispatch('showSuccess', 'Deck created successfully')
					} else {
						this.$store.dispatch('showSuccess', 'Deck edited successfully')
					}
				})
				.catch(error => console.log(error))
		},
		addWord(addSubtract) {
			if (addSubtract == 'add') {
				this.deck.numOfWords++
				this.pushData()
			} else {
				this.spliceMetadata(this.deck.numOfWords - 1)
			}
		},
		deleteDeck() {
			this.$store.commit('addSuccess', '')
			this.$store.dispatch('deleteDeck', this.deck.name)
				.then(this.$store.dispatch('showSuccess', 'Deck deleted successfully'))
				.then(this.$store.dispatch('showSuccess', ''))
		}
	},
	mounted() {
		this.$store.commit('addError', '')
		if (this.view == 'create') {
			this.resetDeck()
		} else {
			this.loadDeck()
		}
	},
	created(){
		this.$store.dispatch('getServerTime')
			.catch(error => console.log(error))
	},
	updated() {
		console.clear()
	}
}
</script>

<style scoped>
input {
	background-color: transparent;
	border-bottom: 2px solid rgba(255,255,255,0.4);
	transition: border-bottom 0.25s ease-in-out;
}
input:focus {
	border-bottom: 2px solid rgba(255,255,255,1);
}

</style>