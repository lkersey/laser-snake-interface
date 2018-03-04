import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import SetUp from '@/components/pages/SetUp'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/set-up',
      name: 'SetUp',
      component: SetUp
    }
  ]
})
