import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    userInfo: {
      name: null,
      email: null,
      photoUrl: null,
      emailVerified: null,
      uid: null,
    }
  },
  mutations: {
    setUser (state, payload) {
      state.user = payload
    }
  },
  actions: {
    setUserAction(context, payload) {
      context.commit('setUser', payload)
    }
  },
  modules: {
  },
  getters: {
  }
})
