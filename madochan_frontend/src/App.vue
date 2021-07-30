<template>
  <Control :settings="settings" />
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
