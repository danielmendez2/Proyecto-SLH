import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '*',
    redirec: '/',
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: function () {
      return import('../views/Dashboard.vue')
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
    path: '/paciente',
    name: 'paciente',
    component: function () {
      return import('../views/Pacientes.vue')
    }
  },
  {
    path: '/HistoriaClinica',
    name: 'HistoriaClinica',
    component: function () {
      return import('../views/HistoriaClinica.vue')
    }
  },
  {
    path: '/carnetVacunas',
    name: 'carnetVacunas',
    component: function () {
      return import('../views/CarnetVacunas.vue')
    }
  },
  {
    path: '/crecimientoDesarrollo',
    name: 'crecimientoDesarrollo',
    component: function () {
      return import('../views/CrecimientoDesarrollo.vue')
    }
  },
  {
    path: '/cita',
    name: 'cita',
    component: function () {
      return import('../views/Citas.vue')
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
