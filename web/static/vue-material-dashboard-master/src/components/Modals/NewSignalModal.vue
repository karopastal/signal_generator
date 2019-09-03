<template>
  <form>
    <md-card>
      <md-card-header>
        <h4 class="title">New Signal </h4>
        <h6> type: default_signal </h6>
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
              <label>Center</label>
              <md-input v-model="center" type="text"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Width</label>
              <md-input v-model="width" type="text"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>Height</label>
              <md-input v-model="height" type="number"></md-input>
            </md-field>
          </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
          <md-field>
            <label>MIN_MASS</label>
              <md-input v-model="MIN_MASS" type="number"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
          <md-field>
            <label>MAX_MASS</label>
              <md-input v-model="MAX_MASS" type="number"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
          <md-field>
            <label>MASS_NUM</label>
              <md-input v-model="MASS_NUM" type="number"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>T</label>
              <md-input v-model="T" type="number"></md-input>
            </md-field>
       </div>
       <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>DECAY_RATE</label>
              <md-input v-model="AMPLITUDE_DECAY_RATE" type="number"></md-input>
            </md-field>
       </div>
          <div class="md-layout-item md-size-100 text-right">
            <md-button class="md-raised md-success" @click="create">Create Signal</md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>

<script>
export default {
   name: 'NewSignalModal',
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
            this.$axios.post('http://localhost:5000/api/v1/resources/new_signal', {
                id: -1,
                type: 'default_signal',
                description: this.description,
                gaussian: {
                    center: this.center,
                    height: this.height,
                    width: this.width
                },
              range: {
                  T: this.T,
                  MIN_MASS: this.MIN_MASS,
                  MAX_MASS: this.MAX_MASS,
                  MASS_NUM: this.MASS_NUM,
                  AMPLITUDE_DECAY_RATE: this.AMPLITUDE_DECAY_RATE
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