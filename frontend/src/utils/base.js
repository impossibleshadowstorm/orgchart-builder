import axios from "axios";

export const HOST = import.meta.env.VITE_BACKEND_URL;

export async function buildHeaders() {
  return { "Content-Type": "application/json" };
}

export async function get(uri, params = {}, options) {
  const headers = await buildHeaders();
  return axios
    .get(`${HOST}${uri}`, { params, headers, ...options })
    .then((res) => res.data);
}

export async function post(uri, body = {}) {
  const headers = await buildHeaders();
  return axios.post(`${HOST}${uri}`, body, { headers }).then((res) => res.data);
}

export async function patch(uri, body = {}) {
  const headers = await buildHeaders();
  return axios
    .patch(`${HOST}${uri}`, body, { headers })
    .then((res) => res.data);
}
