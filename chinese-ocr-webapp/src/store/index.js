import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router/index'

import * as firebase from 'firebase/app'
import 'firebase/auth'
import credentials from '../firebase/credentials'
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
    signInError: ''
  },
  mutations: {
    updateUser(state, payload) {
      state.userInfo.displayName = payload.user.displayName
      state.userInfo.email = payload.user.email
      state.userInfo.emailVerified = payload.user.emailVerified
      state.userInfo.photoURL = payload.user.photoURL
      state.userInfo.uid = payload.user.uid
      router.push('dashboard') // Redirects to the dashboard page
    },
    clearErrors(state) {
      state.signInError = ''
    },
    addError(state, msg) {
      state.signInError = msg
    },
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
    }
  },
  modules: {
  },
  getters: {
  }
})
