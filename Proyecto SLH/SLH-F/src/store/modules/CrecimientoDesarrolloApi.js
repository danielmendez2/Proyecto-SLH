import http from "@/http";

export default {
  namespaced: true,
  state: {
    crecimientoDesarrollo: null,
  },
  getters: {},
  mutations: {},
  actions: {
    async getCrecimiento({ commit }) {
      try {
        const respuesta = await http({
          url: `Growthgrowth_and_development/`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async getCrecimientoid({ commit }, { id }) {
      try {
        const respuesta = await http({
          url: `Growthgrowth_and_development/${id}`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async crearCrecimiento({ commit }, { data }) {
      try {
        const respuesta = await http({
          url: `Growthgrowth_and_development/`,
        //   header: { Accept: "application/json", "Content-Type": "applicaton/json" },
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
