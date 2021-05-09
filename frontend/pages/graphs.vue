<template>
  <div class="container row">
    <v-spacer />
    <v-row>
      <v-col cols="9">
        <line-chart
          :data="lightChartData"
          xtitle="Timestamp"
          ytitle="Light intensity"
          title="Light intensity in time"
        />
        <!--todo just a line chart-->
      </v-col>
      <v-col cols="3">
        <pie-chart :data="pieChartData" suffix="%" title="Light ratio" />
        <!--todo stosunek światła pow minimum a poniżej (last 24h)-->
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <line-chart :data="tempChartData" :precision="3" />
        <!--        Temp graph-->
        <!-- todo line chart of temperatures, should be pretty steady -->
      </v-col>
      <v-col cols="4">
        Stream
        <!-- todo DASH stream-->
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Graphs',
  data() {
    return {
      pieChartData: [],
      lightChartData: {},
      tempChartData: {},
    }
  },
  async asyncData({ $axios }) {
    const resp = await $axios.$get('/api/graph-data')
    const pieChartData = [
      ['Above threshhold', resp.light_rate.above],
      ['Below threshhold', resp.light_rate.below],
    ]
    const lightChartData = resp.lights
    const tempChartData = resp.temps
    return { pieChartData, lightChartData, tempChartData }
  },
}
</script>

<style scoped></style>
