<template>
  <div class="container">
    <Control :settings="settings" />
    <div class="footer">
      Powered by
      <a href="https://github.com/HylisWilk/madochan" target="_blank"
        >madochan</a
      >
      made by
      <a href="https://twitch.tv/bacing" target="_blank">bacing</a>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Control from "./components/Control.vue";
import api from "./api";

export default defineComponent({
  name: "App",
  components: {
    Control,
  },
  data() {
    return {
      settings: {
        model: [],
        weirdness: [],
      },
    };
  },
  async created() {
    this.settings = await api.getSettings();
  },
});
</script>

<style>
@import "bulma/css/bulma.css";
</style>
