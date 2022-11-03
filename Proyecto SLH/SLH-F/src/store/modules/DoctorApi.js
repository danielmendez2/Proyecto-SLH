///api/Patients/listpatients/
import http from "@/http";

export default {
  namespaced: true,
  state: {
    doctor: null,
  },
  getters: {},
  mutations: {},
  actions: {
    async getDoctores({ commit }) {
      try {
        const respuesta = await http({
          url: `/Doctors/listdoctors/`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async getDoctorid({ commit }, { id }) {
      try {
        const respuesta = await http({
          url: `/Doctors/listdoctors/${id}`,
          header: {},
          method: "GET",
        });
        console.log("res", respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
    async crearDoctor({ commit }, { data }) {
      try {
        const respuesta = await http({
          url: `/Doctors/listdoctors/`,
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
