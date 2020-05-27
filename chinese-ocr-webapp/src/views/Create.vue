<template>
    <div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
			<div class='col-span-1'>
				<Sidebar/>
			</div>
			<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 overflow-x-none overflow-y-auto' id='page-content'>
				<DeckGrid view='create'/>
			</div>
    </div>
</template>

<script>
import Sidebar from '../components/Sidebar'
import DeckGrid from '../components/DeckGrid'
export default {
	name: 'Create',
	components: {
		Sidebar,
		DeckGrid
	},
	props: {
		name: String
	}
}
</script>

<style scoped>

</style>