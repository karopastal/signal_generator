<template>
  <div>
    <md-steppers>
      <md-step id="first" md-label="Signal">
         <div v-for="signal in config.signals">
            <md-radio v-model="plot.signal":value="signal.id">signal id: {{signal.id}} - {{signal.description}}</md-radio>
        </div>
      </md-step>

      <md-step id="second" md-label="Background">
        <div v-for="bg in config.backgrounds">
            <md-radio v-model="plot.background":value="bg.id">background id: {{bg.id}} - {{bg.description}}</md-radio>
        </div>
      </md-step>

      <md-step id="third" md-label="Wavelet">
        <div v-for="wavelet in config.wavelets">
            <md-radio v-model="plot.wavelet":value="wavelet.id">wavelet id: {{wavelet.id}} - {{wavelet.description}}</md-radio>
        </div>
      </md-step>
    </md-steppers>


    <div>
     <md-card>
      <md-card-content>
      <div class="text-center">
        <table>
          <tr>
            <th>Signal</th>
            <th>Background</th>
            <th>Wavelet</th>
            <th>Fluctuations</th>
          </tr>

          <tr>
            <td>{{ plot.signal }}</td>
            <td>{{ plot.background }}</td>
            <td>{{ plot.wavelet }}</td>
            <td>{{ plot.fluctuations }}</td>
          </tr>
        </table>
        </div>
        <div class="text-right">
            <md-switch v-model="plot.fluctuations">Fluctuations</md-switch>
        </div>
      </md-card-content>

      <md-card-actions>
        <md-button class="md-flat"  @click="showPlotSignalAndBgModal(plot)">Plot Signal + Background</md-button>
        <md-button class="md-warning" @click="plotCWT(plot)">Plot CWT</md-button>
      </md-card-actions>
    </md-card>
  </div>

  </div>
</template>

<script>
import PlotSignalBgModal from "@/components/Modals/PlotSignalBgModal.vue";

  export default {
    name: 'dynamic-plots',
    data: () => ({
        path: "",
        config: {
            signals: [],
            backgrounds: [],
            wavelets: []
        },
      plot: {
          signal: "-",
          background: "-",
          wavelet: "-",
          fluctuations: false,
      }
    }),
    mounted () {
        this.loadData();
      },
    methods: {
        loadData(){
            this.$axios
              .get('http://localhost:5000/api/v1/resources/signals')
              .then(response => (this.config.signals = response.data));

            this.$axios
              .get('http://localhost:5000/api/v1/resources/backgrounds')
              .then(response => (this.config.backgrounds = response.data))

            this.$axios
              .get('http://localhost:5000/api/v1/resources/wavelets')
              .then(response => (this.config.wavelets = response.data))
        },
        showPlotSignalAndBgModal(plot) {
           this.$modal.show(PlotSignalBgModal,
                {
                    plot: plot
                },
                {
                    width: 800,
                    height: 700
              });
        },
        plotCWT(plot) {
            this.$axios.post('http://localhost:5000/api/v1/resources/plot_cwt', {
                data: plot,
             }).then((response) => {
                 alert('trigger plot Modal');
             }).catch((e) => {
                console.error(e)
             })
       }
    }
  }
</script>