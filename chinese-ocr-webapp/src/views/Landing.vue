<template>
	<div>
			<Title/>
			<!-- Displays database properties -->
			<h1>{{ testDB }}</h1> 
	</div>
</template>

<script>
import Title from '../components/Title.vue'
import { db } from '../firebase/db.js'

export default {
	name: 'Landing',
	components: {
		Title
	},
	data(){
		return{
			testDB: ''
		}
	},
	mounted: function(){
		if (location.hostname === "localhost") { // Checks for local emulator
			db.settings({
				host: "localhost:3000",
				ssl: false
			})
		}

		db.collection('test-collection').doc('test-items').get()
		.then(doc => {
			if (!doc.exists) {
				console.log('No such document!');
			} else {
				this.testDB = ('Document data:', doc.data());
			}
		})
		.catch(err => {
			console.log('Error getting document', err);
		})

		db.collection('test-collection').doc('test-items').set({
			name: 'foo',
			age: 'bar'
		})
	}
}
</script>

<style>

</style>