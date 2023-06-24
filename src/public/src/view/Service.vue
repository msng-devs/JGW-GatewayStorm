<template>

  <v-app id="services">
    <LoadingSpinner :is-loading="isLoading"></LoadingSpinner>
    <v-container class="fill-height" fluid>
        <NavBar></NavBar>
        <v-main>


            <v-row justify="center" align="center">
              <v-col cols="12" md="10">
                <Alters ref="alters"></Alters>
              </v-col>
            </v-row >

            <v-row justify="center" align="center">
              <v-col cols="12" md="10">

                <v-sheet :elevation="5" :rounded="true" class="m-5 pa-15">
                  <v-alert border="start" color="indigo-lighten-1" class="mb-10">
                    <v-alert-title>
                      <p class="text-h5">
                        <v-icon small>
                          mdi-lan
                        </v-icon>
                        서비스 목록
                      </p>
                    </v-alert-title>

                    <p class="py-3">현재 등록된 서비스 목록입니다.</p>
                  </v-alert>
                  <ServiceTable :services="services" @on-edit="editService"/>
                  <v-spacer></v-spacer>

                  <v-row justify="center" class="mt-10">

                    <v-btn rounded="xl" color="indigo-darken-1" @click="openAddDialog">
                      <v-icon small class="mr-3">mdi-plus-box-multiple</v-icon>
                      신규 아이템 추가
                    </v-btn>
                  </v-row>

                  <ServiceAdd ref="addDialog" @on-error="processAddError" @add-service="insertService"/>
                  <ServiceEdit ref="editDialog" @on-error="processAddError" @on-delete="deleteService" @on-update="updateService"/>
                </v-sheet>
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
import ServiceEdit from "../components/ServiceEdit.vue";
import ServiceAdd from "../components/ServiceAdd.vue";
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

//서비스 추가
const addDialog = ref(false);

const openAddDialog = () => {
  addDialog.value.openDialog();
};

const editDialog = ref(false);
const editService = (name,description,domain,id) => {
  editDialog.value.openDialog(name,description,domain,id);
}

const processAddError = (type,message) => {
  alters.value.addAlert(type,message);
}



const insertService = (service) => {
  services.value.unshift(service);
}

const deleteService = (id) => {
  const index = services.value.findIndex(service => service.id === id);
  if (index !== -1) {
    services.value = [
      ...services.value.slice(0, index),
      ...services.value.slice(index + 1)
    ];
  }
}

const updateService = (id, data) => {
  console.log(id)
  console.log(data)
  const index = services.value.findIndex(service => service.id === id);
  if (index !== -1) {
    services.value = [
      ...services.value.slice(0, index),
      { ...services.value[index], ...data },
      ...services.value.slice(index + 1)
    ];
  }
}

</script>

<style scoped>
html { overflow-y: auto }
</style>