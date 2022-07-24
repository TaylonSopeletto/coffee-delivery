<template>
  <div>
    <img class="image" src="https://i.postimg.cc/qRP1mkdM/Image.png" />
    <p class="category">Expresso</p>
    <p class="name">{{ coffee.name }}</p>
    <p class="description">{{ coffee.description }}</p>
    <p class="price">
      <span class="price-span">R$</span>{{ Number(coffee.price).toFixed(2) }}
    </p>
  </div>
</template>

<script>
export default {
  name: "Coffee",
  props: {
    coffee: Object,
  },
};
</script>

<style scoped>
div {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  background: #f3f2f2;
  padding: 20px;
  border-radius: 6px 36px;
  height: 310px;
  width: 300px;
}

img {
  position: absolute;
  top: -30px;
}

.category {
  background: #f1e9c9;
  color: #c47f17;
  border-radius: 10px;
  padding: 4px 8px;
  font-weight: 700;
}

.name {
  font-weight: bold;
  font-size: 20px;
}

.description {
  color: #8d8686;
  text-align: center;
  font-size: 14px;
}

.price {
  font-size: 26px;
  font-weight: bold;
}

.price-span {
  font-size: 14px;
}
</style>
