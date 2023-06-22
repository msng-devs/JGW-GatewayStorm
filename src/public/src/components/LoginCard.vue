<template>
  <v-card>

    <v-card-title class="text-center my-5 py-5">
      <p class="text-h5">Login with Jaram Groupware Account</p>
    </v-card-title>
    <v-row class="my-3">
      <v-divider></v-divider>
    </v-row>
    <v-card-subtitle class="text-center my-3">
      <p class="text-h6">계속하려면 개발자 계정으로 로그인하세요.</p>
    </v-card-subtitle>


    <v-card-item>

      <v-row justify="center" align="center" class="my-5">
        <v-col cols="12" sm="3">
          <v-spacer></v-spacer>
        </v-col>
        <v-col cols="12" sm="6">
          <v-btn @click="signInWithGoogle()" block color="white" dark>
            <v-icon left>mdi-google</v-icon>
            구글로 로그인
          </v-btn>
        </v-col>
        <v-col cols="12" sm="3">
          <v-spacer></v-spacer>
        </v-col>

        <v-col cols="12" sm="3">
          <v-spacer></v-spacer>
        </v-col>
        <v-col cols="12" sm="6">
          <v-btn @click="signInWithGithub()" block color="black" dark>
            <v-icon left>mdi-github</v-icon>
            깃허브로 로그인
          </v-btn>
        </v-col>
        <v-col cols="12" sm="3">
          <v-spacer></v-spacer>
        </v-col>
      </v-row>

    </v-card-item>
  </v-card>
</template>

<script setup>

import {GithubAuthProvider, GoogleAuthProvider, onAuthStateChanged, signInWithRedirect, signOut,} from "firebase/auth";
import {auth} from '../firebase.config'
import {useAuthStore} from "../store/auth.store";
import {inject, onMounted} from "vue";
import {tr} from "vuetify/locale";

const emits = defineEmits(['onFinish', 'onError'])

const authStore = useAuthStore();
authStore.loadInfoFromLocalStorage()

// Google 로그인
const signInWithGoogle = async () => {
  localStorage.setItem('inLoginProcess', 'true')

  const provider = new GoogleAuthProvider();

  await signInWithRedirect(auth, provider)

};

// GitHub 로그인
const signInWithGithub = async () => {
  localStorage.setItem('inLoginProcess', 'true')

  const provider = new GithubAuthProvider();

  await signInWithRedirect(auth, provider)
};

const axios = inject('axios')

const checkServer = async (token) => {
  try {
    const response = await axios.get('/api/v1/ping/auth', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log("Server And User Role Check Success");
    return true;
  } catch (error) {
    if (error.response) {
      switch (error.response.status) {
        case 403:
          console.log('403 error: Forbidden');
          emits('onError', '해당 시스템에 접근할 권한이 없습니다. 관리자에게 문의하세요 ')
          break;
        case 404:
        case 500:
          console.log('404 error: Not Found');
          emits('onError', '서버 연결중 에러가 발생했습니다. 다시 시도해 주세요.')
          break;

        default:
          emits('onError', '알 수 없는 에러가 발생했습니다. 다시 시도해 주세요.')
          break;
      }
    } else if (error.request) {
      emits('onError', '서버에 연결할 수 없습니다. 네트워크 상태를 확인해주세요.')
    }

    return false;
  }
}



onMounted(async () => {
  await onAuthStateChanged(auth, async (user) => {
    if (user) {
      const token = await user.getIdToken()
      const status = await checkServer(token)
      console.log(token)
      if(!status) {
        authStore.setLogin(false)
        await signOut(auth);
        emits('onFinish')
        localStorage.setItem('inLoginProcess', 'false')
        console.log("Login Fail")
      } else{
        console.log("Login Success");
        authStore.setLogin(true)
        emits('onFinish')
        localStorage.setItem('inLoginProcess', 'false')
      }
    } else {
      localStorage.setItem('inLoginProcess', 'false')
      authStore.setLogin(false)
      emits('onError', '로그인에 실패했습니다.')
    }
  });


})
</script>

<style scoped>
</style>