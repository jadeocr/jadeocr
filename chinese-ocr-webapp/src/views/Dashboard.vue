<template>
	<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 opacity-87">
		<div>
			<Sidebar/>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
export default {
	name: 'Dashboard',
	components: {
		Sidebar
	}
}
</script>

<style scoped>

</style>