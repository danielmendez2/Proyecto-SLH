<template>
  <div>
    <div>
      <div>
        <h1>Carnet vacunación</h1>
        <div cols="12" md="4" lg="3">
          <v-btn color="success" @click="vacuna.estado = true" dark large>
            Crear Carnet vacunas
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
        <template>
          <v-data-table
            
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </template>
      </div>
    </div>
    <VACUNAS :vacuna="vacuna"></VACUNAS>
  </div>
</template>
<script>
import popapVacunas from "../components/CV.vue";

export default {
  components: {
    VACUNAS: popapVacunas,
  },
  data: () => ({
    vacuna: {
      estado: false,

      // headers: [
      //   {
      //     text: "Nombres",
      //     align: "start",
      //     sortable: false,
      //     value: "nombres",
      //   },
      //   { text: "Apellidos", value: "apellidos" },
      //   { text: "Tipo ID", value: "tipo_id" },
      //   { text: "Numero ID", value: "numero_id" },
      //   { text: "Fecha nacimiento", value: "fecha_nacimiento" },
      //   { text: "Biológico", value: "biologico" },
      //   { text: "Dosis", value: "dosis" },
      //   { text: "Fecha vacuna", value: "fecha_vacuna" },
      //   { text: "Fabricante", value: "fabricante" },
      //   { text: "Lote", value: "lote" },
      //   { text: "IPS vacuna", value: "ips_vacuna" },
      //   { text: "Nombre vacunador", value: "nombre_vacunador" },
      //   { text: "Cedula vacunador", value: "cedula_vacunador" },
      // ],
      // registros: [
      //   {
      //     nombres: "daniel",
      //     apellidos: "mendez",
      //     tipo_id: "cc",
      //     numero_id: "100680995",
      //     fecha_nacimiento: "20/09/2000",
      //     biologico: "covid-19",
      //     dosis: "1",
      //     fecha_vacuna: "03/01/2022",
      //     fabricante: "moderna",
      //     lote: "005h21a",
      //     ips_vacuna: "c-a restrepo",
      //     nombre_vacunador: "jennifer vera",
      //     cedula_vacunador: "101903578",
      //   },
      //   {
      //     nombres: "",
      //     apellidos: "",
      //     tipo_id: "",
      //     numero_id: "",
      //     fecha_nacimiento: "",
      //     biologico: "",
      //     dosis: "",
      //     fecha_vacuna: "",
      //     fabricante: "",
      //     lote: "",
      //     ips_vacuna: "",
      //     nombre_vacunador: "",
      //     cedula_vacunador: "",
      //   },
      //   {
      //     nombres: "",
      //     apellidos: "",
      //     tipo_id: "",
      //     numero_id: "",
      //     fecha_nacimiento: "",
      //     biologico: "",
      //     dosis: "",
      //     fecha_vacuna: "",
      //     fabricante: "",
      //     lote: "",
      //     ips_vacuna: "",
      //     nombre_vacunador: "",
      //     cedula_vacunador: "",
      //   },
      //   {
      //     nombres: "",
      //     apellidos: "",
      //     tipo_id: "",
      //     numero_id: "",
      //     fecha_nacimiento: "",
      //     biologico: "",
      //     dosis: "",
      //     fecha_vacuna: "",
      //     fabricante: "",
      //     lote: "",
      //     ips_vacuna: "",
      //     nombre_vacunador: "",
      //     cedula_vacunador: "",
      //   },
      //   {
      //     nombres: "",
      //     apellidos: "",
      //     tipo_id: "",
      //     numero_id: "",
      //     fecha_nacimiento: "",
      //     biologico: "",
      //     dosis: "",
      //     fecha_vacuna: "",
      //     fabricante: "",
      //     lote: "",
      //     ips_vacuna: "",
      //     nombre_vacunador: "",
      //     cedula_vacunador: "",
      //   },

      //   {
      //     nombres: "",
      //     apellidos: "",
      //     tipo_id: "",
      //     numero_id: "",
      //     fecha_nacimiento: "",
      //     biologico: "",
      //     dosis: "",
      //     fecha_vacuna: "",
      //     fabricante: "",
      //     lote: "",
      //     ips_vacuna: "",
      //     nombre_vacunador: "",
      //     cedula_vacunador: "",
      //   },
      // ],
    },
  }),
};
</script>
<style scoped>
.border {
  border-left: 4px solid #0ba518;
}
</style>
