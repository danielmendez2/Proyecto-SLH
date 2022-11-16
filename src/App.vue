<template>
  <v-app>
  <Navbar v-if="$route.path != '/Login'"/>
    <v-content class="ma-4">
      <router-view></router-view>
    </v-content>
     <Footer v-if="$route.path != '/Login'"/>
  </v-app>
 
</template>

<script>
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
export default {
  name: 'App',
  components: {
   Navbar,
   Footer
  },
  data: () => ({
    //
  }),
};
</script>
<style>
.sticky{
position: sticky;
top:0px;
z-index: 1;
}
</style>