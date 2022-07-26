<template>
  <div class="container">
    <img class="image" src="https://i.postimg.cc/qRP1mkdM/Image.png" />

    <div class="category-list">
      <p class="category" v-for="category in coffee.categories">
        {{ category.name }}
      </p>
    </div>

    <p class="name">{{ coffee.name }}</p>
    <p class="description">{{ coffee.description }}</p>

    <div class="footer">
      <p class="price">
        <span class="price-span">R$</span>{{ Number(coffee.price).toFixed(2) }}
      </p>
      <div class="quantity-picker">
        <button v-on:click="decrement" class="left">-</button>
        <p>{{ quantity }}</p>
        <button v-on:click="increment" class="right">+</button>
      </div>

      <button class="buy">
        <font-awesome-icon icon="fa-solid fa-cart-shopping" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      quantity: 1,
    };
  },
  methods: {
    increment() {
      this.quantity++;
    },
    decrement() {
      if (this.quantity > 1) this.quantity--;
    },
  },
  name: "Coffee",
  props: {
    coffee: Object,
  },
};
</script>

<style scoped>
.buy {
  background: #4b2995;
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  font-size: 18px;
  border-radius: 8px;
}

.buy:hover {
  cursor: pointer;
  background: #4b5999;
}

.container {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  background: #f3f2f2;
  padding: 20px;
  border-radius: 6px 36px;
  width: 300px;
  height: 300px;
}

.quantity-picker {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.quantity-picker button {
  border: none;
  padding: 10px;
  font-size: 16px;
  background: #e6e5e5;
  color: #8047f8;
  font-weight: bold;
  width: 30px;
  height: 40px;
}

.quantity-picker .right {
  border-radius: 0px 10px 10px 0px;
}

.quantity-picker .left {
  border-radius: 10px 0px 0px 10px;
}

.quantity-picker button:hover {
  background: #dddd;
  cursor: pointer;
}

.quantity-picker p {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #272221;
  font-weight: 400;

  width: 30px;
  text-align: center;
  background: #e6e5e5;
  height: 40px;
}

.footer {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 20px;
}

.category-list {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

img {
  z-index: 1;
  position: absolute;
  top: -30px;
}

.category {
  background: #f1e9c9;
  color: #c47f17;
  border-radius: 10px;
  padding: 4px 10px;
  font-weight: 700;
  font-size: 10px;
  text-transform: uppercase;
}

.name {
  font-weight: bold;
  font-size: 20px;
}

.description {
  color: #8d8686;
  text-align: center;
  font-size: 14px;
  height: 80px;
}

.price {
  font-size: 26px;
  font-weight: bold;
}

.price-span {
  font-size: 14px;
}
</style>
