<template>
  <v-sheet :elevation="5" :rounded="true" class="m-5 p-5">

      <v-data-table
          :headers="headers"
          :items="services"
          :items-per-page="itemsPerPage"
          item-key="id"
          :fixed-header="true"
          :search="search"
          class="elevation-1 p-5 m-5"
      >
        <template v-slot:item.action="{ item }">
          <v-btn small @click="onEdit(item)" class="mr-2" >
            <v-icon>
              mdi-pencil
              <v-tooltip
                  activator="parent"
                  location="top"
              >정보 수정</v-tooltip>
            </v-icon>
          </v-btn>

          <v-btn small @click="onDelete(item)">
            <v-icon>
              mdi-cog
              <v-tooltip
                  activator="parent"
                  location="top"
              >Route 편집</v-tooltip>
            </v-icon>
          </v-btn>

        </template>
      </v-data-table>

  </v-sheet>

</template>

<script setup>
import {ref, onMounted, defineProps, toRefs, watch} from 'vue';

const props = defineProps({
  services: Array
});

const { services } = toRefs(props);

const search = ref('');

const headers = [
  {
    title: '서비스 ID',
    align: 'center',
    sortable: true,
    key: 'id',
  },
  { title: '이름', align: 'center', key: 'name' },
  { title: '도메인', align: 'center', key: 'domain' },
  { title: '설명', align: 'center', key: 'index' },
  { title: 'Actions', align: 'center', key: 'action' }
]

const itemsPerPage = ref(10); // Or whatever number you prefer

const onEdit = (item) => {
  console.log(`Editing ${item.id}`);
  // Add your edit logic here
};

const onDelete = (item) => {
  console.log(`Deleting ${item.id}`);
  // Add your delete logic here
};
</script>