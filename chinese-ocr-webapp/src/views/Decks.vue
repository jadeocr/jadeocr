<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 mt-12 md:mt-0 overflow-x-none overflow-y-auto' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Decks</p>
			<p v-if='$store.state.formSuccess' class='text-green-500 text-base mt-1 -mb-1' id='successField'>{{ $store.state.formSuccess }}</p>
			<div class="mt-8">
				<router-link :to='{ name: "create" }'
				class='btn btn-purple opacity-87 text-white py-2 px-4 rounded'>
					Add Deck
				</router-link>
			</div>
			<div v-if='$store.state.numOfDecks' class='mt-12 grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 font-normal text-center'>
				<div v-for='(n, i) in $store.state.numOfDecks' :key='i.key' class='w-3/5 mt-4 col-span-1'>
					<div class='bg-black rounded-md px-12 py-12 decklist'>
						<div class=''>
							{{ $store.state.decks[i].name }}
						</div>
						<div class='btn btn-blue opacity-87 text-white py-1 text-md mt-2 rounded w-full'>
							<router-link :to='{ path: `/review/${$store.state.decks[i].name}` }'>
								Learn
							</router-link>
						</div>
						<div class='mt-2'>
							<router-link :to='{ path: `/edit/${$store.state.decks[i].name}` }'>
								<svg class="bi bi-pencil-square" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
									<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456l-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
									<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
								</svg>
							</router-link>
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
	name: 'Decks',
	data() {
		return {
		}
	},
	components: {
		Sidebar
	},
	beforeCreate() {
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
	background-color: rgba(255,255,255,0.05);
	z-index: 2;
}
</style>