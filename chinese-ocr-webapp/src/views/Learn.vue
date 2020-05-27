<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 mt-12 md:mt-0' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Learn</p>
			<div v-if='$store.state.numOfDecks' class='mt-8 grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 font-normal text-center'>
				<div v-for='(n, i) in $store.state.numOfDecks' :key='i.key' class='w-4/5 mt-4 col-span-1'>
					<div class='bg-black rounded-md px-12 py-12 decklist'>
						<div>
							{{ $store.state.decks[i].name }}
						</div>
						<router-link :to='{ path: `/review/${$store.state.decks[i].name}` }'>
							<div class='btn btn-purple opacity-87 text-white py-1 text-md mt-2 rounded w-full'>
								Learn
							</div>
						</router-link>
						<div>
							<!-- TODO: Sort by due date, show stats -->
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
export default {
	name: 'Learn',
	components: {
		Sidebar
	},
	props: {
		deckName: String
	},
		beforeCreate() {
		this.$store.commit('addError', '')
		this.$store.dispatch('getDecks')
	}
}
</script>

<style scoped>
#page-content {
	height: 80vh;
}

.decklist {
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255,255,255,0.07);
	z-index: 2;
}
</style>