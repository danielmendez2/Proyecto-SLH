<template>
  <nav>
    <v-app-bar color="light-blue lighten-1" dark app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase">
        <span class="font-weight-light">SLH</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn text v-on="on">
            <v-icon left>expand_more</v-icon>
            <span>Menu</span>
          </v-btn>
        </template>
        <v-list flat>
          <v-list-item v-for="link in links" :key="link.text" router :to="link.route" active-class="border">
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-btn text @click="estado.alerta = true">
        <span>Salir</span>
        <v-icon right>exit_to_app</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" dark app class="blue">
      <v-list flat>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.route" active-class="border">
          <v-list-item-content>
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-dialog overlay-color="grays" width="400" v-model="estado.alerta">
      <v-card>
        <v-card-title> ¿Quieres cerrar sesión? </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="estado.alerta = false" flat>No</v-btn>
          <v-btn @click="salir()" flat>Si</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </nav>
</template>
<script>
import router from "@/router";
import Popup from "./Popup.vue";
export default {
  data: () => ({
    drawer: true,
    estado: {
      alerta: false,
    },
    links: [
      { text: "Inicio", route: "/dashboard" },
      { text: "Pacientes", route: "/paciente" },
      // { text: "Citas médicas", route: "/cita" },
      { text: "Historias clínicas", route: "/HistoriaClinica" },
      { text: "Vacunas", route: "/carnetVacunas" },
      { text: "Crecimiento y desarrollo", route: "/crecimientoDesarrollo" },
    ],
  }),
  mounted() {
    if (!localStorage.auth) {
      this.$router.push("/Login");
    }
  },
  methods: {
    salir() {
      localStorage.removeItem("auth");
      this.$router.push("/Login");
    },
  },
  components: {
    Popup,
  },
};
</script>
<style scoped>
.border {
  border-left: 4px solid #0ba518;
}
</style>
