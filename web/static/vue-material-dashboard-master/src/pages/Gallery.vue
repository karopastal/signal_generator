<template>
<div>
  <img class="image" v-for="(image, i) in images" :src="image" @click="onClick(i)">
  <vue-gallery-slideshow :images="images" :index="index"  ></vue-gallery-slideshow>
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
       'http://localhost:5000/file1',
       'http://localhost:5000/file2',
    ]

    this.index = 0
  }
};
</script>
