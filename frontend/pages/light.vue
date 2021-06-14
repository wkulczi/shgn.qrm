<template>
  <div class="container">
    <v-row class="justify-content-center">
      <v-col cols="6">
        <v-row>
          <line-chart
            :data="lightsVals"
            xtitle="Timestamp"
            ytitle="Light intensity"
            title="Light intensity in time"
          />
        </v-row>
        <v-row>
          <line-chart
            :data="lightsVoltage"
            xtitle="Timestamp"
            ytitle="Light intensity in voltage"
            title="Light intensity in time (V)"
          />
        </v-row>
      </v-col>
      <v-col offset="1" cols="4">
        <v-row>
          <v-card flat>
            <v-card-title> Light data</v-card-title>
            <v-data-table
              :headers="headers"
              :items="lightData"
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
  name: 'Light',
  async asyncData({ $axios }) {
    const resp = await $axios.$get('/api/light-data')
    const lightData = resp.lights_table_data
    const lightsVals = resp.lights_vals
    const lightsVoltage = resp.lights_voltage
    return { lightData, lightsVals, lightsVoltage }
  },
  data() {
    return {
      lightData: {},
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
        { text: 'Value', value: 'val.val' },
        { text: 'Voltage', value: 'val.voltage' },
      ],
    }
  },
}
</script>

<style scoped></style>
