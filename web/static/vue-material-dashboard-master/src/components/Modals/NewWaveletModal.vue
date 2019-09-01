<template>
  <form>
    <md-card>
      <md-card-header>
        <h4 class="title">New Wavelet </h4>
        <h6> type: default_wavelet </h6>
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
            <md-button class="md-raised md-success" @click="create">Create Wavelet</md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>

<script>
export default {
   name: 'NewWaveletModal',
    props: ['item']
  ,
   data() {
    return {
      description: null,
      name: 'cmor',
      B: null,
      C: null,
      MAX_SCALES: null,
      MIN_SCALES: null
    };
  },
    methods: {
        create(){
            this.$axios.post('http://localhost:5000/api/v1/resources/new_wavelet', {
              id: -1,
              type: 'default_wavelet',
              description: this.description,
              wavelet: {
                  description: this.description,
                  name: this.name,
                  B: this.B,
                  C: this.C,
                  min_scales: this.MAX_SCALES,
                  max_scales: this.MIN_SCALES
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