<template>
  <div class="container">
    <v-row>
      <v-row style="min-height: 200px"> </v-row>
      <v-row style="min-height: 400px">
        <p class="project-description">
          This webservice was created as a project for Poznan University of
          Technology. <br />
          The webservice connects two photoresistors, one thermistor and a
          raspberry pi camera to create a simple monitor system for my
          aquarium.<br />
          Below you can see the photo of my aquarium, connection schematics and
          a picture of assembled hardware solution.
        </p>
      </v-row>
      <v-row><nuxt-img src="aquarium.jpg" alt="aquarium photo" /></v-row>
      <v-row><nuxt-img src="hardware.jpg" alt="hardware connections" /></v-row>
      <v-row><nuxt-img src="schema.png" alt="hardware schema" /></v-row>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'About',
}
</script>

<style scoped>
.project-description {
  font-size: 1.1rem;
  letter-spacing: 0.2px;
  line-height: 2rem;
}
</style>
