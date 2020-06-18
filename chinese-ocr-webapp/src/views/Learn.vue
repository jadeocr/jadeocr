<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-20 p-8 md:px-8 overflow-x-none overflow-y-auto' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Learn</p>
			<div class="mt-8">
				<router-link :to='{ name: "create" }'
				class='btn bg-teal-500 font-normal opacity-87 text-white py-2 px-4 rounded'>
					Create Deck
				</router-link>
			</div>
			<p v-if='$store.state.formSuccess' class='text-green-500 text-base mt-1 -mb-1' id='successField'>{{ $store.state.formSuccess }}</p>
			<DeckList/>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
import DeckList from '../components/DeckList'
export default {
	name: 'Learn',
	components: {
		Sidebar,
		DeckList
	},
	props: {
		deckName: String
	},
	mounted() {
		
	}
}
</script>

<style scoped>

</style>