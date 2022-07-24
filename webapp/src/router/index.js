import { createRouter, createWebHistory } from "vue-router";
import Checkout from "../views/Checkout.vue";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/checkout",
    name: "Checkout",
    component: Checkout,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

export default router;
