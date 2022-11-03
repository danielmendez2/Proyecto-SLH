<template>
  <v-dialog v-model="vacuna.estado" persistent>
    <v-card>
      <v-container id="user-profile" fluid tag="section">
        <h1>Carnet de vacunas</h1>
        <v-btn class="text-xs-center" color="warning" @click="vacuna.estado = false"> cerrar </v-btn>
        <v-row justify="center">
          <v-col cols="12" md="12">
            <base-material-card>
              <v-form>
                <v-container class="py-0">
                  <v-row justify="center">
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="carnet_vacuna.Biological" label="Biológico" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" type="date" v-model="carnet_vacuna.Vaccine_date" label="Fecha aplicación" />
                    </v-col>
                    <v-col cols="12" md="6" lg="3">
                      <v-text-field class="purple-input" type="number" m v-model="carnet_vacuna.Dose" label="Dosis" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="carnet_vacuna.Factory" label="Fabricante" />
                    </v-col>
                    <v-col cols="12" md="4" lg="2">
                      <v-select v-model="carnet_vacuna.Eps" :items="['SANITAS', 'NUEVA EPS', 'FAMISANAR', 'CAPITAL SALUD', 'ALIANSALUD', 'COMPENSAR', 'COMMEVAEPS', 'SALUD TOTAL', 'SURA', 'SOS', 'FUNDACION SALUD MIA']" label="EPS">
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title :id="attrs['aria-labelledby']" v-text="item"></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="carnet_vacuna.ips" label="IPS vacunadora" />
                    </v-col>

                    <div class="text-xs-right">
                      <v-btn color="success" @click="procesar()" class="mr-0">Guardar</v-btn>
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
import { required, minLength, email } from "vuelidate/lib/validators";
import { mapActions } from "vuex";
export default {
  name: "cv",

  props: {
    vacuna: Object,
  },

  data() {
    return {
      // submited: false,
      carnet_vacuna: {
        Biological: "",
        Dose: "",
        Vaccine_date: "",
        Factory: "",
        Lot: "",
        Vaccinator_name: "",
        Data: "",
        Eps: "",
        ips: "",
      },
      //servicios: [],
    };
  },

  methods: {
    // ...mapActions({
    //   crearCarnet: "carnet_vacunas/crearCarnet",
    // }),
    // async crearHistory() {
    //   // const data = this.historia_clinica({ data });
    //   const data = {
    //     Name: 1,
    //     Occupation: "estudiantebbbbbbbbbbb",
    //     reason_for_consultation: "vacunacdfgdfgdfgion influencia",
    //     current_illness: "Ninguna",
    //     hour_entry_finish: "2022-10-24T06:00:00Z",
    //     Doctor_concept: "el paciente puede segufgdfgdfgdfgdfgir a vacunacion",
    //   };
    //   // Name: 1,
    //   // Occupation: "estudiantebbbbbbbbbbb",
    //   // reason_for_consultation: "vacunacdfgdfgdfgion influencia",
    //   // current_illness: "Ninguna",
    //   // hour_entry_finish: "2022-10-24T06:00:00Z",
    //   // Doctor_concept: "el paciente puede segufgdfgdfgdfgdfgir a vacunacion",

    //   // this.historia_clinica;
    //   let res = await this.crearHistoria({ data });
    //   console.log("respuesta de crear historia", res);
    // },
    // guardar() {
    //   axios
    //     .post(
    //       "http://127.0.0.1:8000/api/history/listhistory/",
    //       (this.historia_clinica = {
    //         Name: 2,
    //         Occupation: this.historia_clinica.Occupation,
    //         reason_for_consultation: this.historia_clinica.reason_for_consultation,
    //         current_illness: this.historia_clinica.current_illness,
    //         hour_entry_finish: this.historia_clinica.hour_entry_finish,
    //         Doctor_concept: this.historia_clinica.Doctor_concept,
    //       })
    //     )

    //     .then((data) => {
    //       console.log(data);
    //       console.log("Hecho", "Paciente creado", "success");
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //       console.log("Error", "Error al guardar", "error");
    //     });
    // },
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
        // console.log(this.historia_clinica.Name)
        // console.log(this.historia_clinica.apellidos)
        // console.log(this.historia_clinica.tipo_id)
        // console.log(this.historia_clinica.reason_for_consultation)
        // console.log(this.historia_clinica.current_illness)
        // console.log(this.historia_clinica.hour_entry_finish)
        // console.log(this.historia_clinica.Doctor_concept)
        // console.log(this.historia_clinica.eps)
        // console.log(this.historia_clinica.correo)
        // console.log(this.historia_clinica.Occupation)
        // console.log(this.historia_clinica.concepto_medico)

        console.log("--------");

        return false;
      } else {
        // this.guardar();

        // console.log("Formulario correcto", data.Occupation );
        alert("Formulario correcto");
      }
    },
  },
  validations: {
    carnet_vacuna: {
      Biological: {
        required,
        minLength: minLength(2),
      },
      Vaccine_date: {
        required,
        minLength: minLength(2),
      },
      Dose: {
        required,
        minLength: minLength(2),
      },
      Factory: {
        required,
        minLength: minLength(2),
      },
      Eps: {
        required,
        minLength: minLength(2),
      },
      Vaccinator_name: {
        required,
        minLength: minLength(1),
      },
    },
  },
};
</script>
