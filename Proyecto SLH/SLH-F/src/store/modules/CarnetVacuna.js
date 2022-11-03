///api/Patients/listpatients/
import http from "@/http";

export default {
  namespaced: true,
  state: {
    paciente: null,
  },
  getters: {},
  mutations: {},
  actions: {
    async getVacunas({ commit }) {
      try {
        const respuesta = await http({
          url: `Vaccines/listvaccines/`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async getVacunasid({ commit }, { id }) {
      try {
        const respuesta = await http({
          url: `Vaccines/listvaccines/${id}`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async crearPaciente({ commit }, { data }) {
      try {
        const respuesta = await http({
          url: `Vaccines/listvaccines/`,
          // header: {},
          data,
          method: "POST",
        });
        return respuesta;
      } catch (error) {
        console.error(error);
        
      }
    },
  },
};
