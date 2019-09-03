<template>
<div>
  <vue-gallery-slideshow :images="images" :index="index" ></vue-gallery-slideshow>
    <div>
      <div
        class="md-layout-item md-medium-size-50 md-xsmall-size-50 md-size-55"
      >
        <md-card>
          <md-card-header data-background-color="black">
            <h4 class="title">narrow vs wide sigma</h4>
            <p class="category"></p>
          </md-card-header>
          <md-card-content>
          <h6>narrow</h6>
            <img src="http://localhost:5000/gallery/width-narrow.png">
          <h6>wide</h6>
            <img src="http://localhost:5000/gallery/width-wide.png">
          </md-card-content>
        </md-card>
      </div>
      <div
        class="md-layout-item md-medium-size-50 md-xsmall-size-50 md-size-55"
      >
        <md-card>
          <md-card-header data-background-color="black">
            <h4 class="title">fine vs coarse: amplitude decay</h4>
            <p class="category"></p>
          </md-card-header>
          <md-card-content>
            <h6>fine</h6>
            <img src="http://localhost:5000/gallery/decay-fine.png">
           <h6>coarse</h6>
            <img src="http://localhost:5000/gallery/decay-coarse.png">
          </md-card-content>
        </md-card>
      </div>
      <div
        class="md-layout-item md-medium-size-50 md-xsmall-size-50 md-size-55"
      >
        <md-card>
          <md-card-header data-background-color="black">
            <h4 class="title">fine vs coarse: frequency as a function of mass</h4>
            <p class="category"></p>
          </md-card-header>
          <md-card-content>
            <h6>fine</h6>
            <img src="http://localhost:5000/gallery/freq-mass-fine.png">
            <h6>coarse</h6>
            <img src="http://localhost:5000/gallery/freq-mass-coarse.png">
          </md-card-content>
        </md-card>
      </div>
            <div
        class="md-layout-item md-medium-size-50 md-xsmall-size-50 md-size-55"
      >
        <md-card>
          <md-card-header data-background-color="black">
            <h4 class="title">fine vs coarse: sigma as a function of mass</h4>
            <p class="category"></p>
          </md-card-header>
          <md-card-content>
            <h6>fine</h6>
            <img src="http://localhost:5000/gallery/width-mass-fine.png">
            <h6>coarse</h6>
            <img src="http://localhost:5000/gallery/width-mass-coarse.png">
          </md-card-content>
        </md-card>
      </div>
     </div>
</div>
</template>

<script>
import VueGallerySlideshow from 'vue-gallery-slideshow'

export default {
  components: {
    VueGallerySlideshow
  },
  methods: {
    onClick(i) {
      console.log(i);
      this.index = i;
    }
  },
  data() {
    this.images = [
       'http://localhost:5000/gallery/width-narrow.png',
       'http://localhost:5000/gallery/width-wide.png',
       'http://localhost:5000/gallery/decay-fine.png',
       'http://localhost:5000/gallery/decay-coarse.png',
       'http://localhost:5000/gallery/freq-mass-fine.png',
       'http://localhost:5000/gallery/freq-mass-coarse.png',
       'http://localhost:5000/gallery/width-mass-fine.png',
       'http://localhost:5000/gallery/width-mass-coarse.png',
    ]

    this.index = 0
  }
};
</script>
