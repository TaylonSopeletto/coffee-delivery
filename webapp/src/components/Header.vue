<template>
  <div class="container">
    <router-link to="/"
      ><img src="https://i.postimg.cc/P59x6xqw/Logo.png"
    /></router-link>
    <div class="right-icons">
      <p class="location">
        <font-awesome-icon icon="fa-solid fa-location-dot" />Cachoeiro de
        Itapemirim, ES
      </p>
      <router-link to="checkout">
        <font-awesome-icon icon="fa-solid fa-cart-shopping"
      /></router-link>
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

.right-icons a {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 5px;
  background: #f1e9c9;
  height: 40px;
  width: 40px;
  font-size: 16px;
  color: #c47f17;
}

.location {
  display: flex;
  gap: 5px;
  align-items: center;
  background: #ebe5f9;
  padding: 14px;
  height: 40px;
  border-radius: 6px;
  color: #4b2995;
}
</style>
