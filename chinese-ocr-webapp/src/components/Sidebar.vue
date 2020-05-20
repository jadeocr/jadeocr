<template>
	<div id='sidebar'>
		<div class='px-8 md:px-16 py-20 md:py-32 font-normal' id='sidebar-content'>
			<div class="mb-16">
				<router-link :to='{ name: "learn" }'>
					<div class="flex items-center hover:opacity-75">
						<svg class="bi bi-book" width="1.5em" height="1.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M3.214 1.072C4.813.752 6.916.71 8.354 2.146A.5.5 0 018.5 2.5v11a.5.5 0 01-.854.354c-.843-.844-2.115-1.059-3.47-.92-1.344.14-2.66.617-3.452 1.013A.5.5 0 010 13.5v-11a.5.5 0 01.276-.447L.5 2.5l-.224-.447.002-.001.004-.002.013-.006a5.017 5.017 0 01.22-.103 12.958 12.958 0 012.7-.869zM1 2.82v9.908c.846-.343 1.944-.672 3.074-.788 1.143-.118 2.387-.023 3.426.56V2.718c-1.063-.929-2.631-.956-4.09-.664A11.958 11.958 0 001 2.82z" clip-rule="evenodd"/>
							<path fill-rule="evenodd" d="M12.786 1.072C11.188.752 9.084.71 7.646 2.146A.5.5 0 007.5 2.5v11a.5.5 0 00.854.354c.843-.844 2.115-1.059 3.47-.92 1.344.14 2.66.617 3.452 1.013A.5.5 0 0016 13.5v-11a.5.5 0 00-.276-.447L15.5 2.5l.224-.447-.002-.001-.004-.002-.013-.006-.047-.023a12.582 12.582 0 00-.799-.34 12.96 12.96 0 00-2.073-.609zM15 2.82v9.908c-.846-.343-1.944-.672-3.074-.788-1.143-.118-2.387-.023-3.426.56V2.718c1.063-.929 2.631-.956 4.09-.664A11.956 11.956 0 0115 2.82z" clip-rule="evenodd"/>
						</svg>
						<p class="ml-5">Learn</p>
					</div>
				</router-link>
			</div>
			<div class="mb-16">
				<router-link :to='{ name: "decks" }'>
					<div class="flex items-center hover:opacity-75">
						<svg class="bi bi-files" width="1.5em" height="1.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M3 2h8a2 2 0 012 2v10a2 2 0 01-2 2H3a2 2 0 01-2-2V4a2 2 0 012-2zm0 1a1 1 0 00-1 1v10a1 1 0 001 1h8a1 1 0 001-1V4a1 1 0 00-1-1H3z" clip-rule="evenodd"/>
							<path d="M5 0h8a2 2 0 012 2v10a2 2 0 01-2 2v-1a1 1 0 001-1V2a1 1 0 00-1-1H5a1 1 0 00-1 1H3a2 2 0 012-2z"/>
						</svg>
						<p class="ml-5">Decks</p>
					</div>
				</router-link>
			</div>
			<div class="mb-16">
				<router-link :to='{ name: "stats" }'>
					<div class="flex items-center hover:opacity-75">
						<svg class="bi bi-graph-up" width="1.5em" height="1.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path d="M0 0h1v16H0V0zm1 15h15v1H1v-1z"/>
							<path fill-rule="evenodd" d="M14.39 4.312L10.041 9.75 7 6.707l-3.646 3.647-.708-.708L7 5.293 9.959 8.25l3.65-4.563.781.624z" clip-rule="evenodd"/>
							<path fill-rule="evenodd" d="M10 3.5a.5.5 0 01.5-.5h4a.5.5 0 01.5.5v4a.5.5 0 01-1 0V4h-3.5a.5.5 0 01-.5-.5z" clip-rule="evenodd"/>
						</svg>
						<p class="ml-5">Stats</p>
					</div>
				</router-link>
			</div>
			<div class="mb-12 md:mb-16">
				<router-link :to='{ name: "profile" }'>
					<div class="flex items-center hover:opacity-75">
						<svg class="bi bi-people-circle" width="1.5em" height="1.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path d="M13.468 12.37C12.758 11.226 11.195 10 8 10s-4.757 1.225-5.468 2.37A6.987 6.987 0 008 15a6.987 6.987 0 005.468-2.63z"/>
							<path fill-rule="evenodd" d="M8 9a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"/>
							<path fill-rule="evenodd" d="M8 1a7 7 0 100 14A7 7 0 008 1zM0 8a8 8 0 1116 0A8 8 0 010 8z" clip-rule="evenodd"/>
						</svg>
						<p class="ml-5">Profile</p>
					</div>
				</router-link>
			</div>
			<div>
				<button @click='signOut'
				class='btn btn-purple opacity-87 text-white py-2 px-4 rounded'>
					Sign Out
				</button>
			</div>
		</div>
		<div class="block md:hidden ml-8 mt-8">
			<button @click='collapse'
			class='py-1 px-2 btn-purple opacity-87 hover:opacity-75 text-white rounded'>
				<svg class="bi bi-list" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
					<path fill-rule="evenodd" d="M2.5 11.5A.5.5 0 013 11h10a.5.5 0 010 1H3a.5.5 0 01-.5-.5zm0-4A.5.5 0 013 7h10a.5.5 0 010 1H3a.5.5 0 01-.5-.5zm0-4A.5.5 0 013 3h10a.5.5 0 010 1H3a.5.5 0 01-.5-.5z" clip-rule="evenodd"/>
				</svg>
			</button>
		</div>
	</div>
</template>

<script>
var $ = require('jquery')
export default {
	name: 'Profile',
	data() {
		return {
		}
	},
	methods: {
		signOut() {
			this.$store.dispatch('signOutAction')
		},
		collapse() {
			let currPos = $('#sidebar-content').css('left')
			if (currPos == '0px') {
				$('#sidebar-content').css('left', '-300px')
				$('#page-content').css('width', '100vw')
				this.$store.commit('toggleSidebarState')
			} else {
				$('#sidebar-content').css('left', '0px')
				$('#page-content').css('width', 'calc(100vw - 300px)')
				this.$store.commit('toggleSidebarState')
			}
		}
	}
}
</script>

<style scoped>
#sidebar-content {
	position: fixed;
	left: 0px;
	width: 300px;
	-webkit-transition: left 0.3s ease;
	transition: left 0.3s ease;
}

@media(max-width: 640px) {
	#sidebar-content {
		left: -300px;
	}
}
</style>