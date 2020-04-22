<template>
	<div>
		<div class='m-auto w-full max-w-xs mt-8 md:mt-10 lg:mt-12 xl:mt-26'>
			<form class='login-form bg-black shadow-md rounded px-8 pt-6 pb-8 mb-4 rounded-md' @submit='checkForm'>
				<div class='mb-4'>
					<label class='block opacity-86 text-sm font-bold mb-2'>
						Email
					</label>
					<input v-model='email' class='bg-gray-300 shadow appearance-none border rounded w-full py-2 px-3 text-gray-800 
					leading-tight focus:outline-none focus:shadow-outline' type='text' placeholder='alice@example.com'>
				</div>
				<div class='mb-6'>
					<label class='block opacity-86 text-sm font-bold mb-2'>
						Password
					</label>
					<input v-model='password' class='bg-gray-300 shadow appearance-none border rounded w-full py-2 px-3 text-gray-800 mb-3 
					leading-tight focus:outline-none focus:shadow-outline' type='password' placeholder='********'>
					<p v-if='errors.length' class='text-red-500 text-sm mt-1 -mb-1'>{{ errors }}</p>
				</div>
				<div class='flex items-center justify-between'>
					<button @click='signInWithEmail'
					class='btn-purple opacity-86 text-white font-bold py-2 px-4 rounded' type='submit'>
						Sign In
					</button>
					<button @click='signUpWithEmail'
					class='btn-purple opacity-86 text-white font-bold py-2 px-4 rounded' type='submit'>
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
import * as firebase from 'firebase/app'
import 'firebase/auth'
import credentials from '../firebase/credentials'
firebase.initializeApp(credentials.firebaseConfig)

export default {
	name: 'Login',
	components: {
		GoogleButton
	},
	data() {
		return {
			email: '',
			password: '',
			errors: []
		}
	},
	methods: {
		checkForm: function(e) {
			this.errors = []

			if ((!this.email) || (!this.password)){
				this.errors.push('Please complete all fields ')
			} else if (!this.validEmail(this.email)) {
				this.errors.push('Invalid Email')
			} else {
				this.error = []
			}

			this.errors = this.errors.toString()
			this.email = ''
			this.password = ''
			e.preventDefault()
		},
		validEmail: function (email) {
			const re = /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
			return re.test(email)
		},
		signUpWithEmail: function() {
			if (!this.errors.length) {
				firebase.auth().createUserWithEmailAndPassword(this.email.trim(), this.password.trim())
				.catch(function(error) {
					console.log(error.code)
					console.log(error.message)
				})
				this.error = []
			}
		},
		signInWithEmail: function() {
			if (!this.errors.length) {
				firebase.auth().signInWithEmailAndPassword(this.email.trim(), this.password.trim())
				.catch(function(error) {
					console.log(error.code)
					console.log(error.message)
				})
				this.error = []			
			}
		}
	}
}
</script>

<style scoped>
.btn-purple {
	background-color: #bb86fc;
	opacity: 0.87;
}

.btn-purple:hover {
	opacity: 0.75;
}

.opacity-86{
	opacity: .86;
}

.login-form {
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255,255,255,0.05);
	z-index: 2;
}
</style>