import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '*',
    redirec: '/',
  },
  {
    path: '/',
    name: 'home',
    component: function () {
      return import('../views/HomeView.vue')
    }
  },
  {
    path: '/Login',
    name: 'login',
    component: function () {
      return import('../views/Login.vue')
    }
  },
  {
    path: '/Team',
    name: 'Team',
    component: function () {
      return import('../views/Team.vue')
    }
  },
  {
    path: '/Projects',
    name: 'Projects',
    component: function () {
      return import('../views/Projects.vue')
    }
  },
  {
    path: '/HomeAdmin',
    name: 'HomeAdmin',
    component: function () {
      return import('../views/HomeAdmin.vue')
    }
  }
]

const router = new VueRouter({
  routes
})

export default router
