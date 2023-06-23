<template>

  <v-app id="apiRoute">
    <LoadingSpinner :is-loading="isLoading"></LoadingSpinner>
    <v-container class="fill-height" fluid>
      <NavBar></NavBar>
      <v-main>


        <v-row justify="center" align="center">
          <v-col cols="12" md="10">
            <Alters ref="alters"></Alters>
          </v-col>
        </v-row>

        <v-row justify="center" align="center">
          <v-col cols="12" md="10">

            <v-sheet :elevation="5" :rounded="true" class="m-5 pa-15">
              <v-alert border="start" color="light-blue-darken-4" class="mb-10">
                <v-alert-title>
                  <p class="text-h5">
                    <v-icon small>
                      mdi-routes
                    </v-icon>
                    Route 목록
                  </p>
                </v-alert-title>

                <p class="py-3">
                  <v-chip><b>{{ serviceName }}</b></v-chip>
                  서비스에 등록된 Router 목록입니다.
                </p>
                <p class="py-3">
                  <v-chip>
                    <v-icon class="mr-2">mdi-tag-multiple</v-icon>
                    {{ serviceDescription }}
                  </v-chip>
                </p>
                <p class="py-3">
                  <v-chip>
                    <v-icon class="mr-2">mdi-domain</v-icon>
                    <b>{{ serviceDomain }}</b></v-chip>
                </p>
                <v-spacer></v-spacer>
              </v-alert>
              <RouteTable v-if="!isLoading" :routes="routes" :methods="methods" :roles="roles" :options="routeOptions"/>
              <v-spacer></v-spacer>
              <v-row justify="center" class="mt-10">

                <v-btn rounded="xl" color="light-blue-accent-4" @click="openAddDialog">
                  <v-icon small class="mr-3">mdi-plus-box-multiple</v-icon>
                  신규 아이템 추가
                </v-btn>
              </v-row>
              <RouteAdd v-if="!isLoading" ref="addRouteDialog" :id="id" :roles="reverseObject(roles)" @on-error="processAddError" @add-route="addRoute"
                        :options="reverseObject(routeOptions)" :methods="reverseObject(methods)"></RouteAdd>
            </v-sheet>
          </v-col>
        </v-row>

      </v-main>

    </v-container>

  </v-app>

  <AuthController @on-error="processLoginCheckerError"></AuthController>
</template>

<script setup>
import {useRoute} from "vue-router";
import LoadingSpinner from "../components/LoadingSpinner.vue";
import NavBar from "../components/NavBar.vue";
import Alters from "../components/Alters.vue";
import AuthController from "../components/AuthController.vue";
import {inject, ref, watch} from "vue";
import {useAuthStore} from "../store/auth.store.js";
import {storeToRefs} from "pinia";
import router from "../router.js";
import RouteTable from "../components/RouteTable.vue";
import RouteAdd from "../components/RouteAdd.vue";

const route = useRoute()
const id = route.params.id

const alters = ref(null)

const processLoginCheckerError = (error) => {
  console.log(error)
  alters.value.addAlert('error', error);
}

const axios = inject('axios')

const authStore = useAuthStore();
const {accessToken} = storeToRefs(authStore)

const isLoading = ref(true);
const serviceName = ref('');
const serviceDomain = ref('');
const serviceDescription = ref('');
let methods = ref({})
let roles = ref({})
let routeOptions = ref({})
//route 정보 관리
const routes = ref([]);

const getRouteData = async () => {
  const response = await axios
      .get('/api/v1/service/' + id + "/apiRoute", {
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        }
      }).catch((error) => {
        switch (error.response.status) {
          case 403:
            router.push({name: 'Login'})
            break;
          default:
            alters.value.addAlert('error', error.response.data.message);
            break;
        }
      });

  return response.data;
}

const getServiceData = async () => {
  const response = await axios
      .get('/api/v1/service/' + id, {
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        }
      }).catch((error) => {
        switch (error.response.status) {
          case 403:
            router.push({name: 'Login'})
            break;
          default:
            alters.value.addAlert('error', error.response.data.message);
            break;
        }
      });

  return response.data;
}

const getMethod = async () => {
  const response = await axios
      .get('/api/v1/method', {
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        }
      }).catch((error) => {
        switch (error.response.status) {
          case 403:
            router.push({name: 'Login'})
            break;
          default:
            alters.value.addAlert('error', error.response.data.message);
            break;
        }
      });

  return response.data;
}

const getRole = async () => {
  const response = await axios
      .get('/api/v1/role', {
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        }
      }).catch((error) => {
        switch (error.response.status) {
          case 403:
            router.push({name: 'Login'})
            break;
          default:
            alters.value.addAlert('error', error.response.data.message);
            break;
        }
      });

  return response.data;
}

const getRouteOptions = async () => {
  const response = await axios
      .get('/api/v1/routeOption', {
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        }
      }).catch((error) => {
        switch (error.response.status) {
          case 403:
            router.push({name: 'Login'})
            break;
          default:
            alters.value.addAlert('error', error.response.data.message);
            break;
        }
      });

  return response.data;
}
const initData = async () => {
  routes.value = await getRouteData();

  //service
  const targetService = await getServiceData()

  serviceName.value = targetService.name;
  serviceDomain.value = targetService.domain;
  serviceDescription.value = targetService.index;

  //method 파싱
  const methodData = await getMethod();
  methods.value = methodData.reduce((acc, cur) => {
    acc[cur.id] = cur.name;
    return acc;
  }, {});

  //role 파싱
  const roleData = await getRole();
  roles.value = roleData.reduce((acc, cur) => {
    acc[cur.id] = cur.name;
    return acc;
  }, {});

  //routeOption 파싱
  const routeOptionData = await getRouteOptions();
  routeOptions.value = routeOptionData.reduce((acc, cur) => {
    acc[cur.id] = cur.name;
    return acc;
  }, {});
  isLoading.value = false;

}

const triggerInitData = async (accessToken) => {
  if (isLoading && accessToken) {
    await initData();
  }
}
watch(accessToken, triggerInitData, {immediate: true});

const reverseObject = (target) => {
  return Object.entries(target).map(([value, text]) => ({
    value,
    text,
  }));
}

//add route
const addRouteDialog = ref(false);
const openAddDialog = () => {
  addRouteDialog.value.openDialog();
}

const addRoute = (route) => {
  routes.value.push(route);
}
const processAddError = (type,message) => {
  alters.value.addAlert(type,message);
}
</script>

<style scoped>

</style>