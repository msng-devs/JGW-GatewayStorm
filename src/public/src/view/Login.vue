<template>

  <header>
    <title>Login</title>
  </header>

  <v-app id="loginPage">

    <v-main>

      <v-container class="fill-height" fluid>

<!--        title & banner-->

        <v-row justify="center" align="center">
          <v-col cols="12" md="5">
            <v-row justify="center" align="center">
              <v-col cols="12" md="12" class="my-2 py-2">
                <v-img :width="800" src="mainlogo.png" class="mx-auto"></v-img>
              </v-col>
            </v-row>
          </v-col>
          <v-divider
              class="ms-3"
              inset
              vertical
          ></v-divider>

<!--          login -->
          <v-col cols="12" md="6">
            <v-row>
              <v-row justify="center" align="center">
                <v-col cols="12" md="8" class="my-5 py-4">
                  <LoginCard></LoginCard>
                </v-col>
              </v-row>
            </v-row>
          </v-col>
        </v-row>

      </v-container>

    </v-main>

  </v-app>

</template>

<script setup>
import LoginCard from "../components/LoginCard.vue";
import {onMounted, watch} from "vue";
import router from "../router.js";

import {useAuthStore} from "../store/auth.store";
import {storeToRefs} from "pinia";
const authStore = useAuthStore();
const {isLogin} = storeToRefs(authStore)

const handleLoginChange = (newLoginStatus) => {
  if(newLoginStatus) {
    router.push({name: 'Services'});
  }
};

watch(isLogin, handleLoginChange);

</script>

<style scoped>

</style>