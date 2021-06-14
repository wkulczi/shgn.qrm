<template>
  <div class="container">
    <v-row class="justify-content-center">
      <v-col cols="6">
        <v-row>
          <line-chart
            :data="tempsGraph"
            xtitle="Timestamp"
            ytitle="Light intensity in voltage"
            title="Light intensity in time (V)"
          />
        </v-row>
      </v-col>
      <v-col offset="1" cols="3">
        <v-row>
          <v-card flat>
            <v-card-title> Temp data</v-card-title>
            <v-data-table
              :headers="headers"
              :items="tempsTable"
              :items-per-page="10"
              class="elevation-1"
              :footer-props="footerProps"
            >
            </v-data-table>
          </v-card>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Temp',
  // async asyncData({ $axios }) {
  asyncData({ $axios }) {
    // const resp = await $axios.$get('/api/tables')
    // const lightData = resp.lights
    const resp = {
      tempsGraph: [{ key1: 'value1' }],
      tempsTable: [
        { date: 2, val: 3 },
        { date: 3, val: 4 },
      ],
    }
    const tempTable = resp.tempsTable
    const tempGraph = resp.tempsGraph
    return { tempGraph, tempTable }
  },
  data() {
    return {
      tempsTable: [],
      tempsGraph: {},
      footerProps: {
        rowsPerPageText: '',
        itemsPerPageOptions: [],
        itemsPerPageText: '',
      },
      headers: [
        {
          text: 'Timestamp',
          sortable: false,
          value: 'date',
        },
        { text: 'Value', value: 'val' },
      ],
    }
  },
}
</script>

<style scoped></style>
