<template>
  <div class="container">
    <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
      <h1 class="display-4">Verify Signature</h1>
      <p class="lead">
        Upload training &amp; test signatures in first two boxes
        to see the verification result in the last box
      </p>
    </div>
    <div class="form-group hide-foldername-input">
      <label for="exampleInputEmail1">Folder name</label>
      <input
        type="email"
        class="form-control"
        v-model="folderName"
        @input="onFolderNameChange"
        placeholder="Folder Name"
      />
    </div>

    <div class="card-deck mb-3 text-center">
      <div class="card mb-4 shadow-sm">
        <div class="card-header">
          <h4 class="my-0 font-weight-normal">Training Signature</h4>
        </div>
        <div class="card-body">
          <FileUpload v-bind:post-meta-data="trainingProps" />
        </div>
      </div>
      <div class="card mb-4 shadow-sm">
        <div class="card-header">
          <h4 class="my-0 font-weight-normal">Test Signatures</h4>
        </div>
        <div class="card-body">
          <FileUpload v-bind:post-meta-data="testProps" />
        </div>
      </div>
      <div class="card mb-4 shadow-sm">
        <div class="card-header">
          <h4 class="my-0 font-weight-normal">Result</h4>
        </div>
        <div class="card-body">
          <button
            type="button"
            class="btn btn-lg btn-block btn-primary remove-img-bttn"
            @click="trainTest"
          >Train &amp; Test</button>
          <div class="spinner-border" role="status" v-if="loading">
            <span class="sr-only">Loading...</span>
          </div>
          <div
            class="alert"
            v-bind:class="{ 'alert-success': testStatus, 'text-danger': !testStatus }"
            role="alert"
          >{{testResponse}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import FileUpload from './FileUpload.vue';

export default {
  components: {
    FileUpload,
  },
  name: 'Ping',
  data() {
    return {
      loading: false,
      testStatus: false,
      testResponse: '',
      folderName: '',
      trainingProps: '{"folder_name":"1234","upload_type":"training"}',
      testProps: '{"folder_name":"1234","upload_type":"test"}',
    };
  },
  methods: {
    trainTest() {
      const path = 'http://localhost:5000/traintest';
      this.loading = true;
      axios
        .get(path)
        .then((res) => {
          this.loading = false;
          // eslint-disable-next-line
          console.log('trainTest:res', res);
          let resultText = '';
          if (res.data && res.data.result > 0.5) {
            this.testStatus = true;
            resultText = 'POSITIVE';
          } else {
            this.testStatus = false;
            resultText = 'NEGATIVE';
          }
          this.testResponse = `${resultText}(${res.data.result})`;
        })
        .catch((error) => {
          this.loading = false;

          // eslint-disable-next-line
          console.error("trainTest:error", error);
        });
    },
    onFolderNameChange() {
      this.trainingProps = `{"folder_name":"${this.folderName}","upload_type":"training"}`;
      this.testProps = `{"folder_name":"${this.folderName}","upload_type":"test"}`;
    },
  },
  created() {},
};
</script>
<style scoped>
.hide-foldername-input {
  display: none;
}
</style>
