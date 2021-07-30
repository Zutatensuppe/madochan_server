
import config from "./config";

async function getSettings() {
  const res = await fetch(`${config.api_url}/settings`, {
    method: "GET",
  });
  return await res.json();
}

async function createWord(params: Record<string, any>) {
  const res = await fetch(`${config.api_url}/_create_word`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8",
    },
    body: JSON.stringify(params),
  });
  return res.json()
}

export default {
  getSettings,
  createWord,
}
