import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth',{

    state: () => ({
        isLogin: false,
    }),
    getters: {
        getLogin(state) {
            return state.isLogin
        }
    },
    actions:{
        setLogin(status){
            this.isLogin = status
        }
    }
})