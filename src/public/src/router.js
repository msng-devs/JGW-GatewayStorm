import {createWebHistory, createRouter } from "vue-router";
import Login from "./view/Login.vue";
import ApiRoute from "./view/ApiRoute.vue";
import Service from "./view/Service.vue";
const routes = [
    {
        path: "/",
        name: "Login",
        component: Login,
    },
    {
        path: "/services",
        name: "Services",
        component: Service,
    },
    {
        path: "/services/:id/api-routes",
        name: "ApiRoute",
        component: ApiRoute,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;