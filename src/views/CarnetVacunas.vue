<template>
  <div>
    <div>
      <div>
        <h1>Carnet vacunas</h1>
        <div cols="12" md="4" lg="3">
          <v-btn color="success" @click="vacuna.estado = true" dark large> Crear carnet de vacunas </v-btn>
        </div>
      </div>
      <div>
        <!-- <div>
          <div cols="12" md="4" lg="3">
            <v-btn color="success" dark large> Consultar por numero ID </v-btn>
          </div>
        </div> -->

        <v-text-field cols="12" md="4" lg="3" v-model="search" label="Consultar por N° documento" class="purple-input" />
        <template>
          <v-data-table :search="search" :headers="headers" :items="vacuas" item-key="id" :items-per-page="5" class="elevation-1"></v-data-table>
        </template>
      </div>
    </div>
    <VACUNA :vacuna="vacuna" v-if="vacuna.estado"></VACUNA>
  </div>
</template>
<script>
import popapVacuna from "../components/CV.vue";
import axios from "axios";
import { Global } from "../global";
import { mapActions } from "vuex";
export default {
  components: {
    VACUNA: popapVacuna,
  },
  data: () => ({
    search: "",
    headers: [
      {
        text: "Nombres",
        align: "center",
        sortable: false,
        value: "name_patient.Name",
      },
      {
        text: "Apellidos",
        align: "center",
        sortable: false,
        value: "name_patient.Surname",
      },
      {
        text: "N° documento paciente",
        align: "center",
        sortable: false,
        value: "name_patient.identification_number",
      },
      {
        text: "Biológico",
        align: "center",
        sortable: false,
        value: "Biological",
      },
      {
        text: "Dosis",
        align: "center",
        sortable: false,
        value: "Dose",
      },
      {
        text: "Fecha vacunación",
        align: "center",
        sortable: false,
        value: "Vaccine_date",
      },
      {
        text: "Fabricante",
        align: "center",
        sortable: false,
        value: "Factory",
      },
      {
        text: "Lote",
        align: "center",
        sortable: false,
        value: "Lot",
      },
      {
        text: "Eps",
        align: "center",
        sortable: false,
        value: "Eps",
      },
      {
        text: "IPS vacunadora",
        align: "center",
        sortable: false,
        value: "Ips",
      },
      {
        text: "Nombre vacunador",
        align: "center",
        sortable: false,
        value: "reason_for_consultation",
      },
      {
        text: "N° documento vacunador",
        align: "center",
        sortable: false,
        value: "hour_entry_finish",
      },
    ],

    vacuna: {
      estado: false,
    },
    vacuas: [],
    pacientes: [],
  }),

  async mounted() {
    this.vacuas = await this.getVacunas();
    this.pacientes = await this.getPacientes();
    this.vacuas.forEach(async (e, i) => {
      e.name_patient = await this.traerPaci(e.name_patient);
    });
    this.getServicios();
  },
  methods: {
    async traerPaci(id) {
      let respaci = [];
      respaci = await this.getPaciente({ id });
      console.log("--------Z", respaci);

      return respaci;
    },
    ...mapActions({
      getVacunas: "vacunas_api/getVacunas",
      getPacientes: "pacientes_api/getPacientes",
      getPaciente: "pacientes_api/getPaciente",
      //getHistoria: "historia_clinica/getHistoria",
    }),
    async obtenerCarnetVacuna() {
      const id = this.search;
      let res = await this.getVacunas({ id });
    },

    getServicios() {
      axios.get(Global.url + "/api/Vaccinesvaccines/").then((res) => {
        console.log("estoy en metodo get vacunas", res.status);
        if (res.status == 200) {
          this.carnet_vacu = res.data;
          console.log((this.carnet_vacu.id = "1"));
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
