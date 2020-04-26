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
    signInWithGoogleAction(context) {
      var provider = new firebase.auth.GoogleAuthProvider()
      firebase.auth().signInWithPopup(provider)
      .then(response => {
        context.commit('updateUser', response)
      })
    }
  },
  modules: {
  },
  getters: {
  }
})
