import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router/index'

import * as firebase from 'firebase/app'
import 'firebase/auth'
import credentials from '../firebase/credentials'
// import db from '../firebase/db'
firebase.initializeApp(credentials.firebaseConfig)

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userInfo: {
      displayName: null,
      email: null,
      emailVerified: null,
      photoURL: null,
      uid: null,
    },
    signedIn: false,
    signInError: '',
  },
  mutations: {
    updateUser(state, payload) {
      state.userInfo.displayName = payload.user.displayName
      state.userInfo.email = payload.user.email
      state.userInfo.emailVerified = payload.user.emailVerified
      state.userInfo.photoURL = payload.user.photoURL
      state.userInfo.uid = payload.user.uid,
      state.signedIn = true
      router.push('dashboard/learn')
    },
    clearErrors(state) {
      state.signInError = ''
    },
    addError(state, msg) {
      state.signInError = msg
    },
    clearUserData(state) {
      state.userInfo.displayName = null
      state.userInfo.email = null
      state.userInfo.emailVerified = null
      state.userInfo.photoURL = null
      state.userInfo.uid = null
      state.signedIn = false
      router.push('/')
    },
    toggleSidebarState(state) {
      state.sidebarExpanded = !state.sidebarExpanded
    }
  },
  actions: {
    signInWithGoogleAction({ commit }) {
      var provider = new firebase.auth.GoogleAuthProvider()
      firebase.auth().signInWithPopup(provider)
        .then(response => commit('updateUser', response))
        .catch(error => commit('addError', error.message))
    },
    signUpWithEmailAction({ commit }, credentials) {
      firebase.auth().createUserWithEmailAndPassword(credentials.email, credentials.password)
        .then(response => commit('updateUser', response))
        .catch(error => commit('addError', error.message))
    },
    signInWithEmailAction({ commit }, credentials) {
      firebase.auth().signInWithEmailAndPassword(credentials.email, credentials.password)
        .then(response => commit('updateUser', response))
        .catch(error => commit('addError', error.message))
    },
    signOutAction({ commit }) {
      firebase.auth().signOut()
      .then(commit('clearUserData'))
      .catch(error => console.log(error))
    },
    resetPassword() {
      firebase.auth().sendPasswordResetEmail(this.state.userInfo.email)
      .catch(error => console.log(error))
    },
    deleteAccount() {
      firebase.auth().currentUser.delete()
      .catch(error => console.log(error))
    },
    createDeck() {
      // if user not has collection then create one, else create document
    }
  },
  modules: {
  },
  getters: {
  }
})
