<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 mt-12 md:mt-0' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Profile</p>
			<div v-if='$store.state.signedIn' class="flex items-center w-32 mt-8 md:mt-12">
				<img class='w-12 md:w-16 rounded-full' :src='$store.state.userInfo.photoURL' alt="Profile Image">
				<p class="ml-8 text-base sm:text-sm md:text-md lg:text-lg xl:text-xl">{{ $store.state.userInfo.displayName }}</p>
			</div>
		</div>
	</div>
</template>

<script>
import Sidebar from '../components/Sidebar'
export default {
	name: 'Profile',
	data() {
		return {
			
		}
	},
	components: {
		Sidebar
	},
	methods: {

	}
}
</script>

<style scoped>

</style>