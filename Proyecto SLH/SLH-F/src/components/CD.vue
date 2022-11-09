<template>
  <v-dialog v-model="crecimt_desarr.estado" persistent>
    <v-card>
      <v-footer class="sticky" color="primary">
        <h1 class="white--text">Crear crecimiento y desarrollo</h1>
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
                        v-model="crecimt_desarrollo.Name_patients"
                        label="Pacientes"
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
                      <v-text-field v-model="crecimt_desarrollo.IMC" class="purple-input" disabled label="IMC" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        maxlength="3"
                        v-model="crecimt_desarrollo.Temperature"
                        class="purple-input"
                        label="Temperatura "
                        suffix="°C"
                        type="number"
                        oninput="if(this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="crecimt_desarrollo.Pulse" class="purple-input" suffix="BPM" label="Pulso" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="crecimt_desarrollo.Breathing_frequency" class="purple-input" label="Frecuencia respiratoria" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="crecimt_desarrollo.Blood_pressure" class="purple-input" label="Tensión arterial" suffix="mmHg" />
                    </v-col>
                    <v-col cols="12">
                      <v-textarea auto-grow class="purple-input" label="Concepto médico" />
                    </v-col>
                    <div class="text-xs-right">
                      <v-btn bottom absolute right color="success" @click="crearDesarrollo()" class="mr-0">Guardar</v-btn>
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
import { Global } from "../global";
import { required, minLength, email } from "vuelidate/lib/validators";
import { mapActions } from "vuex";
export default {
  name: "cd",
  props: {
    crecimt_desarr: Object,
  },
  data() {
    return {
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

  async mounted() {
    this.pacientes = await this.getPacientes();
    console.log(this.pacientes);
  },

  methods: {
    async mounted() {
      this.pacientes = await this.getPacientes();
      console.log(this.pacientes);
    },
    async mounted() {
      console.log("array pacientes", this.paciente);
      this.getServicios();
    },
    getServicios() {
      axios.get(Global.url + "/api/Patients/listpatients/").then((res) => {
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
      crearCrecimiento: "crecimiento_api/crearCrecimiento",
      getPacientes: "pacientes_api/getPacientes",
    }),
    async crearDesarrollo() {
      this.crecimt_desarr.IMC = this.crecimt_desarr.Weight / (this.crecimt_desarr.stature * this.crecimt_desarr.stature);
      console.log("VALOR DE IMC", this.crecimt_desarr.IMC);
      const data = {
        Name_patients: this.crecimt_desarr.Name_patients,
        Weight: this.crecimt_desarr.Weight,
        stature: this.crecimt_desarr.stature,
        IMC: this.crecimt_desarr.IMC,
        Temperature: this.crecimt_desarr.Temperature,
        Pulse: this.crecimt_desarr.Pulse,
        Breathing_frequency: this.crecimt_desarr.Breathing_frequency,
        Blood_pressure: this.crecimt_desarr.Blood_pressure,
        Doctor_name: this.crecimt_desarr.Doctor_name,
      };
      let res = await this.crearCrecimiento({ data });
      console.log("respuesta de crear historia", res);
    },

    procesar() {
      if (this.$v.$invalid) {
        alert("Llenar todos los campos");
        console.log("--------");

        return false;
      } else {
        alert("Formulario correcto");
      }
    },
  },
};
</script>
