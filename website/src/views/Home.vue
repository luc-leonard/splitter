<template>
  <div class="container">

    <FileUpload></FileUpload>
  </div>
</template>

<script lang="ts">

// eslint-disable-next-line no-unused-vars

import Vue from "vue";
import {Component} from "vue-property-decorator";
import FileUpload from "@/components/FileUpload.vue";

@Component({
  components: {
    FileUpload

  },
})
export default class extends Vue {

  mounted() {
  }
}
</script>

<style>
body {
  background-image: url("../../public/bg.jpg");
}
</style>
