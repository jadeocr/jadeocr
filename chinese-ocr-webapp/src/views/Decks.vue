<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-20 p-8 md:px-8 overflow-x-none overflow-y-auto' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Decks</p>
			<div class="mt-8">
				<router-link :to='{ name: "create" }'
				class='btn btn-teal font-normal opacity-87 text-white py-2 px-4 rounded'>
					Add Deck
				</router-link>
			</div>
			<DeckList view='decks'/>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
import DeckList from '../components/DeckList'
export default {
	name: 'Decks',
	data() {
		return {
		}
	},
	components: {
		Sidebar,
		DeckList
	}
}
</script>

<style scoped>

</style>