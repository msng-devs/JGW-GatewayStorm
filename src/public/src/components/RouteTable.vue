<template>

    <v-data-table
        :headers="headers"
        :items="routes"
        :items-per-page="itemsPerPage"
        item-key="id"
        :fixed-header="true"
        :search="search"
        class="elevation-0 p-5 m-5"
    >
      <template v-slot:item.role_id="{ item }">
        <v-chip color="light-blue-lighten-4">
          {{ (item.columns.role_id) ? role[item.columns.role_id] : "X"}}
        </v-chip>
      </template>
      <template v-slot:item.method_id="{ item }">
        <v-chip color="light-blue-lighten-4">
          {{ method[item.columns.method_id] }}
        </v-chip>
      </template>
      <template v-slot:item.route_option_id="{ item }">
        <v-chip color="light-blue-lighten-4">
          {{ option[item.columns.route_option_id] }}
        </v-chip>
      </template>
      <template v-slot:item.action="{ item }">
        <v-btn small rounded="xl" @click="onEdit(item)" class="mr-2" icon color="light-blue-darken-4">
          <v-icon>
            mdi-pencil
          </v-icon>
          <v-tooltip
              activator="parent"
              location="top"
          >정보 수정
          </v-tooltip>
        </v-btn>

      </template>
    </v-data-table>

</template>

<script setup>
import {ref, onMounted, defineProps, toRefs, watch, computed} from 'vue';
import router from "../router.js";
import {tr} from "vuetify/locale";

const props = defineProps({
  routes: Array,
  methods:Object,
  roles:Object,
  options:Object,
});

const {routes,methods,options,roles} = toRefs(props);

const option = options.value;
const method = methods.value;
const role = roles.value;

const search = ref('');

const headers = [
  {
    title: 'ROUTE ID',
    align: 'center',
    sortable: true,
    key: 'id',
  },
  {title: '경로', align: 'center', key: 'path'},
  {title: 'ROLE', align: 'center', key: 'role_id'},
  {title: 'HTTP METHOD', align: 'center', key: 'method_id'},
  {title: '옵션', align: 'center', key: 'route_option_id'},
  {title: '관리', align: 'center', key: 'action'}
]

const itemsPerPage = ref(10); // Or whatever number you prefer

const emits = defineEmits(['on-edit','on-add']);
const onAdd = (item) => {
  emits('on-add')
}
const onEdit = (item) => {
  emits('on-edit', item.columns)
}
</script>
