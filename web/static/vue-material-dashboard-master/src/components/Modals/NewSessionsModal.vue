<template>
  <form>
    <md-card>
      <md-card-header>
        <h4 class="title">New Session </h4>
      </md-card-header>

      <md-card-content>
        <div class="md-layout">
          <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Name</label>
              <md-input v-model="name" type="text"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Base Name</label>
              <md-input v-model="basename" type="text"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Description</label>
              <md-input v-model="description" type="text"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-size-100 text-left">
            <md-button class="md-raised md-success" @click="create">Create Session</md-button>
            <md-button class="md-raised" @click="$emit('close')">Close</md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>

<script>
export default {
   name: 'NewSessionsModal',
    props: ['item']
  ,
   data() {
    return {
      description: null,
      center: null,
      height: null,
      width: null,
      T: null,
      MIN_MASS: null,
      MAX_MASS: null,
      MASS_NUM: null,
      AMPLITUDE_DECAY_RATE: null
    };
  },
    methods: {
        create(){
            this.$axios.post('http://localhost:5000/api/v1/resources/new_sessions', {
                id: -1,
                name: this.name,
                basename: this.basename,
                description: this.description,
             }).then((response) => {
                alert("updated successfully");
                this.$emit('close');
             })
                .catch((e) => {
                console.error(e)
             })
           }
        }
    }
</script>