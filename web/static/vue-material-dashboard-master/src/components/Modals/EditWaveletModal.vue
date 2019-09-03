<template>
  <form>
    <md-card>
      <md-card-header>
        <h4 class="title">Wavelet ID: {{ item.id }} </h4>
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
            <label>name</label>
              <md-input v-model="name" type="text"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
          <md-field>
            <label>B</label>
              <md-input v-model="B" type="number"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
          <md-field>
            <label>C</label>
              <md-input v-model="C" type="number"></md-input>
            </md-field>
         </div>
         <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>MIN_SCALES</label>
              <md-input v-model="MIN_SCALES" type="number"></md-input>
            </md-field>
       </div>
       <div class="md-layout-item md-small-size-100 md-size-33">
            <md-field>
              <label>MAX_SCALES</label>
              <md-input v-model="MAX_SCALES" type="number"></md-input>
            </md-field>
       </div>
          <div class="md-layout-item md-size-100 text-right">
            <md-button class="md-raised md-danger" @click="Delete">Delete Wavelet</md-button>
            <md-button class="md-raised md-success" @click="Update">Update Wavelet</md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>

<script>
export default {
   name: 'EditWaveletModal',
    props: ['item']
  ,
   data() {
    return {
      description: this.item.description,
      name: this.item.wavelet.name,
      B: this.item.wavelet.B,
      C: this.item.wavelet.C,
      MAX_SCALES: this.item.wavelet.max_scales,
      MIN_SCALES: this.item.wavelet.min_scales
    };
  },
    methods: {
        Delete() {
            this.$axios.post('http://localhost:5000/api/v1/resources/delete_wavelet', {
                id: this.item.id
             }).then((response) => {
                alert("deleted successfully");
                this.$emit('close');
             }).catch((e) => {
              console.error(e)
         })
        },
        Update () {
            this.$axios.post('http://localhost:5000/api/v1/resources/update_wavelet', {
                id: this.item.id,
                type: this.item.type,
                description: this.description,
                 wavelet: {
                      description: this.description,
                      name: this.name,
                      B: this.B,
                      C: this.C,
                      min_scales: this.MIN_SCALES,
                      max_scales: this.MAX_SCALES
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