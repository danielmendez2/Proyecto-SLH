<template>
  <v-dialog v-model="crecimt_desarr.estado" persistent>
    <v-card>
      <v-footer class="sticky" color="primary">
        <h1 class="white--text">Crecimiento y desarrollo</h1>
        <v-spacer></v-spacer>
        <v-btn icon @click="crecimt_desarr.estado = false">
          <v-icon>mdi-close-thick</v-icon>
        </v-btn>
      </v-footer>
      <v-container id="user-profile" fluid tag="section">
        <v-row justify="center">
          <v-col cols="12" md="12">
            <base-material-card>
              <v-form>
                <v-container class="py-0">
                  <v-row justify="center">
                    <v-col cols="12" md="4" lg="2">
                      <v-autocomplete
                        item-text="identification_number"
                        item-value="id"
                        v-model="crecimt_desarrollo.name_patients"
                        label="N° documento paciente"
                        :items="pacientes"
                      >
                      </v-autocomplete>
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="crecimt_desarrollo.Weight" suffix="Kg" type="number" label="Peso" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        v-model="crecimt_desarrollo.stature"
                        maxlenxgth="10"
                        label="Estatura"
                        type="number"
                        suffix="cm"
                        class="purple-input"
                      />
                    </v-col>

                    <v-col cols="12" md="4">
                      <v-text-field v-model="calcular_imc" class="purple-input" disabled label="IMC" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="crecimt_desarrollo.Temperature" class="purple-input" label="Temperatura " suffix="°C" type="number" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="crecimt_desarrollo.Pulse" class="purple-input" suffix="BPM" label="Pulso" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        v-model="crecimt_desarrollo.Breathing_frequency"
                        class="purple-input"
                        label="Frecuencia respiratoria"
                        suffix="Res/Minuto"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="crecimt_desarrollo.Blood_pressure" class="purple-input" label="Tensión arterial" suffix="mmHg" />
                    </v-col>

                    <div class="text-xs-right">
                      <v-btn bottom absolute right color="success" @click="crearCrecimiento()" class="mr-0">Registrar</v-btn>
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
    <v-snackbar class="black--text" color="success" right v-model="alert.estado">
      <h3>{{ alert.text }}</h3>

      <template v-slot:action="{ attrs }">
        <v-btn color="withe" icon v-bind="attrs" @click="alert.estado = false"><v-icon>mdi-close-thick</v-icon></v-btn>
      </template>
    </v-snackbar>
    <v-snackbar class="black--text" color="warning" right v-model="alertfail.estado">
      <h3>{{ alertfail.text }}</h3>

      <template v-slot:action="{ attrs }">
        <v-btn color="withe" icon v-bind="attrs" @click="alertfail.estado = false"><v-icon>mdi-close-thick</v-icon></v-btn>
      </template>
    </v-snackbar>
  </v-dialog>
</template>
<script>
import { required, minLength, email } from "vuelidate/lib/validators";
import { Global } from "../global";
import { mapActions } from "vuex";
import axios from "axios";
export default {
  name: "cd",
  props: {
    crecimt_desarr: Object,
  },
  data() {
    return {
      // rules: {
      //   required: (value) => !!crecimt_desarrollo.Weight || "Required.",
      //   counter: (value) => crecimt_desarrollo.Weight.length <= 3 || "Max 3 characters",
      //   email: (value) => {
      //     const pattern =
      //       /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      //     return pattern.test(value) || "Invalid e-mail.";
      //   },
      // },
      alert: {
        estado: "",
        text: "",
      },
      alertfail: {
        estado: "",
        text: "",
      },
      crecimt_desarrollo: {
        name_patients: "",
        Weight: "",
        stature: "",
        IMC: "",
        Temperature: "",
        Pulse: "",
        Breathing_frequency: "",
        Blood_pressure: "",
        Doctor_name: "",
      },

      idpaci: [],
      crecimiento: [],
      pacientes: [],
    };
  },
  computed: {
    calcular_imc() {
      let imc_local = (this.crecimt_desarrollo.IMC =
        Number(this.crecimt_desarrollo.Weight) / (Number(this.crecimt_desarrollo.stature) * Number(this.crecimt_desarrollo.stature)));
      //imc_local.padStart(4,"0");
      // imc_local = toString(imc_local);
      let a = Number(imc_local).toString().split(".");
      let b = a[1] && a[1];
      return Number(b);
    },
  },

  async mounted() {
    // this.crecimt_desarr.IMC = this.crecimt_desarr.Weight / (this.crecimt_desarr.stature * this.crecimt_desarr.stature);
    // console.log("VALOR DE IMC", this.crecimt_desarr.IMC);
    this.pacientes = await this.getPacientes();
    this.getServicios();
  },
  methods: {
    getServicios() {
      axios.get(Global.url + "Patientspatients/").then((res) => {
        console.log("estoy en metodo get pacientes", res.status);
        if (res.status == 200) {
          this.historia_cli = res.data;
          console.log((this.historia_cli.id = "1"));
        } else {
          alert("no se pudo conectar");
        }
      });
    },
    ...mapActions({
      crearCrecientoDesa: "crecimiento_api/crearCrecimiento",
      getPacientes: "pacientes_api/getPacientes",
    }),
    async crearCrecimiento() {
      const data = {
        name_patients: this.crecimt_desarrollo.name_patients,
        Weight: this.crecimt_desarrollo.Weight,
        stature: this.crecimt_desarrollo.stature,
        IMC: this.calcular_imc,
        Temperature: this.crecimt_desarrollo.Temperature,
        Pulse: this.crecimt_desarrollo.Pulse,
        Breathing_frequency: this.crecimt_desarrollo.Breathing_frequency,
        Blood_pressure: this.crecimt_desarrollo.Blood_pressure,
        Doctor_name: this.crecimt_desarrollo.Doctor_name,
      };
      console.log("imc", data.IMC);
      console.log("imc", data.Temperature);
      console.log("imc", data.Weight);
      let res = await this.crearCrecientoDesa({ data });
      if (res) {
        this.alert.estado = true;
        setTimeout(() => {
          this.crecimt_desarr.estado = false;
        }, 1000);
        this.alert.text = "Carnet registrado";
      } else {
        this.alertfail.estado = true;
        this.alertfail.text = "Complete los campos";
      }
    },
  },
};
</script>
