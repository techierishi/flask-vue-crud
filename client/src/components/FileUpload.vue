<template>
  <div class="file-upload-div">
    <div class="container" v-if="!image">
      <div class="input-group mb-3 custom-file-wrapper">
        <div class="custom-file">
          <input
            type="file"
            class="custom-file-input"
            id="inputGroupFile01"
            @change="onFileChange"
            aria-describedby="inputGroupFileAddon01"
          />
          <label class="custom-file-label" for="inputGroupFile01">Choose file</label>
        </div>
      </div>
    </div>
    <div class="container" v-else>
      <div class="row">
        <div v-if="isLoading">
          <Loader />
        </div>
      </div>
      <div class="row">
        <img :src="image" class="img-thumbnail" />
      </div>
      <button
        type="button"
        class="btn btn-lg btn-block btn-danger remove-img-bttn"
        @click="removeImage"
      >Remove</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Loader from "./Loader";
export default {
  name: "FileUpload",
  props: ["postMetaData"],
  components: {
    Loader
  },
  data() {
    return {
      image: "",
      isLoading: false
    };
  },
  methods: {
    openFileSelector() {
      document.querySelector(".file-input").click();
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.createImage(files[0]);
    },
    createImage(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;
      reader.onload = e => {
        vm.image = e.target.result;
      };
      reader.readAsDataURL(file);
      this.uploadFile(file);
    },
    removeImage: function(e) {
      this.image = "";
    },
    uploadFile: function(file) {
      const path = `http://localhost:5000/file-upload`;
      var data = new FormData();
      data.append("file", file);
      data.append("postMeta", this.postMetaData);
      this.isLoading = true;
      var config = {
        onUploadProgress: function(progressEvent) {
          var percentCompleted = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
        }
      };
      axios
        .post(path, data, config)
        .then(res => {
          this.isLoading = false;

          console.log("uploadFile:success", res.data);
        })
        .catch(err => {
          this.isLoading = false;

          console.log("uploadFile:err", err);
        });
    }
  },
  mounted() {}
};
</script>
<style scoped>
body {
  font-family: sans-serif;
  background-color: #eeeeee;
}
.remove-img-bttn {
  margin: 1em 0;
}
.custom-file-wrapper {
  margin-top: 3px;
}
</style>