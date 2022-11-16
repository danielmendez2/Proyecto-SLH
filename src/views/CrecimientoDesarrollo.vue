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

        <v-text-field cols="12" md="4" lg="3" v-model="search" label="Consultar por N° documento" class="purple-input" />
        <template>
          <v-data-table
            :search="search"
            :headers="headers"
            item-key="id"
            :items="crecimiento_des"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </template>
      </div>
    </div>
    <CRECIMIENTO :crecimt_desarr="crecimt_desarr"  v-if="crecimt_desarr.estado" ></CRECIMIENTO>
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
    search: "",
    crecimt_desarr: {
      estado: false,
    },
    headers: [
      {
        text: "Nombres",
        align: "center",
        sortable: false,
        value: "name_patients.Name",
      },
      {
        text: "Apellidos",
        align: "center",
        sortable: false,
        value: "name_patients.Surname",
      },
      {
        text: "N° documento paciente",
        align: "center",
        sortable: false,
        value: "name_patients.identification_number",
      },
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
    pacientes: [],
  }),

  async mounted() {
    this.crecimiento_des = await this.getCrecimiento();
    this.pacientes = await this.getPacientes();
    this.crecimiento_des.forEach(async (e, i) => {
      e.name_patients = await this.traerPaci(e.name_patients);
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
      getCrecimiento: "crecimiento_api/getCrecimiento",
      getPacientes: "pacientes_api/getPacientes",
      getPaciente: "pacientes_api/getPaciente",
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
