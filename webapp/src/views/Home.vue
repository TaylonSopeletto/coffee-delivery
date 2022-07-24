<script setup>
import CoffeeList from "../components/CoffeesList.vue";
</script>
<template>
  <div class="landing-page">
    <div>
      <h1 class="title">
        Encontre o café perfeito<br />
        para qualquer hora do dia
      </h1>
      <h2 class="description">
        Com o Coffee Delivery você recebe seu café onde estiver, a qualquer hora
      </h2>
      <div class="description-items-wrapper">
        <div class="description-list">
          <div>
            <p>Compra simples e segura</p>
          </div>
          <div>
            <p>Entrega rápida e rastreada</p>
          </div>
        </div>
        <div class="description-list">
          <div>
            <p>Embalagem mantém o café intacto</p>
          </div>
          <div>
            <p>O café chega fresquinho até você</p>
          </div>
        </div>
      </div>
      <h3 class="subtitle">Nossos Cafés</h3>
    </div>

    <img src="https://i.postimg.cc/TwmCypKq/Imagem.png" />
  </div>
  <CoffeeList />
</template>

<style scoped>
.landing-page {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
}

.title {
  font-size: 48px;
  color: #403937;
  font-weight: 800;
}

.description {
  color: #403937;
  font-stretch: 100;
  font-weight: 400;
  margin-bottom: 40px;
  margin-top: 40px;
}

.description-items-wrapper {
  display: flex;
  gap: 20px;
}

.description-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  font-size: 16px;
}

.subtitle {
  font-size: 32px;
  color: #403937;
  font-weight: 800;
  margin-top: 100px;
}
</style>
