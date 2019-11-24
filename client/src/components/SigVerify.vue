<template>
  <div class="container">
    <div class="container">
      <div class="row">
        <div class="col-sm">
          <div class="file-upload">
            <button class="file-upload-btn" type="button">Add Image</button>

            <div class="image-upload-wrap">
              <input
                class="file-upload-input"
                type="file"
                v-on:input="readURL($event);"
                accept="image/*"
              />
              <div class="drag-text">
                <h3>Drag and drop a file or select add Image</h3>
              </div>
            </div>
            <div class="file-upload-content">
              <img class="file-upload-image" src="#" alt="your image" />
              <div class="image-title-wrap">
                <button type="button" onclick="removeUpload()" class="remove-image">
                  Remove
                  <span class="image-title">Uploaded Image</span>
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm">
          <div class="file-upload">
            <button class="file-upload-btn" type="button">Add Image</button>

            <div class="image-upload-wrap">
              <input
                class="file-upload-input"
                type="file"
                v-on:input="readURL(this);"
                accept="image/*"
              />
              <div class="drag-text">
                <h3>Drag and drop a file or select add Image</h3>
              </div>
            </div>
            <div class="file-upload-content">
              <img class="file-upload-image" src="#" alt="your image" />
              <div class="image-title-wrap">
                <button type="button" onclick="removeUpload()" class="remove-image">
                  Remove
                  <span class="image-title">Uploaded Image</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Ping",
  data() {
    return {
      msg: ""
    };
  },
  mounted : function(){
    let dropArea = document.querySelector('.image-upload-wrap')
    dropArea.addEventListener('dragleave', () => {
        document.querySelector('.image-upload-wrap').classList.remove('image-dropping');
    }, false)
    dropArea.addEventListener('dragover',  () => {
        document.querySelector('.image-upload-wrap').classList.add('image-dropping');
    }, false)
  },
  methods: {
    readURL(event) {
      console.log('event',event);
      if (event.target.files && event.target.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
          document.querySelector(".image-upload-wrap").style.display = 'none';

          document.querySelector(".file-upload-image").setAttribute("src", e.target.result);
          document.querySelector(".file-upload-content").style.display='block';

          document.querySelector(".image-title").innerHTML = event.target.files[0].name;
        };

        reader.readAsDataURL(event.target.files[0]);
      } else {
        removeUpload();
      }
    },
    removeUpload() {
      document.querySelector(".file-upload-input").replaceWith(document.querySelector(".file-upload-input").clone());
      document.querySelector(".file-upload-content").hide();
      document.querySelector(".image-upload-wrap").show();
    },
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
<style scoped>
body {
  font-family: sans-serif;
  background-color: #eeeeee;
}

.file-upload {
  background-color: #ffffff;
  width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.file-upload-btn {
  width: 100%;
  margin: 0;
  color: #fff;
  background: #1fb264;
  border: none;
  padding: 10px;
  border-radius: 4px;
  border-bottom: 4px solid #15824b;
  transition: all 0.2s ease;
  outline: none;
  text-transform: uppercase;
  font-weight: 700;
}

.file-upload-btn:hover {
  background: #1aa059;
  color: #ffffff;
  transition: all 0.2s ease;
  cursor: pointer;
}

.file-upload-btn:active {
  border: 0;
  transition: all 0.2s ease;
}

.file-upload-content {
  display: none;
  text-align: center;
}

.file-upload-input {
  position: absolute;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  outline: none;
  opacity: 0;
  cursor: pointer;
}

.image-upload-wrap {
  margin-top: 20px;
  border: 4px dashed #1fb264;
  position: relative;
}

.image-dropping,
.image-upload-wrap:hover {
  background-color: #1fb264;
  border: 4px dashed #ffffff;
}

.image-title-wrap {
  padding: 0 15px 15px 15px;
  color: #222;
}

.drag-text {
  text-align: center;
}

.drag-text h3 {
  font-weight: 100;
  text-transform: uppercase;
  color: #15824b;
  padding: 60px 0;
}

.file-upload-image {
  max-height: 200px;
  max-width: 200px;
  margin: auto;
  padding: 20px;
}

.remove-image {
  width: 200px;
  margin: 0;
  color: #fff;
  background: #cd4535;
  border: none;
  padding: 10px;
  border-radius: 4px;
  border-bottom: 4px solid #b02818;
  transition: all 0.2s ease;
  outline: none;
  text-transform: uppercase;
  font-weight: 700;
}

.remove-image:hover {
  background: #c13b2a;
  color: #ffffff;
  transition: all 0.2s ease;
  cursor: pointer;
}

.remove-image:active {
  border: 0;
  transition: all 0.2s ease;
}
</style>

