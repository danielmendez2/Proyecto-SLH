<template>
  <v-container fluid class="fill-height">
    <div>
      <div>
        <h1>Pacientes</h1>
        <div cols="12" md="4" lg="3">
          <v-btn color="success" @click="paciente_popap.estado = true" dark large> Crear paciente </v-btn>
        </div>
      </div>
      <div>
        <v-text-field cols="12" md="4" lg="3" v-model="search" label="Consultar" class="purple-input" />
        <template>
          <v-data-table :search="search" :headers="headers" :items="pacientes" item-key="id" :items-per-page="5" class="elevation-1">
            <template v-slot:[`item.actions`]="{ item }">
              <v-icon small color="warning" class="mr-2" @click="editPaciente(item)"> mdi-pencil </v-icon>
            </template>
          </v-data-table>
        </template>
      </div>
    </div>
    <PACIENTE :paciente_popap="paciente_popap" v-if="paciente_popap.estado"></PACIENTE>
    <PACIENTEOP :paciente_popap="paciente_op" v-if="paciente_op.estado"></PACIENTEOP>
  </v-container>
</template>
<script>
import popapPaciente from "../components/PCT.vue";
import paciente_op from "../components/PCT_EDIT.vue";
import axios from "axios";
import { Global } from "../global";
import { mapActions } from "vuex";

export default {
  components: {
    PACIENTE: popapPaciente,
    PACIENTEOP: paciente_op,

  },
  data: () => ({
    search: "",
    headers: [
      {
        text: "Nombre",
        align: "center",
        sortable: false,
        value: "Name",
      },
      {
        text: "Apellido",
        align: "center",
        sortable: false,
        value: "Surname",
      },
      {
        text: "Tipo doc.",
        align: "center",
        sortable: false,
        value: "type_identification",
      },
      {
        text: "Número doc.",
        align: "center",
        sortable: false,
        value: "identification_number",
      },
      {
        text: "Número celular",
        align: "center",
        sortable: false,
        value: "Phone",
      },
      {
        text: "Dirección",
        align: "center",
        sortable: false,
        value: "Direction",
      },
      {
        text: "Género",
        align: "center",
        sortable: false,
        value: "gender",
      },
      {
        text: "EPS",
        align: "center",
        sortable: false,
        value: "Eps",
      },
      {
        text: "Correo",
        align: "center",
        sortable: false,
        value: "email",
      },
      {
        text: "Fecha de nacimiento",
        align: "center",
        sortable: false,
        value: "date_of_birth",
      },
      { text: "Actions", value: "actions", sortable: false },
    ],
    paciente_popap: {
      estado: false,
    },
    paciente_op: {
      estado: false,
    },
    pacientes: [],
  }),
  async mounted() {
    this.pacientes = await this.getPacientes();
    console.log("array pacientes", this.pacientes);

    this.getServicios();
  },
  methods: {
    ...mapActions({
      getPacientes: "pacientes_api/getPacientes",
      getPaciente: "paciente/getPaciente",
    }),
    async obtenerPaciente() {
      const id = this.search;
      let res = await this.getPaciente({ id });
    },
    editPaciente(item) {
      //console.log(item)
      this.paciente_op.Name = item.Name;
      this.paciente_op.Surname = item.Surname;
      this.paciente_op.type_identification = item.type_identification;
      this.paciente_op.identification_number = item.identification_number;
      this.paciente_op.Phone = item.Phone;
      this.paciente_op.Direction = item.Direction;
      this.paciente_op.gender = item.gender;
      this.paciente_op.Eps = item.Eps;
      this.paciente_op.email = item.email;
      this.paciente_op.date_of_birth = item.date_of_birth;
      this.paciente_op.id = item.id;

      this.paciente_op.estado = true;
      this.paciente_op.editar = true;
    },
    getServicios() {
      let config = {
        // Headers:{
        //   'token': Global.token
        // }
      };
      axios.get(Global.url + "/api/Patientspatients/").then((res) => {
        console.log("estoy en metodo get pacientes", res.status);
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
