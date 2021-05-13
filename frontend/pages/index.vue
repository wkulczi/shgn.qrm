<template>
  <v-row class="container">
    <div class="align-left">
      <v-row class="justify-content-center" no-gutters>
        <v-col cols="2"><Logo /></v-col>
      </v-row>
      <h1 class="quicksand-font title">
        The current <br />
        tank temperature is:
      </h1>
      <div class="quicksand-font temp-div">{{ temp }} °C</div>
      <div class="disclaimer">
        This page updates automatically every 30 seconds.
      </div>
    </div>
  </v-row>
</template>

<script>
import Logo from '../components/Logo'
export default {
  components: { Logo },
  data: () => {
    return {
      temp: '27.94',
      timerPassed: false,
      documentHasFocus: true,
      fetchDataInterval: null,
      watchWindowFocusInterval: null,
    }
  },
  async fetch() {
    const resp = await this.$axios.$get('/api/temp')
    this.temp = resp.temp
  },
  beforeDestroy() {
    clearInterval(this.fetchDataInterval)
    clearInterval(this.watchWindowFocusInterval)
  },
  mounted() {
    this.fetchDataInterval = setInterval(function () {
      this.timerPassed = !(this.timerPassed && this.documentHasFocus)
    }.bind(this), 30000)
    this.watchWindowFocusInterval = setInterval(function () {
      this.documentHasFocus = document.hasFocus()
      if (this.timerPassed && this.documentHasFocus) {
        this.timerPassed = false
        this.$fetch()
      }
      if (this.documentHasFocus) {
        document.title = 'shgn'
      } else {
        document.title = 'shgn.sleep'
      }
    }.bind(this), 500)
  },
}
</script>

<style>
.page-enter-active,
.page-leave-active {
  transition: opacity 0.23s;
}
.page-enter,
.page-leave-active {
  opacity: 0;
}

.align-left {
  text-align: left;
}

.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.quicksand-font {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

/* todo add some kind of animation so you could know that it refreshed */
.temp-div {
  padding: 1rem 0 0 2rem;
  display: block;
  font-size: 6rem;
  font-weight: 200;
}

.title {
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.disclaimer {
  padding-top: 2rem;
  color: #868383;
}
</style>
