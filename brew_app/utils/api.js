import axios from 'axios'
import VueAxios from 'vue-axios'
import Vue from 'vue'

Vue.use(VueAxios, axios)

const BASE_URL = 'http://localhost:5000'

export {getTemperatureData, }

function getTemperatureData() {
  return axios.get(BASE_URL + '/temperatures')
}
