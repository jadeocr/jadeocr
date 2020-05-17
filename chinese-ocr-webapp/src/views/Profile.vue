<template>
	<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class="col-span-1"></div>
		<div class='col-span-4 mt-16'>
			<p class="text-base text-md sm:text-lg md:text-xl lg:text-2xl xl:text-3xl font-normal">
				Profile
			</p>
			<div class="flex items-center w-32 mt-12">
				<img :src='$store.state.userInfo.photoURL' alt="Profile Image" class='rounded-full'>
				<p class="ml-12 text-base text-sm sm:text-md md:text-lg lg:text-xl xl:text-2xl">{{ $store.state.userInfo.displayName }}</p>
			</div>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
export default {
	name: 'Profile',
	components: {
		Sidebar
	}
}
</script>

<style scoped>

</style>