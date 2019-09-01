<template>
  <form>
    <md-card>
      <md-card-header>
        <h4 class="title">New Background </h4>
        <h6> type: default_background </h6>
      </md-card-header>

      <md-card-content>
        <div class="md-layout">
                  <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label>Description</label>
              <md-input v-model="description" type="text"></md-input>
            </md-field>
          </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
          <md-field>
            <label>MIN_BG</label>
              <md-input v-model="MIN_BG" type="number"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
          <md-field>
            <label>MAX_BG</label>
              <md-input v-model="MAX_BG" type="number"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
          <md-field>
            <label>BG_NUM</label>
              <md-input v-model="BG_NUM" type="number"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Amplitude</label>
              <md-input v-model="amplitude" type="number"></md-input>
            </md-field>
       </div>
       <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>DECAY_RATE</label>
              <md-input v-model="BACKGROUND_DECAY_RATE" type="number"></md-input>
            </md-field>
       </div>
          <div class="md-layout-item md-size-100 text-right">
            <md-button class="md-raised md-success" @click="create">Create Background</md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>

<script>
export default {
   name: 'NewBackgroundModal',
    props: ['item']
  ,
   data() {
    return {
      description: null,
      amplitude: null,
      MIN_BG: null,
      MAX_BG: null,
      BG_NUM: null,
      BACKGROUND_DECAY_RATE: null
    };
  },
    methods: {
        create(){
            this.$axios.post('http://localhost:5000/api/v1/resources/new_background', {
                id: -1,
                type: 'default_background',
                description: this.description,
              range: {
                  amplitude: this.amplitude,
                  MIN_BG: this.MIN_BG,
                  MAX_BG: this.MAX_BG,
                  BG_NUM: this.BG_NUM,
                  BACKGROUND_DECAY_RATE: this.BACKGROUND_DECAY_RATE
              }
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