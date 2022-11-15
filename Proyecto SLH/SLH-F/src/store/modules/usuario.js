import http from "@/http";

export default {
  namespaced: true,
  state: {
    usuario: null,
  },
  getters: {},
  mutations: {},
  actions: {
    async loginUsuario({ commit }, { data }) {
      const { usuario, password } = data;
      const date = {
        email: usuario,
        password: password,
      };
      try {
        const respuesta = await http({
          url: `token`,
          header: {},
          method: "POST",
          data: date,
        });
        let acceso = {};
        if (respuesta.access) {
          localStorage.auth = respuesta.access;
          localStorage.refresh = respuesta.refresh;
          acceso = 200;
        } else {
          acceso = 400;
        }
        return acceso;
      } catch (error) {
        console.error(error);
      }
    },
    // async loginUsuario({ commit }, { data }) {
    //   const { usuario, password } = data;
    //   try {
    //     const respuesta = await http({
    //       url: `useruser/`,
    //       header: {},
    //       method: "GET",
    //     });
    //     let acceso = {};
    //     respuesta.forEach((e) => {
    //       console.log(usuario == e.email && password == e.password);
    //       if (usuario == e.email && password == e.password) {
    //         console.log(usuario, password);
    //         localStorage.auth = JSON.stringify(e);
    //         acceso = 200;
    //       } else acceso = 400;
    //     });
    //     return acceso;
    //   } catch (error) {
    //     console.error(error);
    //   }
    // },
    async gethistorias({ commit }) {
      try {
        const respuesta = await http({
          url: `historia/lista`,
          header: {},
          method: "GET",
        });
        console.log(respuesta);
        return respuesta;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
