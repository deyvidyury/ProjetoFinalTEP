import Vue from 'vue'
import Vuex from 'vuex'
import {HTTP} from '../shared/http-common'
import router from '../router'

const TOKEN_URL = 'http://localhost:8000/api-token/'
const BASE_URL = 'http://localhost:8000/'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    loading: false,
    error: null,
    livros: [],
    resenhas: [],
    previousResenhas: null,
    nextResenhas: null,
    previousLivros: null,
    nextLivros: null,
    user: null
  },
  mutations: {
    setUser (state, payload) {
      state.user = payload
    },
    setResenhasCarregadas (state, payload) {
      state.resenhas = payload
    },
    updateResenha (state, payload) {
      let resenha = state.resenhas.find((resenha) => {
        return resenha.id === payload.id
      })
      resenha.nota.estrelas__avg = payload.nota.estrelas__avg
      resenha.comentarios = payload.comentarios
    },
    setLivrosCarregados (state, payload) {
      state.livros = payload
    },
    setPreviousResenhas (state, payload) {
      state.previousResenhas = payload
    },
    clearPreviousResenhas (state) {
      state.previousResenhas = null
    },
    setNextResenhas (state, payload) {
      state.nextResenhas = payload
    },
    clearNextResenhas (state) {
      state.nextResenhas = null
    },
    setPreviousLivros (state, payload) {
      state.previousLivros = payload
    },
    clearPreviousLivros (state) {
      state.previousLivros = null
    },
    setNextLivros (state, payload) {
      state.nextLivros = payload
    },
    clearNextLivros (state) {
      state.nextLivros = null
    },
    setLoading (state, payload) {
      state.loading = payload
    },
    setError (state, payload) {
      state.error = payload
    },
    clearError (state) {
      state.error = null
    }
  },
  actions: {
    carregaResenhas ({commit}, url = 'http://localhost:8000/resenhas/') {
      commit('setLoading', true)
      commit('clearPreviousResenhas')
      commit('clearNextResenhas')
      let resenhas = []
      HTTP.get(url)
        .then((dados) => {
          resenhas = dados.data.results
          commit('setResenhasCarregadas', resenhas)
          commit('setPreviousResenhas', dados.data.previous)
          commit('setNextResenhas', dados.data.next)
          commit('setLoading', false)
        })
        .catch((error) => {
          console.log(error)
          commit('setLoading', false)
        })
    },
    carregaLivros ({commit}, url = 'http://localhost:8000/livros/') {
      commit('setLoading', true)
      commit('clearPreviousLivros')
      commit('clearNextLivros')
      let livros = []
      HTTP.get(url)
        .then((dados) => {
          livros = dados.data.results
          commit('setLivrosCarregados', livros)
          commit('setPreviousLivros', dados.data.previous)
          commit('setNextLivros', dados.data.next)
          commit('setLoading', false)
        })
        .catch((error) => {
          console.log(error)
          commit('setLoading', false)
        })
    },
    avaliar ({commit}, payload) {
      HTTP.post('http://localhost:8000/avaliacoes/', {resenha: payload.resenha, estrelas: payload.nota, usuario: 1})
        .then((response) => {
          // recarregar a resenha
          HTTP.get('http://localhost:8000/resenhas/' + payload.resenha + '/')
            .then((dados) => {
              commit('updateResenha', dados.data)
            })
            .catch((error) => {
              console.log(error)
            })
        })
        .catch((error) => {
          console.log(error)
        })
    },
    registrar ({commit}, payload) {
      commit('setLoading', true)
      commit('clearError')

      // createUser
      HTTP.post(BASE_URL + 'users/', payload).then((response) => {
        console.log(response)
        let newUser = response.data
        let creds = {
          username: payload.username,
          password: payload.password
        }

        // Pega token do usuario
        HTTP.post(TOKEN_URL, creds).then((response) => {
          commit('setLoading', false)
          localStorage.setItem('token', response.token)
          newUser.authenticated = true
          commit('setUser', newUser)
          router.push('/')
        }).catch((err) => {
          commit('setLoading', false)
          console.log(err)
        })
      }).catch((err) => {
        commit('setLoading', false)
        console.log(err)
      })
    },
    login ({commit}, payload) {
      commit('setLoading', true)
      commit('clearError')
      HTTP.post(TOKEN_URL, payload)
        .then(response => {
          commit('setLoading', false)
          localStorage.setItem('token', response.data.token)
          // pega informacoes do usuario
          HTTP.get(BASE_URL + 'users/?search=' + payload.username)
            .then(response => {
              commit('setLoading', false)
              console.log(response)
              let user = response.data.results
              user.authenticated = true
              commit('setUser', user)
            })
            .catch(error => {
              commit('setLoading', false)
              console.log(error)
            })
          router.push('/')
        })
        .catch(error => {
          commit('setLoading', false)
          console.log(error)
        })
    },
    logout ({commit}) {
      commit('setLoading', true)
      HTTP.get(BASE_URL + 'api-auth/logout/')
        .then(() => {
          commit('setLoading', false)
          localStorage.removeItem('token')
          commit('setUser', null)
          router.push('/')
        })
        .catch(error => {
          commit('setLoading', false)
          console.log(error)
        })
    }
  },
  getters: {
    resenhasCarregadas (state) {
      return state.resenhas
    },
    resenhasMaisRecentes (state, getters) {
      return state.resenhas.slice(0, 5)
    },
    livrosCarregados (state) {
      return state.livros
    },
    livrosMaisRecentes (state, getters) {
      return state.livros.slice(0, 5)
    },
    resenhaCarregada (state) {
      return (resenhaId) => {
        return state.resenhas.find((resenha) => {
          return resenha.id + '' === resenhaId
        })
      }
    },
    livroCarregado (state) {
      return (livroId) => {
        return state.livros.find((livro) => {
          return livro.id + '' === livroId
        })
      }
    },
    previousResenhas (state) {
      return state.previousResenhas
    },
    nextResenhas (state) {
      return state.nextResenhas
    },
    previousLivros (state) {
      return state.previousLivros
    },
    nextLivros (state) {
      return state.nextLivros
    },
    user (state) {
      return state.user
    },
    loading (state) {
      return state.loading
    },
    erro (state) {
      return state.error
    }
  }
})
