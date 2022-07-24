<script setup>
import Coffee from "./Coffee.vue";
</script>

<template>
  <div class="coffees">
    <div v-for="coffee in coffees">
      <Coffee :coffee="coffee" />
    </div>
  </div>
</template>
<script>
export default {
  name: "CoffeesList",
  methods: {
    async fetchCoffees() {
      const response = await fetch("http://127.0.0.1:8000/coffees/");
      const jsonResponse = await response.json();
      return jsonResponse;
    },
  },
  async created() {
    const coffees = await this.fetchCoffees();
    this.coffees = coffees;
  },
  components: {
    Coffee,
  },
  data() {
    return {
      coffees: Array,
    };
  },
};
</script>

<style scoped>
.coffees {
  margin-top: 40px;
  display: grid;
  grid-template-columns: repeat(4, calc(100% / 4));
  row-gap: 40px;
}
</style>
