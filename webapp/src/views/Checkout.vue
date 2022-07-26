<template>
  <div class="container">
    <div>
      <h2 class="title">Complete seu pedido</h2>

      <div class="address-form">
        <div class="address-title">
          <p class="form-title">Endereço de Entrega</p>
          <p class="form-subtitle">
            Informe o endereço onde deseja receber seu pedido
          </p>
        </div>
        <div class="row">
          <input placeholder="CEP" />
        </div>
        <div class="row">
          <input placeholder="Rua" />
        </div>
        <div class="row">
          <input placeholder="Número" />
          <input placeholder="Complemento" />
        </div>

        <div class="row">
          <input placeholder="Bairro" />
          <input placeholder="Cidade" />
          <input placeholder="UF" />
        </div>
      </div>

      <div class="address-form">
        <div class="address-title">
          <p class="form-title">Pagamento</p>
          <p class="form-subtitle">
            O pagamento é feito na entrega. Escolha a forma que deseja pagar
          </p>
        </div>
      </div>
    </div>

    <div>
      <h2 class="title">Cafés selecionados</h2>
      <div class="coffee-cart">
        <div class="price">
          <p>Total de itens</p>
          <p>R$33,20</p>
        </div>

        <div class="price">
          <p>Entrega</p>
          <p>R$3,20</p>
        </div>

        <div class="price">
          <p class="total">Total</p>
          <p class="total">R$43,20</p>
        </div>
        <button>CONFIRMAR PEDIDO</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: grid;
  grid-template-columns: 70% 30%;
  gap: 30px;
  width: 100%;
}

.coffee-cart {
  background: #f3f2f2;
  width: 100%;
  padding: 30px;
  margin-top: 20px;
  border-radius: 6px 30px;
}

.price {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  margin: 10px 0px;
}

.total {
  font-weight: 700;
  font-size: 20px;
}

.coffee-cart button {
  background: #dbac2c;
  border: none;
  padding: 10px;
  width: 100%;
  color: white;
  font-weight: 700;
  height: 40px;
  border-radius: 6px;
}

.title {
  font-weight: bold;
  color: #403937;
}

.address-form {
  margin-top: 20px;
  background: #f3f2f2;
  border-radius: 6px;
  padding: 40px;
}

.address-title {
  margin-bottom: 40px;
}

.form-title {
  color: #403937;
  font-size: 16px;
}

.form-subtitle {
  font-size: 14px;
}

.address-form input {
  background: #eeeded;
  width: 200px;
  height: 42px;
  border: 1px solid #e6e5e5;
  border-radius: 4px;
  padding: 5px 10px;
  font-size: 14px;
}

.row {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 15px;
}
</style>
