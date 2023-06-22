<template>

  <header>
    <title>Login</title>
  </header>

  <v-app id="loginPage">

    <v-main>

      <v-container class="fill-height" fluid>
        <LoadingSpinner :is-loading="inLoginProcess"></LoadingSpinner>
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
                  <LoginCard @on-finish="changeInLoginProcess" @on-error="processLoginCardError"></LoginCard>
                </v-col>
              </v-row>
            </v-row>
          </v-col>


          <v-col cols="12" md="6">
            <v-row justify="center" align="center">
              <v-col cols="12" md="12" class="my-5 py-4">
                <Alters ref="alters"></Alters>
              </v-col>
            </v-row>
          </v-col>
        </v-row>

      </v-container>

    </v-main>

  </v-app>
</template>

<script setup>
import {computed, onBeforeMount, onMounted, ref, watch} from "vue";
import LoginCard from "../components/LoginCard.vue";
import LoadingSpinner from "../components/LoadingSpinner.vue";

import router from "../router.js";
import {useAuthStore} from "../store/auth.store";
import {storeToRefs} from "pinia";
import LoginChecker from "../components/AuthController.vue";
import Alters from "../components/Alters.vue";

const authStore = useAuthStore();
authStore.loadInfoFromLocalStorage()
const {isLogin} = storeToRefs(authStore)

const getInLoginProcess = () => {
  const inLoginProcessFromLocalStorage = localStorage.getItem('inLoginProcess');
  if (inLoginProcessFromLocalStorage) {
    return JSON.parse(inLoginProcessFromLocalStorage);
  } else {
    return false;
  }
}

const inLoginProcess = ref(getInLoginProcess());

const changeInLoginProcess = () => {
  inLoginProcess.value = false;
}

const handleLoginChange = (newLoginStatus) => {
  if(newLoginStatus) {
    router.push({name: 'Services'});
  }
};

watch(isLogin, handleLoginChange,{ immediate: true });


const alters = ref(null);

const processLoginCardError = (error) => {
  alters.value.addAlert('error',error);
}
</script>

<style scoped>

</style>