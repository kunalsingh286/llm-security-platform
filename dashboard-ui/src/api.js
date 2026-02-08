import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const getLogs = () =>
  api.get("/audit/logs");

export default api;
