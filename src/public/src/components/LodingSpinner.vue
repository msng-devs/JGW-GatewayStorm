<template>
  <div class="vld-parent">
    <loading :active="isLoading"
             :can-cancel="true"
             :on-cancel="onCancel"
             :is-full-page="fullPage">

    </loading>

    <label><input type="checkbox" v-model="fullPage">Full page?</label>
  </div>
</template>

<script setup>
import Loading from 'vue-loading-overlay';
</script>

<style scoped>

</style>