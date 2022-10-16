<template>
    <v-container
      id="user-profile"
      fluid
      tag="section"
    >
      <v-row justify="center">
        <v-col
          cols="12"
          md="8"
        >
          <base-material-card>
            <!-- <template v-slot:heading>
              <div class="display-2 font-weight-light">
                Edit Profile
              </div>
  
              <div class="subtitle-1 font-weight-light">
                Complete your profile
              </div>
            </template> -->
  
            <v-form>
              <v-container class="py-0">
                <v-row>
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-text-field
                      label="Company (disabled)"
                      disabled
                    />
                  </v-col>
  
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-text-field
                      class="purple-input"
                      label="Nombres"
                    />
                  </v-col>
  
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-text-field
                      label="Apellidos"
                      class="purple-input"
                    />
                  </v-col>
  
                  <v-col
                    cols="12"
                    md="6"
                  >
                    <v-text-field
                      label="Tipo de documento -----lista"
                      class="purple-input"
                    />
                  </v-col>
  
                  <v-col
                    cols="12"
                    md="6"
                  >
                    <v-text-field
                      label="Numero  de documento"
                      class="purple-input"
                    />
                  </v-col>
  
                  <v-col cols="12" md="4">
                    <v-text-field
                      label="Numero telefono"
                      class="purple-input"
                    />
                  </v-col>
  
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-text-field
                      label="Dirección"
                      class="purple-input"
                    />
                  </v-col>
  
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-text-field
                      label="Genero---lista"
                      class="purple-input"
                    />
                  </v-col>
  
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-text-field
                      class="purple-input"
                      label="EPS"
                     
                    />
                  </v-col>
                  
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-text-field
                      class="purple-input"
                      label="Correo electronico"
                      type="email"
                    />
                  </v-col>
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-text-field
                      class="purple-input"
                      label="Ocupación"
                     
                    />
                  </v-col>
                  
                  <v-col cols="12">
                    <v-textarea
                      class="purple-input"
                      label="About Me"
                      value="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    />
                  </v-col>
  
                  <v-col
                    cols="12"
                    class="text-right"
                  >
                    <v-btn
                      color="success"
                      class="mr-0"
                    >
                      Update Profile
                    </v-btn>
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
          </base-material-card>
        </v-col>
  
        <v-col
          cols="12"
          md="4"
        >
    
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
    export default {
      //
    }
  </script>
  