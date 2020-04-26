import Vue from 'vue'
import Vuex from 'vuex'
import * as firebase from 'firebase/app'
import 'firebase/auth'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null
  },
  mutations: {
    updateUser(state, payload) {
      state.user = payload
    }
  },
  actions: {
    signInWithGoogleAction({ commit }) {
      var provider = new firebase.auth.GoogleAuthProvider()
      firebase.auth().signInWithPopup(provider)
        .then(response => commit('updateUser', response))
        .catch(error => console.log(error))
    },
    signUpWithEmailAction({ commit }, credentials) {
      firebase.auth().createUserWithEmailAndPassword(credentials.email, credentials.password)
        .then(response => commit('updateUser', response))
        .catch(error => console.log(error))
    },
    signInWithEmailAction({ commit }, credentials) {
      firebase.auth().signInWithEmailAndPassword(credentials.email, credentials.password)
        .then(response => commit('updateUser', response))
        .catch(error => console.log(error))
    }
  },
  modules: {
  },
  getters: {
  }
})
