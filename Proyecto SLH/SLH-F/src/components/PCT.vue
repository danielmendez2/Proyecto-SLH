<template>
  <v-dialog v-model="paciente.estado" persistent>
    <v-card>
      <v-container id="user-profile" fluid tag="section">
        <h1>Crear paciente</h1>
        <v-row justify="center">
          <v-col cols="12" md="12">
            <base-material-card>
              <v-form>
                <v-container class="py-0">
                  <v-row justify="center">
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" type="text" v-model="paciente.Name" label="Nombres" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="paciente.Surname" label="Apellidos" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-select
                        v-model="paciente.type_identification"
                        :items="[
                          '(CC) Cédula de ciudadanía',
                          '(CE) Cédula de extranjeria',
                          '(NIP) Número de indentificación personal',
                          '(NIT) Número de identificación tributaria',
                          '(NIT) Tarjeta de identidad',
                          '(PAP) Pasaporte',
                        ]"
                        label="Tipo de documento"
                      >
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title :id="attrs['aria-labelledby']" v-text="item"></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-text-field v-model="paciente.identification_number" type="number" label="Número  de documento" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-text-field v-model="paciente.date_of_birth" type="date" label="Fecha de nacimiento" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="4" lg="2">
                      <v-select v-model="paciente.gender" :items="['Femenino', 'Masculino', 'Otros']" label="Género">
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title :id="attrs['aria-labelledby']" v-text="item"></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="paciente.Phone" v-mask="'+57 (###) ####-###'" label="Número celular" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="paciente.Direction" label="Dirección" class="purple-input" />
                    </v-col>

                  
                    <v-col cols="12" md="4" lg="2">
                      <v-select v-model="paciente.Eps" :items="['SANITAS', 'NUEVA EPS', 'FAMISANAR', 'CAPITAL SALUD', 'ALIANSALUD', 'COMPENSAR', 'COMMEVAEPS', 'SALUD TOTAL', 'SURA', 'SOS', 'FUNDACION SALUD MIA']" label="EPS">
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title :id="attrs['aria-labelledby']" v-text="item"></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" label="Correo electrónico" v-model="paciente.email" />
                    </v-col>

                    <div class="text-xs-right">
                      <v-btn color="success" @click="procesar()" class="mr-0">Guardar</v-btn>
                      <!-- v-on="submit.prevent="procesar()" -->
                      <v-btn color="warning" class="mr-0" @click="paciente.estado = false"> cerrar </v-btn>
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
// import { Global } from '../Global';
// import axios from 'axios';
import { required, minLength, email } from "vuelidate/lib/validators";
import { mapActions } from "vuex";
// import { config } from 'vue/types/umd';
export default {
  name: "hc",

  props: {
    paciente: Object,
  },

  data() {
    return {
      date: "2018-03-02",

      // submited: false,
      paciente: {
        Name: "",
        Surname: "",
        type_identification: "",
        identification_number: "",
        Phone: "",
        Direction: "",
        gender: "",
        Eps: "",
        email: "",
        date_of_birth: "",
      },
      //servicios: [],
    };
  },

  methods: {
    allowedDates: (val) => parseInt(val.split("-")[2], 10) % 2 === 0,
    ...mapActions({
      crearPaciente: "paciente/crearPaciente",
    }),
    async crearPaciente() {
      const data = this.paciente;
      let res = await this.crearPaciente({ data });
      console.log(res);
    },
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
      // if (this.$v.$invalid) {
      //   alert("Llenar todos los campos");
      //   // console.log(this.paciente.nombres)
      //   // console.log(this.paciente.apellidos)
      //   // console.log(this.paciente.tipo_id)
      //   // console.log(this.paciente.numero_id)
      //   // console.log(this.paciente.numero_telef)
      //   // console.log(this.paciente.direccion)
      //   // console.log(this.paciente.genero)
      //   // console.log(this.paciente.eps)
      //   // console.log(this.paciente.correo)
      //   // console.log(this.paciente.fecha_nacimt)

      //   console.log("--------");

      //   return false;
      // } else {
      this.crearPaciente();
      alert("Formulario correcto");
      // }
    },
  },
  validations: {
    paciente: {
      Name: {
        required,
        minLength: minLength(2),
      },
      Surname: {
        required,
        minLength: minLength(2),
      },
      tipo_id: {
        required,
        minLength: minLength(2),
      },
      numero_id: {
        required,
        minLength: minLength(2),
      },
      Phone: {
        required,
        minLength: minLength(2),
      },
      Direction: {
        required,
        minLength: minLength(2),
      },
      genero: {
        required,
        minLength: minLength(1),
      },
      eps: {
        required,
        minLength: minLength(2),
      },
      correo: {
        required,
        minLength: minLength(2),
        email,
      },
      fecha_nacimt: {
        required,
        minLength: minLength(2),
      },
    },
  },
};
</script>
