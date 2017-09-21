import Vue from 'vue'
import Vuetify from 'vuetify'
import './stylus/main.styl'
import App from './App'
import router from './router'
import { store } from './Store'
import DateFilter from './filters/date'
import VueFilter from 'vue-filter'
import StarRating from 'vue-star-rating'

Vue.use(Vuetify)
Vue.use(VueFilter)
Vue.config.productionTip = false

Vue.component('star-rating', StarRating)

Vue.filter('date', DateFilter)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
  created () {
    this.$store.dispatch('carregaResenhas')
    this.$store.dispatch('carregaLivros')
  }
})
