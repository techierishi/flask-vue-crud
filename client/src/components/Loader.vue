<template>
<div class="progress-bar">
  <span class="bar">
    <span class="progress"></span>
  </span>
</div>
</template>
<script>

export default {

};
</script>
<style>
body {
  background: #eef1f3;
}

@-webkit-keyframes loader {
  0% {
    width: 0;
  }
  20% {
    width: 10%;
  }
  25% {
    width: 24%;
  }
  43% {
    width: 41%;
  }
  56% {
    width: 50%;
  }
  66% {
    width: 52%;
  }
  71% {
    width: 60%;
  }
  75% {
    width: 76%;
  }
  94% {
    width: 86%;
  }
  100% {
    width: 100%;
  }
}

@keyframes loader {
  0% {
    width: 0;
  }
  20% {
    width: 10%;
  }
  25% {
    width: 24%;
  }
  43% {
    width: 41%;
  }
  56% {
    width: 50%;
  }
  66% {
    width: 52%;
  }
  71% {
    width: 60%;
  }
  75% {
    width: 76%;
  }
  94% {
    width: 86%;
  }
  100% {
    width: 100%;
  }
}
.progress-bar {
  border-radius: 5px 5px 0 0;
  overflow: hidden;
  width: 100%;
}
.progress-bar span {
  display: block;
}

.bar {
  background: rgba(0, 0, 0, 0.075);
}

.progress {
  -webkit-animation: loader 8s ease infinite;
          animation: loader 8s ease infinite;
  background: #75b800;
  color: #fff;
  padding: 5px;
  width: 0;
}

.progress-bar {
  left: 50%;
  max-width: 87%;
  height: 4px;
  position: absolute;
  -webkit-transform: translate3d(-50%, -50%, 0);
          transform: translate3d(-50%, -50%, 0);
}

</style>
