<script setup>
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend, 
    registerables,
    scales,
    TimeScale,
    plugins
  } from 'chart.js'
  import { Line } from 'vue-chartjs'
  import 'chartjs-adapter-moment'
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    scales,
    TimeScale,
    ...registerables
  )

  import { ref, useTemplateRef, onMounted } from 'vue';
  let chart = useTemplateRef('my-chart');
  

  const data = {
    // labels: [],
    datasets: [
        {
            label: 'Data One',
            // backgroundColor: '#f87979',
            // borderColor: '#f87979',
            data: [{x: new Date('2024-02-21 10:02:00'), y: 20}, {x: new Date('2024-02-21 10:02:00'), y: 10}]
        },
        {
            label: 'Data Two',
            // backgroundColor: '#f87975',
            // borderColor: '#f87975',
            data: [{x: new Date('2024-02-21 10:02:00'), y: 20}, {x: new Date('2024-02-21 10:02:00'), y: 10}]
        }
    ]

  // labels: [1,2,3,4,5,6,7],
  // datasets: [
  //   {
  //     label: 'Data One',
  //     backgroundColor: '#f87979',
  //     borderColor: '#f87979',
  //     data: [40, 39, 10, 40, 39, 80, 40, 49]
  //   },
  //   {
  //     label: 'Data Two',
  //     backgroundColor: '#c87979',
  //     data: [40, 39, 10, 40, 39, 80, 40]
  //   }
  // ]
}

const options = {
  responsive: true,
  maintainAspectRatio: false,
  scales:{
    x: {
      type: 'time',
      time: {
        unit: 'minute', // Разбивка по минутам
        displayFormats: {
          minute: 'DD MMM HH:mm' // Отображение в формате "часы:минуты"
        }
      }
    },
    y: {
      title:{
        text: "Температура, C°",
        display: true
      }
    }
  },
  plugins:{
    legend:{
      // position: ''
    }
  }
  // type: 'line',
    // responsive: true,
}

  onMounted(() => {
    console.log(chart.value.chart);
  });
</script>

<template>
    <Line :options="options" :data="data" ref="my-chart"></Line>
</template>

<style scoped>
header{
    background-color: aqua;
}
</style>