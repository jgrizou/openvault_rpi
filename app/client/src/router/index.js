import Vue from 'vue'
import Router from 'vue-router'
import SPA from './../pages/SPA'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/*',
      name: 'SPA',
      component: SPA
    }
  ]
})
