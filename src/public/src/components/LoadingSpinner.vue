<template>
  <div class="vl-parent">
    <loading v-model:active="isLoading"
             :can-cancel="false"
             :is-full-page="true"
             :background-color="'#000000'"
             :color="'#ffffff'"
             :opacity="0.99"
             :height="0"
             :width="0"
    >
      <slot name="default">
        <v-container class="centered-container" v-if="isLoading">
                <v-row class="text-center" justify="center" align="center">
                  <v-col cols="12" md="12" class="my-2 py-2">
                    <v-img :width="800" src="/mainlogo.png" class="mx-auto"></v-img>
                  </v-col>
                  <v-col cols="12" md="12" class="my-2 py-2">
                    <v-progress-circular
                        color="dark-blue"
                        indeterminate
                        :size="128"
                        :width="12"
                    ></v-progress-circular>
                  </v-col>
                </v-row>
              </v-container>
      </slot>
    </loading>
  </div>
</template>

<script setup>
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
import {toRefs} from "vue";

const props = defineProps({
  isLoading: {
    type: Boolean,
    default: false
  }
});

const {isLoading} = toRefs(props)

</script>

<style scoped>
.centered-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
</style>