<template>
  <div>
      <modals-container/>

       <div>
          <md-button class="md-round md-success" @click="showNewWaveletModal">Create New Wavelet</md-button>
          </br></br>
      </div>

    <md-table v-model="wavelets" :table-header-color="tableHeaderColor">
      <md-table-row class="btn" @click="showEditWaveletModal(item)" slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID">{{ item.id }}</md-table-cell>
        <md-table-cell md-label="Type">{{ item.type }}</md-table-cell>
        <md-table-cell md-label="Desc">{{ item.description }}</md-table-cell>
        <md-table-cell md-label="Name">{{ item.wavelet.name }}</md-table-cell>
        <md-table-cell md-label="B">{{ item.wavelet.B }}</md-table-cell>
        <md-table-cell md-label="C">{{ item.wavelet.C }}</md-table-cell>
        <md-table-cell md-label="MIN_SCALES">{{ item.wavelet.min_scales }}</md-table-cell>
        <md-table-cell md-label="MAX_SCALES">{{ item.wavelet.max_scales }}</md-table-cell>
        </md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>

import NewWaveletModal from "@/components/Modals/NewWaveletModal.vue";
import EditWaveletModal from "@/components/Modals/EditWaveletModal.vue";

export default {
  name: "wavelets-table",
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      wavelets: []
    }
  },
  mounted () {
    this.loadData();
  },
  methods: {
    loadData(){
        this.$axios
          .get('http://localhost:5000/api/v1/resources/wavelets')
          .then(response => (this.wavelets = response.data))
    },
    showNewWaveletModal(){
        this.$modal.show(NewWaveletModal,
        null,
        {
            width: 656,
            height: 430
      },
      {
        'before-close': this.loadData
      });
    },
    showEditWaveletModal(item){
        this.$modal.show(EditWaveletModal,
        {
            item: item
        },
        {
            width: 656,
            height: 430
      },
      {
        'before-close': this.loadData
      }
      );
    }
  }
};
</script>
