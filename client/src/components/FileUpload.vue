<template>
  <div class="file-upload-div">
    <multiple-file-uploader postURL="http://localhost:5000/file-upload-multi" v-bind:postMeta=postMetaData successMessagePath=" Files uploaded successfully " errorMessagePath=""></multiple-file-uploader>
  </div>
</template>

<script>
import MultipleFileUploader from '@updivision/vue2-multi-uploader';

export default {
  name: 'FileUpload',
  props: ['postMetaData'],
  components: {
    MultipleFileUploader,
  },
  data() {
    return {
      image: '',
    };
  },
  methods: {},
  mounted() {},
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
