<template>
  <div class="container">
    <v-row class="justify-content-center">
      <v-col cols="4">
        <v-row>
          <v-card flat>
            <v-card-title>Header tabeli</v-card-title>
            <v-data-table
              :headers="headers"
              :items="tempData"
              :items-per-page="10"
              class="elevation-1"
              :footer-props="footerProps"
            ></v-data-table>
          </v-card>
        </v-row>
      </v-col>
      <v-col offset="1" cols="4">
        <v-row>
          <v-card flat>
            <v-card-title> Header tabeli</v-card-title>

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
    const resp = await $axios.$get('/api/tables')
    const tempData = resp.temps
    const lightData = resp.lights
    return { tempData, lightData }
  },
  data() {
    return {
      tableDatas: {
        tempData: {},
        lightData: {},
      },
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
