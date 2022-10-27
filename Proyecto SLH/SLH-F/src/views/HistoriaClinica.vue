<template>
  <div>
    <div>
      <div>
        <h1>Historias clínicas</h1>
        <div cols="12" md="4" lg="3">
          <v-btn color="success" @click="historia.estado = true" dark large>
            Crear Historia clínica
          </v-btn>
        </div>
      </div>
      <div>
        <!-- <div>
          <div cols="12" md="4" lg="3">
            <v-btn color="success" dark large> Consultar por numero ID </v-btn>
          </div>
        </div> -->

        <v-text-field
          cols="12"
          md="4"
          lg="3"
          v-model="search"
          label="Consultar"
          class="purple-input"
        />

        <!-- :items="registros" -->
        <template>
          <v-data-table
            :search="search"
            :headers="headers"
            :items="historias"
            item-key="id"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </template>
      </div>
    </div>
    <HISTORIA :historia="historia"></HISTORIA>
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
        text: "ID",
        align: "center",
        sortable: false,
        value: "id",
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
  }),

  async mounted() {
    this.historias = await this.getHistorias();
    this.getServicios();
  },
  methods: {
    ...mapActions({
      getHistorias: "historia_clinica/getHistorias",
      getHistoria: "historia_clinica/getHistoria",
    }),
    async obtenerHistoria() {
      const id = this.search;
      let res = await this.getHistoria({ id });
       
    },

    getServicios() {
      let config = {
        // Headers:{
        //   'token': Global.token
        // }
      };
      axios.get(Global.url + "/api/historia/lista").then((res) => {
        console.log(res.status);
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
