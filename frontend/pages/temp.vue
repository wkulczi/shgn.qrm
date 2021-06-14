<template>
  <div class="container">
    <v-row class="justify-content-center">
      <v-col cols="6">
        <v-row>
          <line-chart
            :data="tempGraph"
            xtitle="Timestamp"
            ytitle="Light intensity in voltage"
            title="Light intensity in time (V)"
          />
        </v-row>
      </v-col>
      <v-col offset="1" cols="4">
        <v-row>
          <v-card flat>
            <v-card-title> Temp data</v-card-title>
            <v-data-table
              :headers="headers"
              :items="tempTable"
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
  async asyncData({ $axios }) {
    const resp = await $axios.$get('/api/temp-data')
    const tempTable = resp.temps_table
    const tempGraph = resp.temps_graph
    return { tempGraph, tempTable }
  },
  data() {
    return {
      tempGraph: [],
      tempTable: {},
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
        { text: 'Value', value: 'value' },
      ],
    }
  },
}
</script>

<style scoped></style>
