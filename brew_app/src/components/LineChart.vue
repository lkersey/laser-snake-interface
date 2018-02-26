<script>
import { Line, mixins } from 'vue-chartjs'

export default {
  extends: Line,
  mixins: [mixins.reactiveProp],
  // props: {
  //   chartData: {
  //     type: Array | Object,
  //     required: false
  //   },
  //   chartLabels: {
  //     type: Array,
  //     required: false
  //   }
  // },

  data () {
    return {
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            },
            gridLines: {
              display: true
            }
          }],
          xAxes: [ {
            gridLines: {
              display: false
            }
          }]
        },
        legend: {
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },

  mounted () {
    this.renderChart(
    // {
    //   labels: this.chartLabels,
    //   datasets: [
    //     {
    //       label: 'temps',
    //       borderColor: '#249EBF',
    //       pointBackgroundColor: 'white',
    //       borderWidth: 1,
    //       pointBorderColor: '249EBF',
    //       backgroundColor: 'transparent',
    //       data: this.chartData
    //     }
    //   ]
    // }, this.options)
      this.chartData, this.options
    )
  }
}
</script>
