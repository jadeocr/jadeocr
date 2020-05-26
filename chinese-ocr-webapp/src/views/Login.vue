<template>
	<div>
		<div class='m-auto w-full max-w-xs mt-10 font-normal'>
			<form class='login-form bg-black shadow-md rounded px-8 pt-6 pb-8 mb-4 rounded-md' @submit.prevent=''>
				<div class='mb-4'>
					<label class='block opacity-87 text-sm mb-2'>
						Email
					</label>
					<input v-model='email' class='bg-gray-300 shadow appearance-none border rounded w-full py-2 px-3 text-gray-800 
					leading-tight focus:outline-none focus:shadow-outline' type='text' placeholder='alice@example.com'>
				</div>
				<div class='mb-6'>
					<label class='block opacity-87 text-sm mb-2'>
						Password
					</label>
					<input v-model='password' class='bg-gray-300 shadow appearance-none border rounded w-full py-2 px-3 text-gray-800 mb-3 
					leading-tight focus:outline-none focus:shadow-outline' type='password' placeholder='********'>
					<button @click='resetPassword' class='text-xs text-blue-400 hover:text-blue-500'>Forgot Password?</button>
					<p v-if='$store.state.formError.length' class='text-red-500 text-sm mt-1'>{{ $store.state.formError }}</p>
					<p v-if='$store.state.formSuccess' class='text-green-500 text-sm mt-1 -mb-1' id='successField'>{{ $store.state.formSuccess }}</p>
				</div>
				<div class='flex items-center justify-between'>
					<button @click='signInWithEmail'
					class='btn-purple opacity-87 text-white py-2 px-4 rounded'>
						Sign In
					</button>
					<button @click='signUpWithEmail'
					class='btn-purple opacity-87 text-white py-2 px-4 rounded'>
						Sign Up
					</button>
				</div>
			</form>
			<GoogleButton/>
		</div>
	</div>
</template>

<script>
import GoogleButton from '../components/GoogleButton'

export default {
	name: 'Login',
	components: {
		GoogleButton
	},
	data() {
		return {
			email: '',
			password: '',
		}
	},
	methods: {
		checkForm() {
			this.$store.commit('addError', '')
			if ((!this.email) || (!this.password)){
				this.$store.commit('addError', 'Please complete all fields')
			} else if (!this.validEmail(this.email)) {
				this.$store.commit('addError', 'Invalid email')
			}
		},
		clearFields() {
			this.email = ''
			this.password = ''
		},
		validEmail(email) {
			const re = /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,4}))$/
			return re.test(email)
		},
		signUpWithEmail() {
			this.checkForm()
			if (!this.$store.state.formError) {
        this.$store.dispatch('signUpWithEmailAction', { 
          email: this.email.trim(), 
          password: this.password.trim()
				})
			}
			this.clearFields()
		},
		signInWithEmail() {
			this.checkForm()
			if (!this.$store.state.formError) {
				this.$store.dispatch('signInWithEmailAction', { 
          email: this.email.trim(), 
          password: this.password.trim()
				})
			}
			this.clearFields()
		},
		resetPassword() {
			if (!this.email) {
				this.$store.commit('addError', 'Please enter your email')
			} else if (!this.validEmail(this.email)) {
				this.$store.commit('addError', 'Invalid email')
			} else {
				this.$store.commit('addError', '')
				this.$store.dispatch('resetPassword', this.email.trim())
					.then(this.$store.dispatch('showSuccess', 'Sent a password reset email'))
			}
		}
	}
}
</script>

<style scoped>
.login-form {
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255,255,255,0.05);
	z-index: 2;
}
</style>