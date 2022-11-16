///api/Patients/listpatients/
import http from "@/http";

export default {
  namespaced: true,
  state: {
    vacunador: null,
  },
  getters: {},
  mutations: {},
  actions: {
    async getVacunadores({ commit }) {
      try {
        const respuesta = await http({
          url: `nursenurse/`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async getVacunador({ commit }, { id }) {
      try {
        const respuesta = await http({
          url: `nursenurse/${id}/`,
          header: {},
          method: "GET",
        });
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async crearVacunador({ commit }, { data }) {
      try {
        const respuesta = await http({
          url: `nursenurse/`,
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
