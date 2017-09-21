import router from 'Vue-router'
import HTTP from '../shared/http-common'

// const LOGIN_URL = 'http://localhost:8000/api-auth/login/'
const TOKEN_URL = 'http://localhost:8000/api-token/'
const BASE_URL = 'http://localhost:8000/'

export default {
  login (context, creds, redirect) {
    console.log(creds)
    HTTP.post(TOKEN_URL, creds).then((response) => {
      localStorage.setItem('token', response.token)
      // this.user.authenticated = true

      // If a redirect link is provided
      if (redirect) {
        router.push(redirect)
      }
    }).catch((err) => {
      console.log(err)
    })
  },
  logout (context, redirect) {
    HTTP.post(BASE_URL + 'api-auth/logout/').then((response) => {
      localStorage.removeItem('token')
      // this.user.authenticated = false

      // If a redirect link is provided
      if (redirect) {
        router.push(redirect)
      }
    }).catch((err) => {
      console.log(err)
    })
  },
  register (context, cred, redirect) {
    HTTP.post(BASE_URL + 'users/', cred).then((response) => {
      this.login(context, cred)

      // If a redirect link is provided
      if (redirect) {
        router.push(redirect)
      }
    }).catch((err) => {
      console.log(err)
    })
  }
}
