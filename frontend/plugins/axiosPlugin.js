import axios from 'axios';

export default {
 install(app) {
    const apiClient = axios.create({
        baseURL: process.env.VUE_APP_API_BASE_URL,
    });

    app.config.globalProperties.$axios = apiClient;
 },
};