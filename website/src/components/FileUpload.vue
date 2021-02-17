<template>
    <b-btn class="file-drop" @drop="handleFileDrop">
      DROP A MUSIC HERE :)
    </b-btn>
</template>

<script lang="ts">

// eslint-disable-next-line no-unused-vars
import Vue from "vue";
import {Component} from "vue-property-decorator";
import axios from "axios";

@Component({
  components: {

  },
})
export default class FileUpload extends Vue {

  handleFileDrop(e: DragEvent) {
    let droppedFiles = e.dataTransfer?.files;
    if (droppedFiles == null) {
      return;
    }
    let formData = new FormData();
    formData.append("file", droppedFiles[0]);
    axios.post(process.env.VUE_APP_BASE_API_URL + '/split', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }).then(console.log)
  }
}
</script>

<style scoped>
.file-drop {
  background: lightblue;
}
</style>
