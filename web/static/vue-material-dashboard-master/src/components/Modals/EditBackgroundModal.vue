<template>
  <form>
    <md-card>
      <md-card-header>
        <h4 class="title">Background ID: {{ item.id }} </h4>
        <h6> type: {{ item.type }} </h6>
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
            <md-button class="md-raised md-danger" @click="Delete">Delete Background</md-button>
            <md-button class="md-raised md-success" @click="Update">Update Background</md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>

<script>
export default {
   name: 'EditBackgroundModal',
    props: ['item']
  ,
   data() {
    return {
      description: this.item.description,
      amplitude: this.item.range.amplitude,
      MIN_BG: this.item.range.MIN_BG,
      MAX_BG: this.item.range.MAX_BG,
      BG_NUM: this.item.range.BG_NUM,
      BACKGROUND_DECAY_RATE: this.item.range.BACKGROUND_DECAY_RATE
    };
  },
    methods: {
        Delete() {
            this.$axios.post('http://localhost:5000/api/v1/resources/delete_background', {
                id: this.item.id
             }).then((response) => {
                alert("deleted successfully");
                this.$emit('close');
             }).catch((e) => {
              console.error(e)
         })
        },
        Update () {
            this.$axios.post('http://localhost:5000/api/v1/resources/update_background', {
                id: this.item.id,
                type: this.item.type,
                description: this.description,
              range: {
                  amplitude: this.amplitude,
                  MIN_BG: this.MIN_BG,
                  MAX_BG: this.MAX_BG,
                  BG_NUM: this.BG_NUM,
                  BACKGROUND_DECAY_RATE: this.BACKGROUND_DECAY_RATE
              }
             }).then((response) => {
                     alert('updated successfully');
                     this.$emit('close');
             })
                .catch((e) => {
                console.error(e)
             })
           }
        }
    }
</script>