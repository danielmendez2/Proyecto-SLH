<template>
    <v-dialog v-model="cita.estado" persistent>
      <v-card>
        <v-container id="user-profile" fluid tag="section">
          <h1>Crear cita medica</h1>
          <v-row justify="center">
            <v-col cols="12" md="12">
              <base-material-card>
                <v-form>
                  <v-container class="py-0">
                    <v-row justify="center">
                      <v-col cols="12" md="4" lg="3">
                        <v-text-field
                          class="purple-input"
                          v-model="cita.fecha"
                          label="Fecha"
                        />
                      </v-col>
                      <v-col cols="12" md="4" lg="3">
                        <v-text-field
                          v-model="cita.hora"
                          label="Hora"
                          class="purple-input"
                        />
                      </v-col>
  
                      <v-col cols="12" md="6" lg="3">
                        <v-select
                          v-model="cita.nomb_doctor"
                          :items="[
                            'Cedula de ciudada',
                            'Registro civil',
                            'Tarjeta de identidad',
                            'Pasaporte',
                          ]"
                          label="Nombre del doctor"
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
                          v-model="cita.eps"
                          label="EPS"
                          class="purple-input"
                        />
                      </v-col>

                 
  
                      <v-col cols="12" md="4" lg="2">
                        <v-select
                          v-model="cita.especializacion"
                          :items="['F', 'M']"
                          label="especializacion"
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
  
  
                     
  
                 
                      <div class="text-xs-right">
                        <v-btn color="success" @click="procesar()" class="mr-0"
                          >Guardar</v-btn
                        >
                        <!-- v-on="submit.prevent="procesar()" -->
                        <v-btn
                          color="warning"
                          class="mr-0"
                          @click="cita.estado = false"
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
  export default {
    name: "cta",
  
    props: {
      cita: Object,
    },
  
    data() {
      return {
        // submited: false,
        cita: {
          fecha: "",
          hora: "",
          nomb_doctor:"",
          eps:"",
          especializacion:""

        },
        servicios:[]
      };
    },
  
    methods: {
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
          console.log(this.cita.fecha)
          console.log(this.cita.hora)
          console.log(this.cita.nomb_doctor)
          console.log(this.cita.eps)
          console.log(this.cita.especializacion)
          console.log("--------")
        
          return false;
        }
        else{
          alert("Formulario correcto");
        }
      },
    },
    validations: {
      historia_clinica: {
        fecha: {
          required,
          minLength: minLength(2),
        },
        hora: {
          required,
          minLength: minLength(2),
        },
        nomb_doctor: {
          required,
          minLength: minLength(2),
        },
        eps: {
          required,
          minLength: minLength(2),
        },
        especializacion: {
          required,
          minLength: minLength(2),
        },
      },
    },
  };
  </script>
  