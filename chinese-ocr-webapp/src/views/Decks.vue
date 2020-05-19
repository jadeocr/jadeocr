<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Decks</p>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
export default {
	name: 'Decks',
	components: {
		Sidebar
	}
}
</script>

<style scoped>

</style>