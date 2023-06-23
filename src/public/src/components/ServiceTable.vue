<template>

    <v-data-table
        :headers="headers"
        :items="services"
        :items-per-page="itemsPerPage"
        item-key="id"
        :fixed-header="true"
        :search="search"
        class="elevation-0 p-5 m-5"
    >
      <template v-slot:item.action="{ item }">
        <v-btn small rounded="xl" @click="onEdit(item.columns)" class="mr-2" icon color="indigo-darken-1">
          <v-icon>
            mdi-pencil
          </v-icon>
          <v-tooltip
              activator="parent"
              location="top"
          >정보 수정
          </v-tooltip>
        </v-btn>

        <v-btn small rounded="xl" @click="goRoute(item)" class="mr-2" icon color="indigo-darken-1">
          <v-icon>
            mdi-routes
          </v-icon>
          <v-tooltip
              activator="parent"
              location="top"
          >Route 편집
          </v-tooltip>
        </v-btn>

      </template>
    </v-data-table>

</template>

<script setup>
import {ref, onMounted, defineProps, toRefs, watch} from 'vue';
import router from "../router.js";
const props = defineProps({
  services: Array
});
const emits = defineEmits({
  'on-edit': null,
});
const {services} = toRefs(props);

const search = ref('');

const headers = [
  {
    title: '서비스 ID',
    align: 'center',
    sortable: true,
    key: 'id',
  },
  {title: '이름', align: 'center', key: 'name'},
  {title: '도메인', align: 'center', key: 'domain'},
  {title: '설명', align: 'center', key: 'index'},
  {title: '관리', align: 'center', key: 'action'}
]

const itemsPerPage = ref(10); // Or whatever number you prefer


//서비스 편집
const onEdit = (item) => {
  console.log(item)
  emits('on-edit', item.name, item.index, item.domain,  item.id)
};

//Route로 이동
const goRoute = (item) => {
  router.push({name: 'ApiRoute', params: {id: item.value}});
};


</script>
