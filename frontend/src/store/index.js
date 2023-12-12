import { createStore } from 'vuex';

export default createStore({
 state: {
    isAuthenticated: false,
    token: '',
 },
 mutations: {
   initializeStore(state) {
      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
   },
   removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
   },
   setUser(state, userData) {
      // Update the state with the user data
      state.user = userData;
    },  
  },
 actions: {
   },
 modules: {
   }
});