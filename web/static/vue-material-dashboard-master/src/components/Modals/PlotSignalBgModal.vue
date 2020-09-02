<template>
        <div>
        <md-card>
          <md-card-content>
          <div v-if="isPath">
              <img v-bind:src="`${path}`">
                  A
          </div>
             <div v-else>
              B
           </div>
          </md-card-content>
        </md-card>
      </div>
</template>

<script>
export default {
   name: 'PlotSignalBgModal',
   props: ['plot'],
    mounted () {
        this.plotSignalAndBg();
    },
   data() {
    return {
        isPath: false,
        path: "http://localhost:5000/plots/"
    };
  },
    methods: {
        plotSignalAndBg() {
        this.$axios.post('http://localhost:5000/api/v1/resources/plot_signal_and_bg', {
            data: this.plot,
         }).then((response) => {
             this.path = this.path + response.data.path;
             this.isPath = true;
             console.log(this.path);
         }).catch((e) => {
            console.error(e)
         });
        }
    }
  }
</script>