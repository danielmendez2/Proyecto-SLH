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
                    <v-col cols="12" md="4" lg="2">
                      <v-autocomplete
                        item-text="identification_number"
                        item-value="id"
                        v-model="historia_clinica.Name_patients"
                        label="Pacientes"
                        :items="pacientes"
                      >
                      </v-autocomplete>
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="historia_clinica.Rh" label="Rh" />
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
                      <v-text-field
                        v-model="historia_clinica.hour_entry_finish"
                        type="datetime-local"
                        label="Fecha y hora de entrada"
                        class="purple-input"
                      />
                    </v-col>
                    <v-col cols="12">
                      <v-textarea class="purple-input" auto-grow v-model="historia_clinica.Doctor_concept" label="Concepto médico" />
                    </v-col>
                    <div class="text-xs-right">
                      <v-btn color="success" @click="crearHistory()" class="mr-0">Guardar</v-btn>

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
    };
  },
  async mounted() {
    this.pacientes = await this.getPacientes();
    console.log(this.pacientes);
  },
  methods: {
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
      crearHistoria: "historia_clinica/crearHistoria",
      getPacientes: "pacientes_api/getPacientes",
    }),
    async crearHistory() {
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
      console.log("respuesta de crear historia", res);
    },

    procesar() {
      if (this.$v.$invalid) {
        alert("Llenar todos los campos");
        console.log("--------");

        return false;
      } else {
        this.guardar();

        alert("Formulario correcto");
      }
    },
  },
  validations: {
    historia_clinica: {
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
    },
  },
};
</script>
