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
          url: `Patientspatients/`,
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
          url: `Patientspatients/${id}/`,
          header: {},
          method: "GET",
        });
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async crearPaciente({ commit }, { data }) {
      try {
        const respuesta = await http({
          url: `Patientspatients/`,
          header: {},
          data,
          method: "POST",
        });
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async editarPaciente({ commit }, { id, data }) {
      try {
        const RES = await http({
          url: `Patientspatients/${id}/`,
          header: {},
          method: "PUT",
          data,
        });
        console.log("res", RES);
        return RES;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
