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
import {onMounted, ref} from 'vue';


const emits = defineEmits(['statusChange'])

import { signInWithRedirect, GoogleAuthProvider, GithubAuthProvider,onAuthStateChanged } from "firebase/auth";
import {auth} from '../firebase.config'

// Google 로그인
const signInWithGoogle = () => {
  const provider = new GoogleAuthProvider();
  signInWithRedirect(auth, provider);
};

// GitHub 로그인
const signInWithGithub = () => {
  const provider = new GithubAuthProvider();
  signInWithRedirect(auth, provider);
};

import {useAuthStore} from "../store/auth.store";
const authStore = useAuthStore();

onMounted(() => {
  onAuthStateChanged(auth, (currentUser) => {
    console.log(currentUser)
    authStore.setLogin(true)

  })
})
</script>

<style scoped>
</style>