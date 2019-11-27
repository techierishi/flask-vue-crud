import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import SigVerify from './components/SigVerify.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Signature Verify',
      component: SigVerify,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
