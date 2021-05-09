<template>
  <div class="container row">
    <v-spacer />
    <v-row>
      <v-col cols="9">
        <line-chart
          :data="{ '2017-01-01': 11, '2017-01-02': 6 }"
          xtitle="Time"
          ytitle="Light value"
          title="Tekst"
        />
        <!--todo just a line chart-->
      </v-col>
      <v-col cols="3">
        <pie-chart
          :data="[
            ['Blueberry', 44],
            ['Strawberry', 23],
          ]"
          suffix="%"
          title="Tekst"
        />
        <!--todo stosunek światła pow minimum a poniżej (last 24h)-->
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <line-chart
          :data="{ '2017-01-01': 11, '2017-01-02': 6 }"
          :precision="3"
        />
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
}
</script>

<style scoped></style>
