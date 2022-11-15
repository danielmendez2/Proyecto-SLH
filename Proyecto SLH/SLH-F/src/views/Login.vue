<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8" lg="7">
            <v-card class="elevation-12">
              <v-window v-model="step">
                <v-window-item :value="1">
                  <v-col cols="12" md="8" lg="12">
                    <v-card-text class="mt-12">
                      <h1 class="text-center display-2" style="color: #03a9f4">Iniciar sesión</h1>
                      <br />
                      <h4 class="text-center mt-4">Brigadas de salud</h4>
                      <v-form>
                        <v-text-field label="Email" name="Email" prepend-icon="email" type="text" color="#03A9F4" v-model="usuario" />
                        <v-text-field
                          id="password"
                          label="Password"
                          name="password"
                          prepend-icon="lock"
                          type="password"
                          color="#03A9F4"
                          v-model="contraseña"
                        />
                      </v-form>
                      <h3 class="text-center mt-4">Olvidaste tu contraseña ?</h3>
                    </v-card-text>
                    <div class="text-center mt-3">
                      <v-btn rounded color="#03A9F4" dark v-on:click="loginAccess()">Iniciar sesión</v-btn>
                    </div>
                  </v-col>
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      usuario: "",
      contraseña: "",
    };
  },
  mounted() {
    if (localStorage.auth) {
      this.$router.push("/");
    }
  },
  methods: {
    ...mapActions({
      LOGIN: "usuario/loginUsuario",
    }),
    async loginAccess() {
      let data = {
        usuario: this.usuario,
        password: this.contraseña,
      };
      let res = await this.LOGIN({ data });

      if (res == 200) {
        return this.$router.push("/");
      } else {
        alert("No se pudo");
      }
    },
  },
};
</script>
