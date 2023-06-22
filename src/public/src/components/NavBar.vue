<template>
    <v-app-bar color="grey-darken-4" class="py-3">

      <v-toolbar-title><v-img :width="200" src="mainlogo.png"></v-img></v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn color="indigo-lighten-2" class="ma-2">
        <v-icon class="mx-2" icon="mdi-lan"></v-icon>
        Services
      </v-btn>

      <v-btn color="indigo-lighten-2" @click="reload">
        <v-icon class="mx-2" icon="mdi-cached"></v-icon>
        Gateway Reload
      </v-btn>

      <v-btn color="indigo-lighten-2" @click="logout">
        <v-icon class="mx-2" icon="mdi-logout"></v-icon>
        Logout
      </v-btn>
    </v-app-bar>
</template>

<script setup>

import router from "../router.js";
import { signOut } from 'firebase/auth';
import { auth } from '../firebase.config';
import {useAuthStore} from "../store/auth.store";
import {storeToRefs} from "pinia";
const authStore = useAuthStore();

const props = defineProps({
  location: {
    type: String,
    default: 'Service'
  }
})

const goHome = () => {
  router.push({name: 'Services'});
}

const logout = async () => {
  try {
    await signOut(auth);
    console.log('User logged out');
    authStore.setLogin(false)
    console.log(authStore.isLogin);
  } catch (error) {
    console.error('Failed to log out', error);
  }
};

</script>

<style scoped>

</style>