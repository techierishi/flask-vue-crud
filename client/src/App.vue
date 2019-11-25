<template>
  <div id="app">
    <Header />
    <div class="container">
      <router-view />

      <Footer />
    </div>
  </div>
</template>
<script>
import Footer from "./components/Footer";
import Header from "./components/Header";
export default {
  components: {
    Footer,
    Header
  }
};
</script>
<style>
#app {
}
</style>
