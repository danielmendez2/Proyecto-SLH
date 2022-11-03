<template>
  <v-dialog v-model="crecimt_desarr.estado" persistent>
    <v-card>
      <v-container id="user-profile" fluid tag="section">
        <h1>Crear crecimiento y desarrollo</h1>
        <v-row justify="center">
          <v-col cols="12" md="12" >
            <base-material-card>
              <v-form>
                <v-container class="py-0">
                  <v-row justify="center">
                    <v-col cols="12" md="12" lg="3">
                      <v-text-field class="purple-input" label="Nombres" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field label="Apellidos" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="6" lg="3">
                      <v-select
                        :items="[
                          '(NIP) Número de indentificación personal',
                          '(NIT) Tarjeta de identidad',
                          '(PAP) Pasaporte',
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
                        label="Número  de documento"
                        class="purple-input"
                        type="number"
                      />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field  suffix="Kg" type="number" label="Peso" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field label="Estatura" type="number" suffix="cm" class="purple-input" />
                    </v-col>

                    <v-col cols="12" md="4">
                      <v-text-field class="purple-input" disabled label="IMC" />
                    </v-col>

                    <v-col cols="12" md="4" lg="2">
                      <v-select :items="['Femenino', 'Masculino', 'Otros']" label="Género">
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

                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        class="purple-input"
                        label="Temperatura "
                        suffix="°C"
                        type="number"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" suffix="BPM" label="Pulso" />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        class="purple-input"
                        label="Frecuencia respiratoria"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field
                        class="purple-input"
                        label="Tensión arterial"
                        suffix="mmHg"
                      />
                    </v-col>
                    <v-col cols="12" md="4" lg="3">
                      <v-text-field class="purple-input" maxlength="4" label="RH" />
                    </v-col>
                    <v-col cols="12">
                      <v-textarea auto-grow
                        class="purple-input"
                        label="Concepto médico"
                      />
                    </v-col>
                    <div class="text-xs-right">
                      <v-btn color="success" class="mr-0">Guardar</v-btn>

                      <v-btn
                        color="warning"
                        class="mr-0"
                        @click="crecimt_desarr.estado = false"
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
    crecimt_desarr: Object,
  },
  data: () => ({}),
};
</script>

