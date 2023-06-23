<template>
  <div class="text-center">
    <v-row justify="center">
      <v-dialog
          v-model="isOpen"
          width="512"
          max-height="512"
      >
        <v-card>
          <v-alert :text="message" :type="type"></v-alert>
        </v-card>
      </v-dialog>
    </v-row>

  </div>
</template>

<script setup>


import {inject, ref} from "vue";

const isOpen = ref(false)
const type= ref('info')
const message = ref('')
const openDialog = (type,message) => {
  isOpen.value = true
  type.value = type
  message.value = message

}

defineExpose({
  openDialog
})

</script>