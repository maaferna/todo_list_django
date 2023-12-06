import { createStore } from 'vuex';

export default createStore({
 state: {
    isAuthenticated: false,
 },
 mutations: {
    authenticate(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
 },
 actions: {
    authenticate({ commit }, isAuthenticated) {
      commit('authenticate', isAuthenticated);
    },
 },
});