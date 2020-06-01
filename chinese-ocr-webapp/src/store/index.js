import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router/index'
import createPersistedState from 'vuex-persistedstate'

import firebase from 'firebase/app'
import credentials from '../firebase/credentials'
import 'firebase/auth'
import 'firebase/firestore'
firebase.initializeApp(credentials.firebaseConfig)
const auth = firebase.auth()
const db = firebase.firestore()

const $ = require('jquery')

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
    formError: '',
    formSuccess: '',
    numOfDecks: 0,
    decks: []
  },
  mutations: {
    updateUser(state, payload) {
      state.userInfo.displayName = payload.user.displayName
      state.userInfo.email = payload.user.email
      state.userInfo.emailVerified = payload.user.emailVerified
      state.userInfo.photoURL = payload.user.photoURL
      state.userInfo.uid = payload.user.uid,
      state.signedIn = true
      router.push('/dashboard/learn')
    },
    addError(state, msg) {
      state.formError = msg
    },
    addSuccess(state, msg) {
      state.formSuccess = msg
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
    },
    updateDecks(state, payload) {
      state.numOfDecks = payload.size
      state.decks = payload.docs
    }
  },
  actions: {
    signInWithGoogleAction({ commit }) {
      const provider = new firebase.auth.GoogleAuthProvider()
      auth.signInWithPopup(provider)
        .then(response => commit('updateUser', response))
        .catch(error => commit('addError', error.message))
    },
    signUpWithEmailAction({ commit }, credentials) {
      auth.createUserWithEmailAndPassword(credentials.email, credentials.password)
        .then(response => commit('updateUser', response))
        .catch(error => commit('addError', error.message))
    },
    signInWithEmailAction({ commit }, credentials) {
      auth.signInWithEmailAndPassword(credentials.email, credentials.password)
        .then(response => commit('updateUser', response))
        .catch(error => commit('addError', error.message))
    },
    signOutAction({ commit }) {
      auth.signOut()
        .then(commit('clearUserData'))
        .catch(error => console.log(error))
    },
    resetPassword(state, email) {
      if (state.signedIn && state.userInfo.uid) {
        auth.sendPasswordResetEmail(email)
          .catch(error => console.log(error))
      }
    },
    deleteAccount({ state }) {
      if (state.signedIn && state.userInfo.uid) {
        // TODO: Delete all user docs
        // TODO: Check perms
        auth.currentUser.delete()
          .catch(error => console.log(error))
      }
    },
    createDeck({ state, dispatch, commit }, payload) {
      if (state.signedIn && state.userInfo.uid) {
        let docRef = db.collection('decks').doc('user-decks').collection(state.userInfo.uid).doc(payload.name)
        docRef.get()
        .then(doc => {
          if (!doc.exists || (payload.method == 'edit')) {
            docRef.set(payload.deck, { merge: true })
              .then(commit('addError', ''))
              .then(router.push('/dashboard/decks'))
              .then(dispatch('getDecks'))
              .catch(error => console.log(error))          
          } else {
            commit('addError', 'A deck with this name already exists')
          }
        })
      }
    },
    showSuccess({ commit }, message) { // Fade for deck creation success message
      new Promise((resolve) => {
        commit('addSuccess', message)
        setTimeout(() => {
          $('#successField').fadeOut(1000, () => {
            commit('addSuccess', '')
            resolve()
          })
        }, 1000)
      })
        .catch(error => console.log(error))
    },
    getDecks({ state, commit }) {
      if (state.signedIn && state.userInfo.uid) {
        let decksRef = db.collection('decks').doc('user-decks').collection(state.userInfo.uid)
        decksRef.get()
          .then(snapshot => {
            commit('updateDecks', { 
              size: snapshot.size,
              docs: snapshot.docs.map(doc => doc.data())
            })
          })
          .catch(error => console.log(error))
      }
    },
    deleteDeck({ state,  dispatch }, name) {
      if (state.signedIn && state.userInfo.uid) {
        let docRef = db.collection('decks').doc('user-decks').collection(state.userInfo.uid).doc(name)
        docRef.delete()
          .then(router.push('/dashboard/decks'))
          .then(dispatch('getDecks'))
          .catch(error => console.log(error))
      }
    },
    getServerTime() {
      return firebase.firestore.Timestamp.now()
    }
  },
  modules: {
  },
  getters: {
  },
  plugins: [createPersistedState()]
})
