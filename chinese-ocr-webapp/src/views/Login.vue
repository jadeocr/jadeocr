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
			<div>
					<button @click='signInWithGoogle'
					class='m-auto w-full bg-white text-gray-600 opacity-86 hover:bg-gray-200 mt-8 px-3 py-1 
					text-base sm:text-md md:text-lg lg:text-xl xl:text-2xl rounded-md'
					>
						<div>
							<span class='google-button__icon w-6 h-6 mr-3 -mt-1'>
								<svg viewBox='0 0 366 372' xmlns='http://www.w3.org/2000/svg'><path d='M125.9 10.2c40.2-13.9 85.3-13.6 125.3 1.1 22.2 8.2 
								42.5 21 59.9 37.1-5.8 6.3-12.1 12.2-18.1 18.3l-34.2 34.2c-11.3-10.8-25.1-19-40.1-23.6-17.6-5.3-36.6-6.1-54.6-2.2-21 4.5-40.5 
								15.5-55.6 30.9-12.2 12.3-21.4 27.5-27 43.9-20.3-15.8-40.6-31.5-61-47.3 21.5-43 60.1-76.9 105.4-92.4z' 
								id='Shape' fill='#EA4335'/>
									<path d='M20.6 102.4c20.3 15.8 40.6 31.5 61 47.3-8 23.3-8 49.2 0 72.4-20.3 15.8-40.6 31.6-60.9 47.3C1.9 232.7-3.8 189.6 4.4 
									149.2c3.3-16.2 8.7-32 16.2-46.8z' id='Shape' fill='#FBBC05'/><path d='M361.7 151.1c5.8 32.7 4.5 66.8-4.7 98.8-8.5 29.3-24.6 
									56.5-47.1 77.2l-59.1-45.9c19.5-13.1 33.3-34.3 37.2-57.5H186.6c.1-24.2.1-48.4.1-72.6h175z' id='Shape' fill='#4285F4'/>
									<path d='M81.4 222.2c7.8 22.9 22.8 43.2 42.6 57.1 12.4 8.7 26.6 14.9 41.4 17.9 14.6 3 29.7 2.6 44.4.1 14.6-2.6 28.7-7.9 
									41-16.2l59.1 45.9c-21.3 19.7-48 33.1-76.2 39.6-31.2 7.1-64.2 7.3-95.2-1-24.6-6.5-47.7-18.2-67.6-34.1-20.9-16.6-38.3-38-50.4-62 
									-15.7 40.6-31.5 60.9-47.3z' fill='#34A853'/>
								</svg>
							</span>		
							<span>
								Sign in with Google
							</span>
						</div>
					</button>
				</div>
		</div>
	</div>
</template>

<script>
import * as firebase from 'firebase/app'
import 'firebase/auth'
import credentials from '../firebase/credentials'
firebase.initializeApp(credentials.firebaseConfig)

export default {
	name: 'Login',
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
		},
		signInWithGoogle: function() {
			var provider = new firebase.auth.GoogleAuthProvider()
			firebase.auth().signInWithPopup(provider)
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

.google-button__icon {
	display: inline-block;
	vertical-align: middle;
}
</style>