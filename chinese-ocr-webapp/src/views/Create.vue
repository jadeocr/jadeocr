<template>
    <div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
			<div class='col-span-1'>
				<Sidebar/>
			</div>
			<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 overflow-x-none overflow-y-auto' id='page-content'>
				<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Create</p>
				<div class="mt-8">
					<button @click='addWord("add")'
					class='btn btn-teal opacity-87 text-white py-2 px-4 rounded mr-4'>
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
				<div class='mt-6'>
					<div class="w-1/2 md:w-1/4 mb-12">
						<input v-model='name' class="bg-gray-300 shadow appearance-none border rounded w-full py-2 px-4 text-gray-800 
						leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder='Deck name'>
						<p v-if='$store.state.formError.length' class='text-red-500 text-sm mt-1 -mb-1'>{{ $store.state.formError }}</p>
					</div>
					<div v-for='(n, i) in deck.numOfWords' :key='i.key' >
						<form>
							<div class="flex flex-wrap -mx-3 mb-6">
								<div class="w-1/3 md:w-1/5 px-3">
									<input v-model='deck.cards[i].pinyin' class="bg-gray-300 shadow appearance-none border rounded w-full py-3 px-4 text-gray-800 
									leading-tight focus:outline-none focus:shadow-outline" type="text" :placeholder='(i+1) + ".  huā"'>
								</div>
								<div class="w-1/3 md:w-1/5 px-3">
									<input v-model='deck.cards[i].hanzi' class="bg-gray-300 shadow appearance-none border rounded w-full py-3 px-4 text-gray-800 
									leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="花">
								</div>
								<div class="w-1/3 md:w-1/5 px-3">
									<input v-model='deck.cards[i].definition' class="bg-gray-300 shadow appearance-none border rounded w-full py-3 px-4 text-gray-800 
									leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="flower">
								</div>
							</div>
						</form>
					</div>
					<div class='mt-4'>
						<button @click='createDeck'
						class='btn btn-purple opacity-87 text-white py-2 px-4 rounded my-auto'>
							Create Deck
						</button>
					</div>
				</div>
			</div>
    </div>
</template>

<script>
import Sidebar from '../components/Sidebar'
export default {
	name: 'Create',
	data() {
		return {
			name: '',
			deck: {
				numOfWords: 6,
				cards: []
			}
		}
	},
	components: {
		Sidebar
	},
	methods: {
		resetDeck() {
			for(let i = 0; i < this.deck.numOfWords; i++) {
				this.deck.cards.push({
					pinyin: '',
					hanzi: '',
					definition: ''
				})
			}
		},
		createDeck() {
			this.$store.dispatch('createDeck', {
				name: this.name,
				deck: JSON.parse(JSON.stringify(this.deck))
			})
			.then(this.$store.dispatch('showSuccess'))
			.catch(error => console.log(error))
		},
		addWord(addSubtract) {
			if (addSubtract == 'add') {
				this.deck.numOfWords++
				this.deck.cards.push({
					pinyin: '',
					hanzi: '',
					definition: ''
				})
			} else {
				this.deck.numOfWords--
				this.deck.cards.pop()
			}
		}
	},
	created(){
		this.resetDeck()
	}
}
</script>

<style scoped>
#page-content {
	height: 80vh;
}
</style>