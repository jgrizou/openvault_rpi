import Vue from 'vue'
import Router from 'vue-router'
import Level1 from './../pages/Level1'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/ui/*',
      name: 'Level1',
      component: Level1
    }
  ]
})
