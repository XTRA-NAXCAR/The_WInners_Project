

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootstrap';
import axios from 'axios';
import { createApp } from 'vue';

import App from './App.vue'

var rootUrl = window.location.origin;


axios.get(rootUrl + '/data/api/')
    .then(response => {
        const data = response.data;
        const app = createApp(App);
        app.provide('$rootUrl', rootUrl)
        app.provide('$data', data);
        app.mount('#app');
    })
    .catch(error => {
        console.error(error);
      });