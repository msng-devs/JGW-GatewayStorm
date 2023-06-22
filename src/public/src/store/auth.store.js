import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth',{

    state: () => ({
        isLogin: false,
        accessToken: null,
    }),
    getters: {
        getLogin(state) {
            return state.isLogin
        },
        getAccessToken(state) {
            return state.accessToken
        }
    },
    actions:{
        setLogin(status){
            this.isLogin = status
            localStorage.setItem('isLogin', status)
        },
        setAccessToken(token){
            this.accessToken = token
            localStorage.setItem('accessToken', token)
        },
        loadInfoFromLocalStorage() {
            const loginFromLocalStorage = localStorage.getItem('isLogin');
            if (loginFromLocalStorage) {
                this.isLogin = JSON.parse(loginFromLocalStorage);
            }
        },
    }
})