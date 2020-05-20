<template>
    <div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
			<div class='col-span-1'>
				<Sidebar/>
			</div>
			<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 mt-12 md:mt-0' id='page-content'>
				<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Create</p>
			</div>
    </div>
</template>

<script>
import Sidebar from '../components/Sidebar'
export default {
	name: 'Create',
	components: {
		Sidebar
	}
}
</script>

<style scoped>

</style>