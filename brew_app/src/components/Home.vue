<template>
  <div id="home">
    <ul>
      <li v-for="count in temps.length" :key="count"> The temp was: {{ temps[count] }} at {{times[count]}} </li>
    </ul>
  </div>
</template>

<script>
import { getTemperatureData } from '../../utils/api'
import moment from 'moment'
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
        this.times = this.converTimestamp(ret.data.timestamps)
      })
        .catch(e => {
          console.log('error caught')
          console.log(e)
        })
    },

    converTimestamp (timestamp) {
      var i = 0
      for (i; i < timestamp.length; i++) {
        // time is recieved in sec since epoch. Moment accepts ms
        // since epoch
        timestamp[i] = moment(timestamp[i] * 1000)
          .format('dddd DD MMMM YYYY, H:mm:ss a')
      }
      return timestamp
    }
  },

  created () {
    // console.log('created')
    this.getData()
    this.timer = setInterval(this.getData, 60000)
  }

}
</script>
