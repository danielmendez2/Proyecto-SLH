<template>
    <div>
      <div>
        <div>
          <h1>Citas</h1>
          <div cols="12" md="4" lg="3">
            <v-btn color="success" @click="cita.estado = true" dark large>
              Crear cita medica
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
            label="Consultar por numero ID"
            class="purple-input"
          />
          
              <!-- :items="registros" -->
          <template>
            <v-data-table
    
              :items-per-page="5"
              class="elevation-1"
            ></v-data-table>
          </template>
        </div>
       
      </div>
      <CITA :cita="cita"></CITA>
    </div>
  </template>
  <script>
  import popapCita from "../components/Cta.vue";
  // import axios from "axios";
  // import {Global} from "../Global"
  export default {
    components: {
      CITA: popapCita,
    },
    data: () => ({
      cita: {
        estado: false,
      },
    }),
    methods: {
    
  },
  
  };
  </script>
  <style scoped>
  .border {
    border-left: 4px solid #0ba518;
  }
  </style>
  