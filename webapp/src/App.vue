<script setup>
import Header from "./components/Header.vue";
import CoffeeList from "./components/CoffeesList.vue";
import axios from "axios";
</script>

<template>
  <Header />
  <router-view></router-view>
</template>

<script>
export default {};
</script>

<style scoped></style>
