<template>
  <div>
    <modals-container/>

      <div>
          <md-button class="md-round md-success" @click="showNewBackgroundModal">Create New Background</md-button>
          </br></br>
      </div>

    <md-table v-model="backgrounds" :table-header-color="tableHeaderColor">
      <md-table-row class="btn" @click="showEditBackgroundModal(item)" slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID">{{ item.id }}</md-table-cell>
        <md-table-cell md-label="Type">{{ item.type }}</md-table-cell>
        <md-table-cell md-label="Desc">{{ item.description }}</md-table-cell>
        <md-table-cell md-label="Amplitude">{{ item.range.amplitude }}</md-table-cell>
        <md-table-cell md-label="MIN_BG">{{ item.range.MIN_BG }}</md-table-cell>
        <md-table-cell md-label="MAX_BG">{{ item.range.MAX_BG }}</md-table-cell>
        <md-table-cell md-label="BG_NUM">{{ item.range.BG_NUM  }}</md-table-cell>
        <md-table-cell md-label="DECAY_RATE">{{ item.range.BACKGROUND_DECAY_RATE }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
import NewBackgroundModal from "@/components/Modals/NewBackgroundModal.vue";
import EditBackgroundModal from "@/components/Modals/EditBackgroundModal.vue";

export default {
  name: "backgrounds-table",
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
      backgrounds: []
    }
  },
  mounted () {
    this.loadData();
  },
  methods: {
    loadData(){
        this.$axios
          .get('http://localhost:5000/api/v1/resources/backgrounds')
          .then(response => (this.backgrounds = response.data))
    },
    showNewBackgroundModal(){
        this.$modal.show(NewBackgroundModal,
        null,
        {
            width: 656,
            height: 430
      },
      {
        'before-close': this.loadData
      });
    },
    showEditBackgroundModal(item){
        this.$modal.show(EditBackgroundModal,
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
