import Vue from 'vue';

import App from './App';
import router from './router';
import store from './store';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.config.productionTip = false;

export default new Vue({
  router,
  store,
  el: '#app',
  template: '<App/>',
  components: { App },
});
