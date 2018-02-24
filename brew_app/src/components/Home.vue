<template>
  <div id="home">
    <ul>
      <li v-for="count in temps.length" :key="count"> The temp was: {{ temps[count] }} at {{times[count]}} </li>
    </ul>
  </div>
</template>

<script>
import { getTemperatureData } from '../../utils/api'
export default {
  name: 'Home',

  data () {
    return {
      probe: '',
      temps: [],
      times: []
    }
  },

  methods: {
    getData () {
      getTemperatureData().then(ret => {
        console.log(ret.data)
        this.probe = ret.data.probe_id
        this.temps = ret.data.temperatures
        this.times = ret.data.timestamps
      })
        .catch(e => {
          console.log('error caught')
          console.log(e)
        })
    }
  },

  created () {
    // console.log('created')
    this.getData()
    this.timer = setInterval(this.getData, 60000)
  }

}
</script>
