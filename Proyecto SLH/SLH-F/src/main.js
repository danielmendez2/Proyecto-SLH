import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import Vuelidate from 'vuelidate'
import VueMask from 'v-mask'
Vue.use(VueMask);
Vue.config.productionTip = false
Vue.use(Vuelidate);
new Vue({
  router,
  store,
  vuetify,
  Vuelidate,
  render: function (h) { return h(App) }
}).$mount('#app')
