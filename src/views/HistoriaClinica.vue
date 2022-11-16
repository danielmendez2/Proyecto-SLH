<template>
  <div>
    <div>
      <div>
        <h1>Historias clínicas</h1>
        <div cols="12" md="4" lg="3">
          <v-btn color="success" @click="historia.estado = true" dark large> Crear Historia clínica </v-btn>
        </div>
      </div>
      <div>
        <!-- <div>
          <div cols="12" md="4" lg="3">
            <v-btn color="success" dark large> Consultar por numero ID </v-btn>
          </div>
        </div> -->

        <v-text-field cols="12" md="4" lg="3" v-model="search" label="Consultar por N° documento" class="purple-input" />

        <!-- :items="registros" -->
        <template>
          <v-data-table :search="search" :headers="headers" :items="historias" item-key="id" :items-per-page="5" class="elevation-1"></v-data-table>
        </template>
      </div>
    </div>
    <HISTORIA :historia="historia" v-if="historia.estado"></HISTORIA>
  </div>
</template>
<script>
import popapHistoria from "../components/HC.vue";
import axios from "axios";
import { Global } from "../global";
import { mapActions } from "vuex";
export default {
  components: {
    HISTORIA: popapHistoria,
  },
  data: () => ({
    search: "",
    headers: [
      {
        text: "Nombres",
        align: "center",
        sortable: false,
        value: "Name_patients.Name",
      },
      {
        text: "Apellidos",
        align: "center",
        sortable: false,
        value: "Name_patients.Surname",
      },
      {
        text: "N° documento",
        align: "center",
        sortable: false,
        value: "Name_patients.identification_number",
      },
      {
        text: "Ocupación",
        align: "center",
        sortable: false,
        value: "Occupation",
      },
      {
        text: "Razón consulta",
        align: "center",
        sortable: false,
        value: "reason_for_consultation",
      },
      {
        text: "Enfermedad actual",
        align: "center",
        sortable: false,
        value: "current_illness",
      },
      {
        text: "Fecha-hora entrada",
        align: "center",
        sortable: false,
        value: "hour_entry_finish",
      },
      {
        text: "Concepto médico",
        align: "center",
        sortable: false,
        value: "Doctor_concept",
      },
    ],
    historia: {
      estado: false,
    },
    historias: [],
    pacientes: [],
  }),

  async mounted() {
    this.historias = await this.getHistorias();
    this.pacientes = await this.getPacientes();

    this.historias.forEach(async (e, i) => {
      e.Name_patients = await this.traerPaci(e.Name_patients);
    });

    this.getServicios();
  },
  methods: {
    async traerPaci(id) {
      let respaci = [];
      respaci = await this.getPaciente({ id });
      return respaci;
    },
    ...mapActions({
      getHistorias: "historia_clinica/getHistorias",
      getPacientes: "pacientes_api/getPacientes",
      getPaciente: "pacientes_api/getPaciente",
    }),
    async obtenerHistoria() {
      const id = this.search;
      let res = await this.getHistoria({ id });
    },
    getServicios() {
      axios.get(Global.url + "/historyhistory/").then((res) => {
        console.log("estoy en metodo get", res.status);
        if (res.status == 200) {
          this.historia_cli = res.data;
          console.log((this.historia_cli.id = "1"));
        } else {
          alert("no se pudo conectar");
        }
      });
    },
  },
};
</script>
<style scoped>
.border {
  border-left: 4px solid #0ba518;
}
</style>
