<template>
  <div class="container">
    <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
      <h1 class="display-4">Verify Signature</h1>
      <p
        class="lead"
      >Upload two signature image in first two boxes to see the verification result in the last box</p>
    </div>

    <div class="card-deck mb-3 text-center">
      <div class="card mb-4 shadow-sm">
        <div class="card-header">
          <h4 class="my-0 font-weight-normal">Image 1</h4>
        </div>
        <div class="card-body">
          <FileUpload />
        </div>
      </div>
      <div class="card mb-4 shadow-sm">
        <div class="card-header">
          <h4 class="my-0 font-weight-normal">Image 2</h4>
        </div>
        <div class="card-body">
          <FileUpload />

        </div>
      </div>
      <div class="card mb-4 shadow-sm">
        <div class="card-header">
          <h4 class="my-0 font-weight-normal">Result</h4>
        </div>
        <div class="card-body">
         Valid
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import FileUpload from "./FileUpload";
export default {
  components: {
    FileUpload
  },
  name: "Ping",
  data() {
    return {
      msg: ''
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/ping";
      axios
        .get(path)
        .then(res => {
          this.msg = res.data;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getMessage();
  }
};
</script>
