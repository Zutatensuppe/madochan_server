<template>
  <div class="container" v-if="settings.model && settings.weirdness">
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
      <span class="button" type="button" @click="onSubmit">Generate Word!</span>

      <div v-if="word">{{ word }}</div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import config from "../config";
export default defineComponent({
  name: "HelloWorld",
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
    };
  },
  mounted() {
    this.model = this.settings.model[0] || "";
    this.weirdness = this.settings.weirdness[0] || 1;
  },
  methods: {
    async onSubmit() {
      const res = await fetch(`${config.api_url}/_create_word`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify({
          model: this.model,
          weirdness: this.weirdness,
          definition: this.definition,
        }),
      });
      const data = await res.json();
      this.word = data.word;
    },
  },
});
</script>

<style scoped>
</style>
