<template>

  <form>
    <md-card>
      <md-card-header>
        <h4 class="title">Signal ID: {{ item.id }} </h4>
        <h6> type: {{ item.type }} </h6>
      </md-card-header>

      <md-card-content>
        <div class="md-layout">
         <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Name</label>
              <md-input v-model="name" readonly></md-input>
            </md-field>
          </div>

         <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Basename</label>
              <md-input v-model="basename" readonly></md-input>
            </md-field>
          </div>

          <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Description</label>
              <md-input v-model="description" readonly></md-input>
            </md-field>
          </div>


          <div class="md-layout-item md-size-100 text-right">
            <md-button class="md-raised md-primary" @click="Load">Load Session</md-button>
            <md-button class="md-raised" @click="Close">Close</md-button>
          </div>

          <div class="md-layout-item md-size-100 text-left">
            <md-button class="md-raised md-danger" @click="Delete">Delete Session</md-button>
          </div>


        </div>
      </md-card-content>
    </md-card>
  </form>
</template>

<script>
export default {
   name: 'EditSessionModal',
    props: ['item']
  ,
   data() {
    return {
      name: this.item.name,
      basename: this.item.basename,
      description: this.item.description,
    };
  },
    methods: {
        Close() {
          this.$emit('close');
        },
        Delete() {
        if (confirm('Are you sure?')) {
            this.$axios.post('http://localhost:5000/api/v1/resources/delete_session', {
                id: this.item.id,
                name: this.item.name,
                basename: this.item.basename,
                description: this.item.description
             }).then((response) => {
                alert("deleted successfully");
                this.$emit('close');
             }).catch((e) => {
              console.error(e)
         })
        } else {
          console.log('Deletion aborted');
        }
        },
        Load () {
            this.$axios.post('http://localhost:5000/api/v1/resources/load_session', {
                id: this.item.id,
                name: this.item.name,
                basename: this.item.basename,
                description: this.item.description
             }).then((response) => {
                     alert('loaded successfully');
                     this.$emit('close');
             })
                .catch((e) => {
                console.error(e)
             })
           }
        }
    }
</script>