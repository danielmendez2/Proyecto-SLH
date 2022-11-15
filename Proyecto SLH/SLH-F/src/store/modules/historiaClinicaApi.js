import http from "@/http";

export default {
  namespaced: true,
  state: {
    historia: null,
  },
  getters: {},
  mutations: {},
  actions: {
    async getHistorias({ commit }) {
      try {
        const respuesta = await http({
          url: `historyhistory/`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async getHistoria({ commit }, { id }) {
      try {
        const respuesta = await http({
          url: `historyhistory/${id}`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async crearHistoria({ commit }, { data }) {
      console.log("data de crear historia", data);
      try {
        const respuesta = await http({
          url: `historyhistory/`,
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
