<template>
  <v-dialog v-model="historia.estado" persistent>
    <v-card>
      <v-container id="user-profile" fluid tag="section">
        <h1>Crear historia clínica</h1>
        <v-row justify="center">
          <v-col cols="12" md="12">
            <base-material-card>
              <v-form>
                <v-container class="py-0">
                  <v-row justify="center">
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="historia_clinica.Name" label="Nombre" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="historia_clinica.Occupation" label="Ocupación" />
                    </v-col>
                    <v-col cols="12" md="6" lg="3">
                      <v-text-field v-model="historia_clinica.reason_for_consultation" label="Razón de la consulta" class="purple-input" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="historia_clinica.current_illness" label="Enfermedad actual" class="purple-input" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="historia_clinica.hour_entry_finish" type="datetime-local" label="Fecha y hora de entrada" class="purple-input" />
                    </v-col>
                    <v-col cols="12">
                      <v-textarea class="purple-input" auto-grow v-model="historia_clinica.Doctor_concept" label="Concepto médico" />
                    </v-col>
                    <!-- <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="historia_clinica.apellidos" label="Apellidos" class="purple-input" />
                    </v-col> -->

                    <!-- <v-col cols="12" md="6" lg="3">
                      <v-select
                        v-model="historia_clinica.tipo_id"
                        :items="['Cedula de ciudada', 'Registro civil', 'Tarjeta de identidad', 'Pasaporte']"
                        label="Tipo de documento"
                      >
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title :id="attrs['aria-labelledby']" v-text="item"></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col> -->

                    <!-- <v-col cols="12" md="4" lg="2">
                      <v-select v-model="historia_clinica.Doctor_concept" :items="['F', 'M']" label="Género">
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title :id="attrs['aria-labelledby']" v-text="item"></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col> -->
                    <!-- 
                    <v-col cols="12" md="4">
                      <v-text-field class="purple-input" v-model="historia_clinica.eps" label="EPS" />
                    </v-col> -->

                    <!-- <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" label="Correo electrnico" v-model="historia_clinica.correo" />
                    </v-col> -->

                    <div class="text-xs-right">
                      <v-btn color="success" @click="procesar()" class="mr-0">Guardar</v-btn>
                      <!-- v-on="submit.prevent="procesar()" -->
                      <v-btn color="warning" class="mr-0" @click="historia.estado = false"> cerrar </v-btn>
                    </div>
                  </v-row>
                </v-container>
              </v-form>
            </base-material-card>
          </v-col>

          <v-col cols="12" md="4"> </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
// import { Global } from '../Global';
// import axios from 'axios';
import { required, minLength, email } from "vuelidate/lib/validators";
// import { config } from 'vue/types/umd';
import { mapActions } from "vuex";

export default {
  name: "hc",

  props: {
    historia: Object,
  },

  data() {
    return {
      // submited: false,
      historia_clinica: {
        Name: "",
        Occupation: "",
        reason_for_consultation: "",
        current_illness: "",
        hour_entry_finish: "",
        Doctor_concept: "",
      },
      // servicios: [],
    };
  },

  methods: {
    ...mapActions({
      crearHistoria: "historia_clinica/crearHistoria",
    }),
    async crearHistory() {
      const data = {};
      //this.historia_clinica
      // Name: 1,
      // Occupation: "estudiantebbbbbbbbbbb",
      // reason_for_consultation: "vacunacdfgdfgdfgion influencia",
      // current_illness: "Ninguna",
      // hour_entry_finish: "2022-10-24T06:00:00Z",
      // Doctor_concept: "el paciente puede segufgdfgdfgdfgdfgir a vacunacion",
      // this.historia_clinica;
      let res = await this.crearHistoria({ data });
      console.log("respuesta de crear historia", res);
    },
    guardar() {
      axios
        .post(
          "http://127.0.0.1:8000/api/history/listhistory/",
          (data = {
            Name_patients: "12",
            Rh: "A+",
            Occupation: "estudiante",
            reason_for_consultation: "vacunacion influencia",
            current_illness: "Ninguna",
            hour_entry_finish: "2022-10-24T06:00:00Z",
            Doctor_concept: "el paciente puede seguir a vacunacion",
          })
        )

        .then((data) => {
          console.log(data);
          console.log("Hecho", "Paciente creado", "success");
        })
        .catch((e) => {
          console.log(e);
          console.log("Error", "Error al guardar", "error");
        });
    },
    // async crearPaciente() {
    //   const data = this.paciente;
    //   let res = await this.crearPaciente({ data });
    //   console.log(res);
    // },
    // getServicios(){
    //   let config = {
    //     headers:{
    //       'token' : Global.token
    //     }
    //   }
    //   axios.get(Global.url, config)
    //   .then()
    // },
    procesar() {
      // this.submited = true;
      // this.$v.$touch();
      if (this.$v.$invalid) {
        alert("Llenar todos los campos");
        console.log("--------");

        return false;
      } else {
        this.guardar();

        // console.log("Formulario correcto", data.Occupation );
        alert("Formulario correcto");
      }
    },
  },
  validations: {
    historia_clinica: {
      // Name_patients: {
      //   required,
      //   minLength: minLength(2),
      // },
      // Rh: {
      //   required,
      //   minLength: minLength(2),
      // },
      Occupation: {
        required,
        minLength: minLength(2),
      },
      reason_for_consultation: {
        required,
        minLength: minLength(2),
      },
      current_illness: {
        required,
        minLength: minLength(2),
      },
      hour_entry_finish: {
        required,
        minLength: minLength(2),
      },
      Doctor_concept: {
        required,
        minLength: minLength(1),
      },

      // apellidos: {
      //   required,
      //   minLength: minLength(2),
      // },
      // tipo_id: {
      //   required,
      //   minLength: minLength(2),
      // },
      // eps: {
      //   required,
      //   minLength: minLength(2),
      // },
      // correo: {
      //   required,
      //   minLength: minLength(2),
      //   email,
      // },

      // concepto_medico: {
      //   required,
      //   minLength: minLength(2),
      // },
    },
  },
};
</script>
