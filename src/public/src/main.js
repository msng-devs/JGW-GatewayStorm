import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { createPinia } from 'pinia'
import router from './router.js'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/styles'
import "@mdi/font/css/materialdesignicons.min.css";
import { aliases, mdi } from 'vuetify/lib/iconsets/mdi'
import {firebaseApp} from './firebase.config'
import { md1 } from 'vuetify/blueprints'
import { VDataTable } from 'vuetify/labs/VDataTable'
const app = createApp(App)
import * as labsComponents from 'vuetify/labs/components'
const pinia = createPinia()
app.use(pinia)

axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios)


const vuetify = createVuetify({
    components: {
        ...components,
        ...labsComponents,
    },
    directives,
    theme: {
        defaultTheme: 'dark'
    },
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
        },
    },
    blueprint: md1,
})

app.use(vuetify)

app.use(router)



app.mount('#app')
