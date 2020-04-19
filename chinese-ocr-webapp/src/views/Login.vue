<template>
	<div>
		<div class='m-auto w-full max-w-xs mt-8 md:mt-10 lg:mt-12 xl:mt-26'>
			<form class='login-form bg-black shadow-md rounded px-8 pt-6 pb-8 mb-4 rounded-md'>
				<div class='mb-4'>
					<label class='block opacity-86 text-sm font-bold mb-2'>
						Email
					</label>
					<input v-model='email' class='shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 
					leading-tight focus:outline-none focus:shadow-outline' type='email' placeholder='alice@example.com'>
				</div>
				<div class='mb-6'>
					<label class='block opacity-86 text-sm font-bold mb-2'>
						Password
					</label>
					<input v-model='password' class='shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 
					leading-tight focus:outline-none focus:shadow-outline' type='password' placeholder='********'>
				</div>
				<div class='flex items-center justify-between'>
					<button @click='signInWithEmail'
					class='btn-purple opacity-86 text-white font-bold py-2 px-4 rounded' type='button'>
						Sign In
					</button>
					<button @click='signUpWithEmail'
					class='btn-purple opacity-86 text-white font-bold py-2 px-4 rounded' type='button'>
						Sign Up
					</button>
				</div>
			</form>
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
			password: ''
		}
	},
	methods: {
		signUpWithEmail: function() {
			firebase.auth().createUserWithEmailAndPassword(this.email.trim(), this.password.trim())
			.catch(function(error) {
				console.log(error.code)
				console.log(error.message)
			})
		},
		signInWithEmail: function(){
			firebase.auth().signInWithEmailAndPassword(this.email.trim(), this.password.trim())
			.catch(function(error) {
				console.log(error.code)
				console.log(error.message)
			})
		}
	}
}
</script>

<style scoped>
.btn-purple {
	background-color: #bb86fc;
	opacity: 0.6;
}

.btn-purple:hover {
	opacity: 0.5;
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