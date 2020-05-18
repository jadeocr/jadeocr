<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='hidden md:block col-span-1'>
			<Sidebar/>
		</div>
		<div class="block md:hidden ml-8 mt-8">
			<button @click='expand'
			class='py-1 px-2 btn-purple opacity-87 hover:opacity-75 text-white rounded'>
				<svg class="bi bi-list" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
					<path fill-rule="evenodd" d="M2.5 11.5A.5.5 0 013 11h10a.5.5 0 010 1H3a.5.5 0 01-.5-.5zm0-4A.5.5 0 013 7h10a.5.5 0 010 1H3a.5.5 0 01-.5-.5zm0-4A.5.5 0 013 3h10a.5.5 0 010 1H3a.5.5 0 01-.5-.5z" clip-rule="evenodd"/>
				</svg>
			</button>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Profile</p>
			<div class="flex items-center w-32 mt-8 md:mt-12">
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
		expand() {

		}
	}
}
</script>

<style scoped>

</style>