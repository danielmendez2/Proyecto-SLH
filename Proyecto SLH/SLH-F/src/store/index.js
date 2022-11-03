import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import usuario from './modules/usuario'
import historia_clinica from './modules/historiaClinicaApi'
import pacientes_api from './modules/pacientesApi'
import crecimiento_api from './modules/pacientesApi'
import vacunas_api from './modules/CarnetVacuna'
import doctor_api from './modules/DoctorApi'

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    usuario,
    historia_clinica,
    pacientes_api,
    crecimiento_api,
    vacunas_api,
    doctor_api
  }
})
