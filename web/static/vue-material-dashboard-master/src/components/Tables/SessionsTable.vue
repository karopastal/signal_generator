<template>
<div>
  <modals-container/>

      <div>
          <md-button class="md-round md-success" @click="showNewSessionModal">Create New Session</md-button>
          </br></br>
      </div>
    <md-table v-model="sessions" :table-header-color="tableHeaderColor">
      <md-table-row  class="btn" @click="showEditSessionModal(item)" slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID">{{ item.id }}</md-table-cell>
        <md-table-cell md-label="NAME">{{ item.name }}</md-table-cell>
        <md-table-cell md-label="Basename">{{ item.basename }}</md-table-cell>
        <md-table-cell md-label="Desc">{{ item.description }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
import EditSessionModal from "@/components/Modals/EditSessionModal.vue";
import NewSessionsModal from "@/components/Modals/NewSessionsModal.vue";

export default {
  name: "sessions-table",
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
      sessions: [],
    }
  },
  mounted () {
    this.loadData();
  },
  methods: {
    loadData(){
        this.$axios
          .get('http://localhost:5000/api/v1/resources/sessions')
          .then(response => (this.sessions = response.data))
    },
    showNewSessionModal(){
        this.$modal.show(NewSessionsModal,
        null,
        {
            width: 656,
            height: 500
      },
      {
        'before-close': this.loadData
      });
    },
    showEditSessionModal(item){
        this.$modal.show(EditSessionModal,
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
