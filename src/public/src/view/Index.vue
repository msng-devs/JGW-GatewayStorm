<template>

  <v-app id="index">
    <LoadingSpinner :is-loading="true"></LoadingSpinner>
  </v-app>

  <AuthController/>

</template>

<script setup>
import AuthController from "../components/AuthController.vue";
import router from "../router.js";
import {watch} from "vue";
import {useAuthStore} from "../store/auth.store.js";
import {storeToRefs} from "pinia";

const authStore = useAuthStore();
authStore.loadInfoFromLocalStorage()
const {isLogin} = storeToRefs(authStore)

const handleLoginChange = (newLoginStatus) => {
  if(newLoginStatus) {
    router.push({name: 'Services'});
  }
};

watch(isLogin, handleLoginChange,{ immediate: true });
</script>

<style scoped>

</style>