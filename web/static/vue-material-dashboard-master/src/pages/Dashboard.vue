<template>
  <div class="content">
    <h3 align="center">Signal Discovery</h3>
    <h5 align="center">Using Wavelet Transform</h5>

    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
      >
        <md-card>
          <md-card-header data-background-color="black">
          <div class="text-right">
            <md-button class="md-top-right md-primary" @click="saveCurrentSession(current_session)">Save Changes Of Current Session</md-button>
           </div>
           <h4 class="title">Current Session: {{ current_session.name }}</h4>
          </md-card-header>
          <md-card-content>
            <sessions-table table-header-color="black"></sessions-table>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>


</template>

<script>
import {SessionsTable} from "@/components";

export default {
  components: { SessionsTable },
  mounted () {
    this.loadData();
  },
  data() {
    return {
      current_session: {
        id: -9999,
        name: "session is empty, load from the list."
      }
    }
    },
    methods: {
        loadData(){
             this.$axios
              .get('http://localhost:5000/api/v1/resources/current_sessions')
              .then(response => (this.current_session = response.data))
    },
    saveCurrentSession(current_session) {
        if (current_session.id == "-9999") {
           alert("session is empty, load from the list.")
        } else {
            this.$axios
              .get('http://localhost:5000/api/v1/resources/save_current_session')
              .then(response => (alert("saved successfully")))
        }
    }
  }
 };
</script>
