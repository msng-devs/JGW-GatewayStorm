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
            <p class="text-center text-h6 mt-5 text-indigo-lighten-3">
              <v-icon small class="mr-3">mdi-plus-box-multiple</v-icon>
              서비스 정보 편집
            </p>
          </v-card-title>
          <v-divider class="mt-5"/>
          <v-card-item>
            <v-form>
              <v-container>
                <v-row>
                  <v-col cols="12" md="6">
                    <v-text-field
                        v-model="name"
                        label="서비스 이름*"
                        required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="6">
                    <v-text-field
                        v-model="description"
                        label="서비스 설명"
                        required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="12">
                    <v-text-field
                        v-model="domain"
                        label="서비스 도메인*"
                        required
                    ></v-text-field>
                  </v-col>
                  <small>*는 필수 필드 입니다.</small>
                </v-row>

              </v-container>
            </v-form>
          </v-card-item>
          <v-card-actions>
            <v-row>
              <v-col cols="12" md="4">
                <v-btn color="green" rounded="xl" block @click="updateService" icon>
                  <v-icon>mdi-check-bold</v-icon>
                  <v-tooltip
                      activator="parent"
                      location="bottom"
                  >수정하기
                  </v-tooltip>
                </v-btn>

              </v-col>

              <v-col cols="12" md="4">
                <v-btn color="red" rounded="xl" block @click="deleteService" icon>
                  <v-icon>mdi-trash-can</v-icon>
                  <v-tooltip
                      activator="parent"
                      location="bottom"
                  >삭제하기
                  </v-tooltip>
                </v-btn>
              </v-col>

              <v-col cols="12" md="4">
                <v-btn color="grey-darken-1" rounded="xl" block @click="isOpen = false" icon>
                  <v-icon>mdi-close-thick</v-icon>
                  <v-tooltip
                      activator="parent"
                      location="bottom"
                  >취소
                  </v-tooltip>
                </v-btn>

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
import {useAuthStore} from "../store/auth.store.js";
import {storeToRefs} from "pinia";


const id = ref(0)
const name = ref('')
const description = ref('')
const domain = ref('')

const isOpen = ref(false)

const emits = defineEmits(['onUpdate', 'onDelete', 'onError'])

const openDialog = (t_name, t_description, t_domain, t_id) => {
  console.log(t_name, t_description, t_domain, t_id)
  isOpen.value = true
  name.value = t_name
  description.value = t_description
  domain.value = t_domain
  id.value = t_id
}

const axios = inject('axios')

const authStore = useAuthStore();
const {accessToken} = storeToRefs(authStore)

//delete

const deleteService = async () => {

  const response = await axios
      .delete('/api/v1/service/' + id.value, {
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        },
      }).then((response) => {
        emits('onDelete', id.value)
        isOpen.value = false
      }).catch((error) => {
        switch (error.response.status) {
          case 400:
          case 404:
            emits('onError', 'error', error.response.data.message)
            isOpen.value = false
            break;
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

//update
const updateService = async () => {
  if (name.value === '' || domain.value === '') {
    emits('onError', 'error', '필수 필드를 입력해주세요.')
    isOpen.value = false
    return
  }
  const data = {
    name: name.value,
    domain: domain.value,
    index: description.value
  }
  const response = await axios
      .put('/api/v1/service/' + id.value, data, {
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        },
      }).then((response) => {
            emits('onUpdate', id.value, response.data)
            isOpen.value = false
          }
      ).catch((error) => {
        switch (error.response.status) {
          case 400:
          case 404:
            emits('onError', 'error', error.response.data.message)
            isOpen.value = false
            break;
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