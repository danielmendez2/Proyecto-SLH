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
                      <v-text-field
                        class="purple-input"
                        v-model="historia_clinica.nombres"
                        label="Nombres"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        v-model="historia_clinica.apellidos"
                        label="Apellidos"
                        class="purple-input"
                      />
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-select
                        v-model="historia_clinica.tipo_id"
                        :items="[
                          'Cedula de ciudada',
                          'Registro civil',
                          'Tarjeta de identidad',
                          'Pasaporte',
                        ]"
                        label="Tipo de documento"
                      >
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title
                              :id="attrs['aria-labelledby']"
                              v-text="item"
                            ></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-text-field
                        v-model="historia_clinica.numero_id"
                        label="Número  de documento"
                        class="purple-input"
                      />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        v-model="historia_clinica.numero_telef"
                        label="Número telefono"
                        class="purple-input"
                      />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        v-model="historia_clinica.direccion"
                        label="Dirección"
                        class="purple-input"
                      />
                    </v-col>

                    <v-col cols="12" md="4" lg="2">
                      <v-select
                        v-model="historia_clinica.genero"
                        :items="['F', 'M']"
                        label="Género"
                      >
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title
                              :id="attrs['aria-labelledby']"
                              v-text="item"
                            ></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col>

                    <v-col cols="12" md="4">
                      <v-text-field
                        class="purple-input"
                        v-model="historia_clinica.eps"
                        label="EPS"
                      />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        class="purple-input"
                        label="Correo electrnico"
                        v-model="historia_clinica.correo"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        class="purple-input"
                        v-model="historia_clinica.ocupacion"
                        label="Ocupación"
                      />
                    </v-col>

                    <v-col cols="12">
                      <v-textarea
                        class="purple-input"
                        v-model="historia_clinica.concepto_medico"
                        label="Concepto médico"
                      />
                    </v-col>
                    <div class="text-xs-right">
                      <v-btn color="success" @click="procesar()" class="mr-0"
                        >Guardar</v-btn
                      >
                      <!-- v-on="submit.prevent="procesar()" -->
                      <v-btn
                        color="warning"
                        class="mr-0"
                        @click="historia.estado = false"
                      >
                        cerrar
                      </v-btn>
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
        nombres: "",
        apellidos: "",
        tipo_id: "",
        numero_id: "",
        numero_telef: "",
        direccion: "",
        genero: "",
        eps: "",
        correo: "",
        ocupacion: "",
        concepto_medico: "",
      },
      servicios: [],
    };
  },

  methods: {
    ...mapActions({
      crearHistoria: "historia_clinica/crearHistoria",
    }),
    async crearHistory() {
      const data = this.historia_clinica;
      let res = await this.crearHistoria({ data });
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
      if (this.$v.$invalid) {
        alert("Llenar todos los campos");
        // console.log(this.historia_clinica.nombres)
        // console.log(this.historia_clinica.apellidos)
        // console.log(this.historia_clinica.tipo_id)
        // console.log(this.historia_clinica.numero_id)
        // console.log(this.historia_clinica.numero_telef)
        // console.log(this.historia_clinica.direccion)
        // console.log(this.historia_clinica.genero)
        // console.log(this.historia_clinica.eps)
        // console.log(this.historia_clinica.correo)
        // console.log(this.historia_clinica.ocupacion)
        // console.log(this.historia_clinica.concepto_medico)

        console.log("--------");

        return false;
      } else {
        this.crearHistory();
        alert("Formulario correcto");
      }
    },
  },
  validations: {
    historia_clinica: {
      nombres: {
        required,
        minLength: minLength(2),
      },
      apellidos: {
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
      numero_telef: {
        required,
        minLength: minLength(2),
      },
      direccion: {
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
      ocupacion: {
        required,
        minLength: minLength(2),
      },
      concepto_medico: {
        required,
        minLength: minLength(2),
      },
    },
  },
};
</script>
