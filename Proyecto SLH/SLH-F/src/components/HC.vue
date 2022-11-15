<template>
  <v-dialog v-model="historia.estado" persistent>
    <v-card>
      <v-footer class="sticky" color="primary">
        <h1 class="white--text">Historia clínica</h1>
        <v-spacer></v-spacer>
        <v-btn icon @click="historia.estado = false">
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
                    <v-col cols="12" md="4" lg="3">
                      <v-autocomplete
                        item-text="identification_number"
                        item-value="id"
                        v-model="historia_clinica.Name_patients"
                        label="N° documento"
                        :items="pacientes"
                      >
                      </v-autocomplete>
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="historia_clinica.Occupation" label="Ocupación" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        v-model="historia_clinica.hour_entry_finish"
                        type="datetime-local"
                        label="Fecha y hora de entrada"
                        class="purple-input"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="12">
                      <v-text-field v-model="historia_clinica.current_illness" label="Enfermedad actual" class="purple-input" />
                    </v-col>
                    <v-col cols="12">
                      <v-textarea class="purple-input" auto-grow v-model="historia_clinica.reason_for_consultation" label="Razón de la consulta" />
                    </v-col>
                    <v-col cols="12">
                      <v-textarea class="purple-input" auto-grow v-model="historia_clinica.Doctor_concept" label="Concepto médico" />
                    </v-col>
                    <v-col class="text-xs-right">
                      <v-btn bottom absolute right color="success" @click="crearHistory()" class="mr-0">Registrar</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-form>
            </base-material-card>
          </v-col>
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
import axios from "axios";
import { Global } from "../global";
import { required, minLength, email } from "vuelidate/lib/validators";
import { mapActions } from "vuex";

export default {
  name: "hc",

  props: {
    historia: Object,
  },
  data() {
    return {
      alert: {
        estado: "",
        text: "",
      },
      alertfail: {
        estado: "",
        text: "",
      },

      historia_clinica: {
        Name_patients: "",
        Rh: "",
        Occupation: "",
        reason_for_consultation: "",
        current_illness: "",
        hour_entry_finish: "",
        Doctor_concept: "",
      },

      idpaci: [],
      pacientes: [],
      rh: ["A +", "A-", "B +", "B-", "AB+", "AB-", "O+", "O-"],
    };
  },
  async mounted() {
    this.pacientes = await this.getPacientes();
    console.log(this.pacientes);
    this.getServicios();
  },
  methods: {
    getServicios() {
      axios.get(Global.url + "/api/historyhistory/").then((res) => {
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
      crearHistoria: "historia_clinica/crearHistoria",
      getPacientes: "pacientes_api/getPacientes",
    }),
    async crearHistory() {
      console.log(this.historia_clinica);
      const data = {
        Name_patients: this.historia_clinica.Name_patients,
        Name: this.historia_clinica.Name_patients,
        Occupation: this.historia_clinica.Occupation,
        Rh: this.historia_clinica.Rh,
        reason_for_consultation: this.historia_clinica.reason_for_consultation,
        current_illness: this.historia_clinica.current_illness,
        hour_entry_finish: this.historia_clinica.hour_entry_finish,
        Doctor_concept: this.historia_clinica.Doctor_concept,
      };
      let res = await this.crearHistoria({ data });
      if (res) {
        this.alert.estado = true;
        setTimeout(() => {
          this.historia.estado = false;
        }, 1000);
        this.alert.text = "Historia registrada";
      } else {
        this.alertfail.estado = true;
        this.alertfail.text = "Complete los campos";
      }
    },
  },
};
</script>
