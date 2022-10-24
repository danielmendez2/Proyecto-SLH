<template>
  <v-dialog v-model="vacuna.estado" persistent>
    <v-card>
      <v-container id="user-profile" fluid tag="section">
        <h1>Crear carnet vacunas</h1>
        <v-row justify="center">
          <v-col cols="12" md="12">
            <base-material-card>
              <v-form>
                <v-container class="py-0">
                  <v-row justify="center">
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" label="Nombres" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field label="Apellidos" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-select
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
                        label="Numero  de documento"
                        class="purple-input"
                      />
                    </v-col>

                    <div>
                      <!-- <div class="mb-6">
                        Active picker: <code>{{ activePicker || "null" }}</code>
                      </div> -->
                      <v-menu
                        ref="menu"
                        v-model="menu"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="date"
                            label="Fecha de nacimiento"
                            prepend-icon="mdi-calendar"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker
                          v-model="date"
                          :active-picker.sync="activePicker"
                          :max="
                            new Date(
                              Date.now() -
                                new Date().getTimezoneOffset() * 60000
                            )
                              .toISOString()
                              .substr(0, 10)
                          "
                          min="1950-01-01"
                          @change="save"
                        ></v-date-picker>
                      </v-menu>
                    </div>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field label="Biológico" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="3">
                      <v-text-field class="purple-input" label="Dosis" />
                    </v-col>
                    <div>
                      <!-- <div class="mb-6">
                        Active picker: <code>{{ activePicker || "null" }}</code>
                      </div> -->
                      <v-menu
                        ref="menu"
                        v-model="menu"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="date"
                            label="Fecha vacuna"
                            prepend-icon="mdi-calendar"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker
                          v-model="date"
                          :active-picker.sync="activePicker"
                          :max="
                            new Date(
                              Date.now() -
                                new Date().getTimezoneOffset() * 60000
                            )
                              .toISOString()
                              .substr(0, 10)
                          "
                          min="1950-01-01"
                          @change="save"
                        ></v-date-picker>
                      </v-menu>
                    </div>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        class="purple-input"
                        label="Fabricante"
                        type="email"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" label="Lote" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        class="purple-input"
                        label="IPS vacunadora"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" label="Nombre vacunador" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" label="Cédula del vacunador" />
                    </v-col>
                    <br>
                    <div class="text-xs-right">
                      <v-btn color="success" class="mr-0">Guardar</v-btn>

                      <v-btn
                        color="warning"
                        class="mr-0"
                        @click="vacuna.estado = false"
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
export default {
  props: {
    vacuna: Object,
    activePicker: null,
    date: null,
    menu: false,
  },
  watch: {
    menu(val) {
      val && setTimeout(() => (this.activePicker = "YEAR"));
    },
    data: () => ({}),
  },
  methods: {
    save(date) {
      this.$refs.menu.save(date);
    },
  },
  methods: {
    save(date) {
      this.$refs.menu.save(date);
    },
  },
};
</script>
