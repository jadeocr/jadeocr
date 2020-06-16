import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router/index'
import createPersistedState from 'vuex-persistedstate'

import * as moment from 'moment'

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
    decks: [],
    serverTime: null,
    untilDue: [], // For displaying due dates on deck list
    dueInfoColor: [],
    dueDifference: 0
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
    },
    updateServerTime(state, payload) {
      state.serverTime = moment.utc(moment.unix(payload.seconds))
    },
    getDueDifference(state, due) {
      due = moment(due, 'YYYY-MM-DD')
      let now = moment(state.serverTime.format('YYYY-MM-DD'), 'YYYY-MM-DD')
      state.dueDifference = moment.duration(due.diff(now)).asDays()
    },
    updateUntilDue(state, payload) {
      state.untilDue = payload
    },
    clearDues(state) { // THIS IS A MUTATION
      state.untilDue = []
      state.dueInfoColor = []
    },
    updateDues(state, payload) {
      if (payload.option == 'untilDue') {
        state.untilDue.push(payload.data)
      } else {
        state.dueInfoColor.push(payload.data)
      }
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
      auth.sendPasswordResetEmail(email)
        .catch(error => console.log(error))
    },
    deleteAccount({ state }) {
      if (state.signedIn && state.userInfo.uid) {
        auth.currentUser.delete()
          .then(router.push('/'))
          .then(this.$store.commit('addError', ''))
          .catch(error => console.log(error))
      }
    },
    createDeck({ state, commit }, payload) {
      if (state.signedIn && state.userInfo.uid) {
        let docRef = db.collection('decks').doc('user-decks').collection(state.userInfo.uid).doc(payload.name)
        let isRenaming = ((payload.name != payload.originalName))
        if ((payload.method == 'create') || !isRenaming) {
          docRef.set(payload.deck, { merge: true })    
            .then(commit('addError', ''))
            .then(router.push('/dashboard/learn'))
            .catch(error => console.log(error))
        } else if (isRenaming) {
          let originalDocRef = db.collection('decks').doc('user-decks').collection(state.userInfo.uid).doc(payload.originalName)
          docRef.set(payload.deck, { merge: true })
            .then(() => {
              originalDocRef.delete()
                .then(commit('addError', ''))
                .then(router.push('/dashboard/learn'))
                .catch(error => console.log(error))
            })
        } else {
          commit('addError', 'A deck with this name already exists')
        }
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
    getDecks({ state, commit, dispatch }) {
      if (state.signedIn && state.userInfo.uid) {
        let decksRef = db.collection('decks').doc('user-decks').collection(state.userInfo.uid)
        decksRef.get()
          .then(snapshot => {
            new Promise((resolve) => {
              commit('updateDecks', {
                size: snapshot.size,
                docs: snapshot.docs.map(doc => doc.data())
              })
              resolve()
            })
              .then(dispatch('calculateUntilDue'))
          })
          .catch(error => console.log(error))
      }
    },
    deleteDeck({ state,  dispatch }, name) {
      if (state.signedIn && state.userInfo.uid) {
        let docRef = db.collection('decks').doc('user-decks').collection(state.userInfo.uid).doc(name)
        docRef.delete()
          .then(() => {
            new Promise((resolve) => {
              dispatch('getDecks')
              resolve()
            })
              .then(router.push('/dashboard/learn'))
              .catch(error => console.log(error))
          })
      }
    },
    getServerTime({ commit }) {
      commit('updateServerTime', firebase.firestore.Timestamp.now())
    },
    calculateUntilDue({ state, commit, dispatch }) {
      dispatch('getServerTime')
        .then(() => {
          commit('clearDues')
          for (let i = 0; i < state.decks.length; i++) {
            let dues = []
            for (let duedate in state.decks[i].dueDates) {
              commit('getDueDifference', state.decks[i].dueDates[duedate])
              dues.push(state.dueDifference)
            }
            commit('updateDues', {
              option: 'untilDue',
              data: Math.min(...dues)
            })
            if (state.untilDue[i] > 0) {
              commit('updateDues', {
                option: 'dueInfoColor',
                data: 'text-green-300'
              })
            } else {
              commit('updateDues', {
                option: 'dueInfoColor',
                data: 'text-red-400'
              })
            }
          }
        })
        .catch(error => console.log(error))
    }
  },
  modules: {
  },
  getters: {
  },
  plugins: [createPersistedState()]
})
