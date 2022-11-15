import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import crecimiento_api from "./modules/CrecimientoDesarrolloApi";
import historia_clinica from "./modules/historiaClinicaApi";
import vacunador_api from "./modules/vacunadorApi";
import pacientes_api from "./modules/pacientesApi";
import vacunas_api from "./modules/CarnetVacuna";
import doctor_api from "./modules/DoctorApi";
import usuario from "./modules/usuario";

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    usuario,
    historia_clinica,
    crecimiento_api,
    vacunador_api,
    pacientes_api,
    vacunas_api,
    doctor_api,
  },
});
