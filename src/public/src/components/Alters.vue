<template>
  <div v-if="alerts.length >= 1">
    <v-alert
        v-for="(alert, index) in alerts"
        :key="alert.id"
        :type="alert.type"
        variant="outlined"
        closable
        @close="removeAlert(index)"
    >
      {{ alert.message }}
    </v-alert>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const alerts = ref([]);

function addAlert(type, message) {

  const id = Math.random().toString(36).substring(7);
  alerts.value.push({ id, type, message });
  console.log(alerts)
}

function removeAlert(index) {
  alerts.value.splice(index, 1);
}

defineExpose({ addAlert });

</script>

<style scoped>

</style>