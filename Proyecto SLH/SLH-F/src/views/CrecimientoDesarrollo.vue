<template>
  <div>
    <div>
      <div>
        <h1>Crecimiento y desarrollo</h1>
        <div cols="12" md="4" lg="3">
          <v-btn color="success" @click="crecimt_desarr.estado = true" dark large> Crear Crecimiento y desarrollo </v-btn>
        </div>
      </div>
      <div>
        <!-- <div>
            <div cols="12" md="4" lg="3">
              <v-btn color="success" dark large> Consultar por numero ID </v-btn>
            </div>
          </div> -->

        <v-text-field cols="12" md="4" lg="3" label="Consultar por número ID" class="purple-input" />
        <template>
          <v-data-table
            :search="crecimt_desarr.search"
            :headers="headers"
            :items="crecimiento_des"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </template>
      </div>
    </div>
    <CRECIMIENTO :crecimt_desarr="crecimt_desarr"></CRECIMIENTO>
  </div>
</template>
<script>
import popapCrecimt_desarr from "../components/CD.vue";
import popapHistoria from "../components/HC.vue";
import axios from "axios";
import { Global } from "../global";
import { mapActions } from "vuex";
export default {
  components: {
    CRECIMIENTO: popapCrecimt_desarr,
  },
  data: () => ({
    crecimt_desarr: {
      search: "",
      estado: false,
    },
    headers: [
      {
        text: "Peso",
        align: "center",
        sortable: false,
        value: "Weight",
      },
      // {
      //   text: "--Name--",
      //   align: "center",
      //   sortable: false,
      //   value: "Name",
      // },
      {
        text: "Estatura",
        align: "center",
        sortable: false,
        value: "stature",
      },
      {
        text: "IMC",
        align: "center",
        sortable: false,
        value: "IMC",
      },
      {
        text: "Temperatura",
        align: "center",
        sortable: false,
        value: "Temperature",
      },
      {
        text: "Pulso",
        align: "center",
        sortable: false,
        value: "Pulse",
      },
      {
        text: "Frecuencia respiratoria",
        align: "center",
        sortable: false,
        value: "Breathing_frequency",
      },
      {
        text: "Presión arterial",
        align: "center",
        sortable: false,
        value: "Blood_pressure",
      },
    ],
    crecimiento: {
      estado: false,
    },

    crecimiento_des: [],
  }),

  async mounted() {
    this.crecimiento_des = await this.getCrecimiento();
    console.log("array crecimiento", this.crecimiento_des);
    this.getServicios();
  },

  methods: {
    ...mapActions({
      getCrecimiento: "crecimiento_api/getCrecimiento",
      //getHistoria: "historia_clinica/getHistoria",
    }),
    async obtenerCrecimiento() {
      const id = this.crecimt_desarr.search;
      let res = await this.getCrecimiento({ id });
    },

    getServicios() {
      axios.get(Global.url + "Growth/listgrowth_and_development/").then((res) => {
        console.log("estoy en metodo get", res.status);
        if (res.status == 200) {
          this.crecimiento_des = res.data;
          console.log((this.crecimiento_des.id = "1"));
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
