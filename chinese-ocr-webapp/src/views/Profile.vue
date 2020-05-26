<template>
	<div class="grid grid-cols-1 md:grid-cols-4 opacity-87">
		<div class='col-span-1'>
			<Sidebar/>
		</div>
		<div class='col-span-1 ml-8 md:ml-0 mt-10 md:mt-20 p-8 md:px-8 mt-12 md:mt-0' id='page-content'>
			<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Profile</p>
			<div v-if='$store.state.signedIn' class="flex items-center mt-8 md:mt-12 text-base sm:text-sm md:text-md lg:text-lg xl:text-xl">
				<img class='w-12 md:w-16 rounded-full' :src='$store.state.userInfo.photoURL' alt="Profile Image">
				<p class="ml-8">{{ $store.state.userInfo.displayName }}</p>
			</div>
			<div v-else class="flex items-center mt-8 md:mt-12 text-base sm:text-sm md:text-md lg:text-lg xl:text-xl">
				<svg class="bi bi-person" width="2.5em" height="2.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
					<path fill-rule="evenodd" d="M13 14s1 0 1-1-1-4-6-4-6 3-6 4 1 1 1 1h10zm-9.995-.944v-.002.002zM3.022 13h9.956a.274.274 0 00.014-.002l.008-.002c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664a1.05 1.05 0 00.022.004zm9.974.056v-.002.002zM8 7a2 2 0 100-4 2 2 0 000 4zm3-2a3 3 0 11-6 0 3 3 0 016 0z" clip-rule="evenodd"/>
				</svg>
				<p class="ml-8 chinese">特尼</p>
			</div>
			<div>
				<div class="mt-20 text-red-500">
					<p class="opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">Danger Zone</p>
				</div>
				<div class='text-xs md:text-sm'>
					<div>
						<button @click='resetPassword'
						class='mt-8 btn-red opacity-87 text-white py-2 px-4 rounded'>
							Reset Password
						</button>
					</div>
					<div class="mt-6">
						<button @click='deleteAccount'
						class='btn-red opacity-87 text-white py-2 px-4 rounded'>
							Delete Account
						</button>
					</div>
				</div>
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
		resetPassword() {
			this.$store.dispatch('resetPassword')
		},
		deleteAccount() {
			alert('Add some warning and confirmation here')
			// this.$store.dispatch('deleteAccount')
		}
	}
}
</script>

<style scoped>

</style>