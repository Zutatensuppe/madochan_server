<template>
  <div class="card p-4" v-if="settings.model && settings.weirdness">
    <h1 class="title">madochan</h1>
    <form class="form">
      <div class="field">
        <label class="label">Model</label>
        <div class="control">
          <div class="select">
            <select v-model="model">
              <option value="">Select a Model</option>
              <option v-for="m in settings.model" :value="m">
                {{ m }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="field">
        <label class="label">Weirdness</label>
        <div class="control">
          <div class="select">
            <select v-model="weirdness">
              <option value="">Select a Weirdness</option>
              <option v-for="w in settings.weirdness" :value="w">
                {{ w }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="field">
        <label class="label">Definition</label>
        <div class="control">
          <textarea
            class="textarea"
            v-model="definition"
            placeholder="Put your definition here"
          ></textarea>
        </div>
      </div>
      <span
        class="button"
        :class="{ 'is-loading': loading }"
        type="button"
        :disabled="!definition ? true : null"
        @click="onSubmit"
        >Generate Word!</span
      >

      <div class="title" v-if="word">{{ word }}</div>
      <div class="has-text-danger" v-if="error">{{ error }}</div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import api from "../api";

export default defineComponent({
  props: {
    settings: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      model: "",
      weirdness: 1,
      definition: "",
      word: "",
      error: "",
      loading: false,
    };
  },
  watch: {
    settings: {
      handler() {
        this.model = this.settings.model[0] || "";
        this.weirdness = this.settings.weirdness[0] || 1;
      },
      deep: true,
    },
  },
  mounted() {
    this.model = this.settings.model[0] || "";
    this.weirdness = this.settings.weirdness[0] || 1;
  },
  methods: {
    async onSubmit() {
      if (this.loading) {
        return;
      }
      this.loading = true;
      this.error = "";
      try {
        const data = await api.createWord({
          model: this.model,
          weirdness: this.weirdness,
          definition: this.definition,
        });
        this.word = data.word;
      } catch (e) {
        this.word = "";
        this.error = "No word could be created due to a server error: " + e;
      }
      this.loading = false;
    },
  },
});
</script>

<style scoped>
</style>
