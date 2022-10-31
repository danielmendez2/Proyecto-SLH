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

        <v-text-field cols="12" md="4" lg="3" v-model="search" label="Consultar por número ID" class="purple-input" />
        <template>
          <v-data-table :search="search" :headers="headers" :items="vacuas" item-key="id" :items-per-page="5" class="elevation-1"></v-data-table>
        </template>
      </div>
    </div>
    <VACUNA :vacuna="vacuna"></VACUNA>
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
        text: "ID",
        align: "center",
        sortable: false,
        value: "id",
      },
      {
        text: "Biologico",
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
        text: "Fecha vacunacion",
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
        text: "Dosis",
        align: "center",
        sortable: false,
        value: "reason_for_consultation",
      },
      {
        text: "Fecha vacuna",
        align: "center",
        sortable: false,
        value: "hour_entry_finish",
      },
      {
        text: "Fabricante",
        align: "center",
        sortable: false,
        value: "Doctor_concept",
      },
      {
        text: "Lote",
        align: "center",
        sortable: false,
        value: "reason_for_consultation",
      },
      {
        text: "IPS vacunadora",
        align: "center",
        sortable: false,
        value: "Doctor_concept",
      },
      {
        text: "Nombre vacunador",
        align: "center",
        sortable: false,
        value: "reason_for_consultation",
      },
      {
        text: "Cédula vacunador",
        align: "center",
        sortable: false,
        value: "hour_entry_finish",
      },
    ],

    vacuna: {
      estado: false,
    },
    vacuas: [],
  }),

  async mounted() {
    this.vacuas = await this.getVacunas();
    console.log("array vacunas",this.vacuas)
    this.getServicios();
  },
  methods: {
    ...mapActions({
      getVacunas: "vacunas_api/getVacunas",
      //getHistoria: "historia_clinica/getHistoria",
    }),
    async obtenerCarnetVacuna() {
      const id = this.search;
      let res = await this.getVacunas({ id });
    },

    getServicios() {
      let config = {
        // Headers:{
        //   'token': Global.token
        // }
      };
      axios.get(Global.url + "/api/Vaccines/listvaccines/").then((res) => {
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
