<template>
  <v-dialog v-model="paciente_popap.estado" persistent>
    <v-card>
      <v-footer class="sticky" color="primary">
        <h1 class="white--text">Editar paciente</h1>
        <v-spacer></v-spacer>
        <v-btn icon @click="paciente_popap.estado = false">
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
                      <v-text-field class="purple-input" type="text" v-model="paciente_popap.Name" label="Nombres" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="paciente_popap.Surname" label="Apellidos" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-select
                        v-model="paciente_popap.type_identification"
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
                      <v-text-field v-model="paciente_popap.identification_number" type="number" label="Número  de documento" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-text-field v-model="paciente_popap.date_of_birth" type="date" label="Fecha de nacimiento" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-select v-model="paciente_popap.gender" :items="['Femenino', 'Masculino', 'Otros']" label="Género">
                        <template v-slot:item="{ item, attrs, on }">
                          <v-list-item v-bind="attrs" v-on="on">
                            <v-list-item-title :id="attrs['aria-labelledby']" v-text="item"></v-list-item-title>
                          </v-list-item>
                        </template>
                      </v-select>
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="paciente_popap.Phone" v-mask="'+57 (###) ####-###'" label="Celular" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field v-model="paciente_popap.Direction" label="Dirección" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="4" lg="2">
                      <v-select
                        v-model="paciente_popap.Eps"
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
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" label="Correo electrónico" v-model="paciente_popap.email" />
                    </v-col>
                    <v-col class="text-xs-right">
                      <v-btn bottom absolute right color="success" @click="editarPaciente()" class="mr-0">Guardar</v-btn>
                    </v-col>
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
import { mapActions } from "vuex";
export default {
  name: "pc",
  props: {
    paciente_popap: Object,
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
    };
  },
  methods: {

    ...mapActions({
      _crearPaciente: "pacientes_api/crearPaciente",
      _editarPaciente: "pacientes_api/editarPaciente",
    }),
    async editarPaciente() {
      const data = {
        Name: this.paciente_popap.Name,
        Surname: this.paciente_popap.Surname,
        type_identification: this.paciente_popap.type_identification,
        identification_number: this.paciente_popap.identification_number,
        Phone: this.paciente_popap.Phone,
        Direction: this.paciente_popap.Direction,
        gender: this.paciente_popap.gender,
        Eps: this.paciente_popap.Eps,
        email: this.paciente_popap.email,
        date_of_birth: this.paciente_popap.date_of_birth,
      };

      // if (this.$refs.form.validate()) {
      //   await this._editarPaciente({ id, data });
      //   this.$refs.form.reset();
      //   this.msj("Examen editado", "green");
      //   setTimeout(() => {}, 1000);
      // } else this.msj("Ocurrio un problema", "red");

      const id = this.paciente_popap.id;
      await this._editarPaciente({ id, data });


      if (id) {
        this.alert.estado = true;
        setTimeout(() => {
          this.paciente_popap.estado = false;
        }, 1000);
        this.alert.text = "Registro editado";
      }else {
        this.alertfail.estado = true;
        this.alertfail.text = "Complete los campos";
      }

    },

    procesar() {
      alert("Formulario correcto");
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
