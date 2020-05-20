<template>
    <div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
			<div class='col-span-1'>
				<Sidebar/>
			</div>
			<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 mt-12 md:mt-0' id='page-content'>
				<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Create</p>
				<div class='mt-8'>
					<!-- TODO: Make prettier, make scroll work, +/- icons -->
					<button @click='addWord'
					class='btn btn-purple opacity-87 text-white py-2 px-4 rounded mr-4'>
						Add Word
					</button>
					<button @click='createDeck'
					class='btn btn-purple opacity-87 text-white py-2 px-4 rounded'>
						Create Deck
					</button>
				</div>
				<div class='mt-8 relative overflow-y-scroll'>
					<div v-for='i in numOfWords' :key='i.key' class="flex">
						<form>
							<div class="flex flex-wrap -mx-3 mb-6">
								<div class="w-1/2 px-3">
									<input class="bg-gray-300 shadow appearance-none border rounded w-full py-3 px-4 text-gray-800 
									leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="wén">
								</div>
								<div class="w-1/2 px-3">
									<input class="bg-gray-300 shadow appearance-none border rounded w-full py-3 px-4 text-gray-800 
									leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="文">
								</div>
							</div>
						</form>
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
			numOfWords: 9,
		}
	},
	components: {
		Sidebar
	},
	methods: {
		createDeck() {
			console.log('yee')
		},
		addWord() {
			this.numOfWords ++
		}
	}
}
</script>

<style scoped>
</style>