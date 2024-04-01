<script setup>
import {RouterView} from 'vue-router'
import NavBar from '@/components/NavBar.vue';
</script>

<template>
  <NavBar />
  <main>
    <RouterView />
  </main>
</template>


<style scoped>
  main {
    margin-left: 375px;
    width: calc(100vw - 375px);
  }
</style>