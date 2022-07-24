<template>
  <div class="container">
    <router-link to="/"
      ><img src="https://i.postimg.cc/P59x6xqw/Logo.png"
    /></router-link>
    <div class="right-icons">
      <p class="location">Cachoeiro de Itapemirim, ES</p>
      <router-link to="checkout">carrinho</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 80px;
}

.right-icons {
  display: flex;
  align-items: center;
  gap: 20px;
}

.location {
  background: #ebe5f9;
  padding: 10px;
  border-radius: 6px;
  color: #4b2995;
}
</style>
