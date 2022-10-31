<template>
    <div>
      <div>
        <div>
          <h1>Crecimiento y desarrollo</h1>
          <div cols="12" md="4" lg="3">
            <v-btn color="success" @click="crecimt_desarr.estado = true" dark large>
              Crear Crecimiento y desarrollo
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
            label="Consultar por número ID"
            class="purple-input"
          />
          <template>
            <v-data-table
              :headers="headers"
              :items="registros"
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
  
  export default {
    components: {
      CRECIMIENTO: popapCrecimt_desarr,
    },
    data: () => ({
        crecimt_desarr: {
        estado: false,
      },
    }),
  };
  </script>
  <style scoped>
  .border {
    border-left: 4px solid #0ba518;
  }
  </style>
  