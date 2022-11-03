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
    async getPacientes({ commit }) {
      try {
        const respuesta = await http({
          url: `Patients/listpatients/`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async getPaciente({ commit }, { id }) {
      try {
        const respuesta = await http({
          url: `Patients/listpatients/${id}`,
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
          url: `Patients/listpatients/`,
          header: {},
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
