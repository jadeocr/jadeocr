<template>
  <div>
    <button @click='signIn'
      class='btn bg-purple-500 hover:bg-purple-600 mt-8 px-3 py-1 
      text-base sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl rounded-lg'
      >
        Log In
      </button>
  </div>
</template>

<script>
import * as firebase from 'firebase'
import credentials from '../firebase/credentials'
firebase.initializeApp(credentials.firebaseConfig)

export default {
  name: 'Login',
  data() {
    return {
    }
  },
  methods: {
    signIn: function() {
      var provider = new firebase.auth.GoogleAuthProvider()
      firebase.auth().signInWithRedirect(provider)
    },
    signOut: function() {
      firebase.auth().signOut()
    },
    getUsername: function() {
      this.username = firebase.auth().currentUser.displayName
    }
  }
}
</script>

<style>
            
</style>