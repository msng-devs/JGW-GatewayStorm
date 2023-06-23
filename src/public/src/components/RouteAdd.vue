<template>
  <div class="text-center">
    <v-row justify="center">
      <v-dialog
          v-model="isOpen"
          width="1024"
          max-height="1024"
      >
        <v-card>
          <v-card-title>
            <p class="text-center text-h6 mt-5 text-indigo-lighten-3"><v-icon small class="mr-3">mdi-plus-box-multiple</v-icon> 신규 Route 추가</p>
          </v-card-title>
          <v-divider class="mt-5"/>
          <v-card-item>
            <v-form>
              <v-container>
                <v-row>
                  <v-col cols="12" md="12">
                    <v-text-field
                        v-model="path"
                        label="서비스 이름*"
                        required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="6">
                    <v-select
                        v-model="method"
                        :items="methods"
                        label="HTTP Method*"
                        item-value="value"
                        item-text="text"
                    ></v-select>
                  </v-col>
                  <v-col cols="12" md="6">
                    <v-select
                        v-model="option"
                        :items="options"
                        label="라우팅 옵션*"
                        item-value="value"
                        item-text="text"
                    ></v-select>
                  </v-col>
                  <v-col cols="12" md="12">
                    <v-select
                        v-show="option === '4'"
                        v-model="role"
                        :items="roles"
                        label="권한"
                        item-value="value"
                        item-text="text"
                    ></v-select>
                  </v-col>
                  <small>*는 필수 필드 입니다.</small>
                </v-row>

              </v-container>
            </v-form>
          </v-card-item>
          <v-card-actions>
            <v-row>
              <v-col cols="12" md="6">
                <v-btn color="green" rounded="xl" block @click="createRoute" icon><v-icon>mdi-check-bold</v-icon><v-tooltip
                    activator="parent"
                    location="bottom"
                >추가하기
                </v-tooltip></v-btn>
              </v-col>

              <v-col cols="12" md="6">
                <v-btn color="red" rounded="xl" block @click="isOpen = false" icon><v-icon>mdi-close-thick</v-icon><v-tooltip
                    activator="parent"
                    location="bottom"
                >취소
                </v-tooltip></v-btn>
              </v-col>

            </v-row>

          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script setup>


import {inject, ref} from "vue";
import DialogResponse from "./DialogResponse.vue";
import {useAuthStore} from "../store/auth.store.js";
import {storeToRefs} from "pinia";
import router from "../router.js";

const emits = defineEmits(['onError','addApiRoute'])

const isOpen = ref(false)

const openDialog = () => {
  isOpen.value = true
}
const props = defineProps({
  id: {
    type: Number,
  },
  roles: {
    type: Object,
  },
  options: {
    type: Object,
  },
  methods: {
    type: Object,
  },
})


const roles = props.roles
const options = props.options
const methods = props.methods
console.log(methods)

const path = ref('')
const role = ref(null)
const method = ref(null)
const option = ref(null)
const id = props.id
const axios = inject('axios')

const authStore = useAuthStore();
const {accessToken} = storeToRefs(authStore)

const createRoute = async () => {
  if(path.value === '' || method.value === '' || option.value === ''){
    emits('onError', 'error','필수 필드를 입력해주세요.')
    isOpen.value = false
    return
  }
  const data = {

    path: path.value,
    methods: method.value,
    option: option.value,
    role: role.value,
  }
  const response = await axios
      .post('/api/v1/service/'+id+"/apiRoute", data ,{
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        },

      }).then((response) => {
        emits('addApiRoute', response.data)
        isOpen.value = false
      })
      .catch((error) => {
        switch (error.response.status) {
          case 400:
          case 404:
            emits('onError', 'error', error.response.data.message)
            isOpen.value = false
            return;

          case 403:
            emits('onError', 'error', "인증에 실패했습니다.")
            isOpen.value = false
            break;
          default:
            emits('onError', 'error', '알 수 없는 에러가 발생했습니다.')
            isOpen.value = false
            break;
        }
      });

}

defineExpose({
  openDialog
})

</script>