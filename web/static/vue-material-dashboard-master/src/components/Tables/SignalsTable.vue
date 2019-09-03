<template>
<div>
  <modals-container/>

      <div>
          <md-button class="md-round md-success" @click="showNewSignalModal">Create New Signal</md-button>
          </br></br>
      </div>
    <md-table v-model="signals" :table-header-color="tableHeaderColor">
      <md-table-row  class="btn" @click="showEditSignalModal(item)" slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID">{{ item.id }}</md-table-cell>
        <md-table-cell md-label="Type">{{ item.type }}</md-table-cell>
        <md-table-cell md-label="Desc">{{ item.description }}</md-table-cell>
        <md-table-cell md-label="Center">{{ item.gaussian.center }}</md-table-cell>
        <md-table-cell md-label="Hight">{{ item.gaussian.height }}</md-table-cell>
        <md-table-cell md-label="Width">{{ item.gaussian.width }}</md-table-cell>
        <md-table-cell md-label="T">{{ item.range.T }}</md-table-cell>
        <md-table-cell md-label="MIN_MASS">{{ item.range.MIN_MASS }}</md-table-cell>
        <md-table-cell md-label="MAX_MASS">{{ item.range.MAX_MASS }}</md-table-cell>
        <md-table-cell md-label="MASS_NUM">{{ item.range.MASS_NUM  }}</md-table-cell>
        <md-table-cell md-label="DECAY_RATE">{{ item.range.AMPLITUDE_DECAY_RATE }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
import EditSignalModal from "@/components/Modals/EditSignalModal.vue";
import NewSignalModal from "@/components/Modals/NewSignalModal.vue";

export default {
  name: "signals-table",
  components: {
  },
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      signals: []
    }
  },
  mounted () {
    this.loadData();
  },
  methods: {
    loadData(){
        this.$axios
          .get('http://localhost:5000/api/v1/resources/signals')
          .then(response => (this.signals = response.data))
    },
    showNewSignalModal(){
        this.$modal.show(NewSignalModal,
        null,
        {
            width: 656,
            height: 500
      },
      {
        'before-close': this.loadData
      });
    },
    showEditSignalModal(item){
        this.$modal.show(EditSignalModal,
        {
            item: item
        },
        {
            width: 656,
            height: 500
      },
      {
        'before-close': this.loadData
      }
      );
    }
  }
};
</script>
