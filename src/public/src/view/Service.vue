<template>

  <v-app id="services">
    <LoadingSpinner :is-loading="isLoading"></LoadingSpinner>
    <v-container class="fill-height" fluid>
        <NavBar></NavBar>
        <v-main>


            <v-row justify="center" align="center">
              <v-col cols="12" md="8">
                <Alters ref="alters"></Alters>
              </v-col>
            </v-row >

            <v-row justify="center" align="center">
              <v-col cols="12" md="8">
                <ServiceTable :services="services"></ServiceTable>
              </v-col>
            </v-row>

        </v-main>

    </v-container>

  </v-app>

  <AuthController  @on-error="processLoginCheckerError"></AuthController>
</template>

<script setup>
import NavBar from "../components/NavBar.vue";
import {inject, onMounted, ref, watch} from "vue";
import Alters from "../components/Alters.vue";
import AuthController from "../components/AuthController.vue";

//Id token 관리
import {useAuthStore} from "../store/auth.store";
import {storeToRefs} from "pinia";
import router from "../router.js";
import LoadingSpinner from "../components/LoadingSpinner.vue";
import Footer from "../components/Footer.vue";
import ServiceTable from "../components/ServiceTable.vue";
const authStore = useAuthStore();
const {accessToken} = storeToRefs(authStore)

//Auth Controller 에러 처리
const alters = ref(null);
const processLoginCheckerError = (error) => {
  console.log(error)
  alters.value.addAlert('error',error);
}

//필요 데이터 불러오기
const axios = inject('axios')
const isLoading = ref(true);

//서비스 데이터 불러오기
const services = ref([]);

const getServiceData = async () => {
  const response = await axios
      .get('/api/v1/service', {
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        }
      }).catch((error) => {
        switch (error.response.status) {
          case 403:
            router.push({name: 'Login'})
            break;
          default:
            alters.value.addAlert('error',error.response.data.message);
            break;
        }
      });

  return response.data;
}

const initData = async () => {
  services.value = await getServiceData();
  isLoading.value = false;
}

const triggerInitData = async (accessToken) => {
  if(isLoading && accessToken) {
    await initData();
  }
}
watch(accessToken, triggerInitData, { immediate: true });


</script>

<style scoped>

</style>