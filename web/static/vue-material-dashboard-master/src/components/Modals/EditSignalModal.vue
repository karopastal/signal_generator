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
          <div class="md-layout-item md-size-100 text-left">
            <md-button class="md-raised md-danger" @click="Delete">Delete Signal</md-button>
            <md-button class="md-raised md-success" @click="Update">Update Signal</md-button>
            <md-button class="md-raised" @click="Close">Close</md-button>
          </div>


        </div>
      </md-card-content>
    </md-card>
  </form>
</template>

<script>
export default {
   name: 'EditSignalModal',
    props: ['item']
  ,
   data() {
    return {
      description: this.item.description,
      center: this.item.gaussian.center,
      height: this.item.gaussian.height,
      width: this.item.gaussian.width,
      T: this.item.range.T,
      MIN_MASS: this.item.range.MIN_MASS,
      MAX_MASS: this.item.range.MAX_MASS,
      MASS_NUM: this.item.range.MASS_NUM,
      AMPLITUDE_DECAY_RATE: this.item.range.AMPLITUDE_DECAY_RATE
    };
  },
    methods: {
        Close() {
          this.$emit('close');
        },
        Delete() {
            this.$axios.post('http://localhost:5000/api/v1/resources/delete_signal', {
                id: this.item.id
             }).then((response) => {
                alert("deleted successfully");
                this.$emit('close');
             }).catch((e) => {
              console.error(e)
         })
        },
        Update () {
            this.$axios.post('http://localhost:5000/api/v1/resources/update_signal', {
                id: this.item.id,
                type: this.item.type,
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