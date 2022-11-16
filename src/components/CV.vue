<template>
  <v-dialog v-model="vacuna.estado" persistent>
    <v-card>
      <v-footer class="sticky" color="primary">
        <h1 class="white--text">Carnet de vacunas</h1>
        <v-spacer></v-spacer>
        <v-btn icon @click="vacuna.estado = false">
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
                        v-model="carnet_vacuna.Name_patients"
                        label="N° documento paciente"
                        :items="pacientes"
                      >
                      </v-autocomplete>
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="carnet_vacuna.Biological" label="Biológico" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" type="date" v-model="carnet_vacuna.Vaccine_date" label="Fecha aplicación" />
                    </v-col>
                    <v-col cols="12" md="6" lg="2">
                      <v-text-field class="purple-input" type="number" m v-model="carnet_vacuna.Dose" label="Dosis" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="carnet_vacuna.Factory" label="Fabricante" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" v-model="carnet_vacuna.Lot" label="Lote" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-select
                        v-model="carnet_vacuna.Eps"
                        :items="[
                          'SANITAS',
                          'NUEVA EPS',
                          'FAMISANAR',
                          'CAPITAL SALUD',
                          'ALIANSALUD',
                          'COMPENSAR',
                          'COMMEVAEPS',
                          'SALUD TOTAL',
                          'SURA',
                          'SOS',
                          'FUNDACION SALUD MIA',
                        ]"
                        label="EPS"
                      >
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title :id="attrs['aria-labelledby']" v-text="item"></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col>
                    <v-col cols="12" md="4" lg="4">
                      <v-text-field class="purple-input" v-model="carnet_vacuna.Ips" label="IPS vacunadora" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-autocomplete
                        item-text="identification_number"
                        item-value="id"
                        v-model="carnet_vacuna.Vaccinator_name"
                        label="N° documento vacunador"
                        :items="vacunadores"
                      >
                      </v-autocomplete>
                    </v-col>

                    <div class="text-xs-right">
                      <v-btn bottom absolute right color="success" @click="crearVacuna()" class="mr-0">Registrar</v-btn>
                    </div>
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
  name: "cv",

  props: {
    vacuna: Object,
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
      // submited: false,
      carnet_vacuna: {
        Name_patients: "",
        Biological: "",
        Dose: "",
        Vaccine_date: "",
        Factory: "",
        Lot: "",
        Vaccinator_name: "",
        Eps: "",
        Ips: "",
      },
      //servicios: [],
      pacientes: [],
      vacunadores: [],
    };
  },
  async mounted() {
    this.pacientes = await this.getPacientes();
    this.vacunadores = await this.getVacunadores();
    this.getServicios();
  },
  methods: {
    getServicios() {
      axios.get(Global.url + "/api/Vaccinesvaccines/").then((res) => {
        console.log("estoy en metodo get pacientes", res.status);
        if (res.status == 200) {
          this.historia_cli = res.data;
          // console.log((this.historia_cli.id = "1"));
        } else {
          alert("no se pudo conectar");
        }
      });
    },
    ...mapActions({
      crearCarnet: "vacunas_api/crearVacuna",
      getVacunadores: "vacunador_api/getVacunadores",
      getPacientes: "pacientes_api/getPacientes",
    }),
    async crearVacuna() {
      console.log("datos de carnet vacunas", this.carnet_vacuna);
      const data = {
        name_patient: this.carnet_vacuna.Name_patients,
        Biological: this.carnet_vacuna.Biological,
        Dose: this.carnet_vacuna.Dose,
        Vaccine_date: this.carnet_vacuna.Vaccine_date,
        Factory: this.carnet_vacuna.Factory,
        Lot: this.carnet_vacuna.Lot,
        Vaccinator_name: this.carnet_vacuna.Vaccinator_name,
        Eps: this.carnet_vacuna.Eps,
        Ips: this.carnet_vacuna.Ips,
      };
      let res = await this.crearCarnet({ data });
      if (res) {
        this.alert.estado = true;
        setTimeout(() => {
          this.vacuna.estado = false;
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
