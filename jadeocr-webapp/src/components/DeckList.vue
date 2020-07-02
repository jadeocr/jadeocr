<template>
	<div id='deck-list'>
		<div v-if='$store.state.numOfDecks' class='mt-8 grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 font-normal text-center'>
			<div v-for='(n, i) in $store.state.numOfDecks' :key='i.key' class='mr-4 md:mr-12 mt-4 mb-8 col-span-1'>
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
					<DueDate :untilDue='$store.state.untilDue[i]' :color='$store.state.dueInfoColor[i]' class="mt-2 -mb-2"/>
				</div>
			</div>
		</div>
		<div v-else>
			<CreateNewDeckMsg/>
		</div>
	</div>
</template>

<script>
import DueDate from '../components/DueDate'
import CreateNewDeckMsg from '../components/CreateNewDeckMsg'
export default {
	name: 'DeckList',
	components: {
		DueDate,
		CreateNewDeckMsg
	},
	beforeCreate() {
	},
	mounted() {
		this.$store.commit('addError', '')
		this.$store.dispatch('getDecks')
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
	background-color: rgba(255,255,255,0.08);
	z-index: 2;
}

#edit-link {
	font-weight: 600;
}

#edit-link:hover {
	opacity: 0.75;
}
</style>
