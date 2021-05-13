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
        <video-player ref="videoPlayer"
                  class="vjs-custom-skin"
                  :options="playerOptions"
                  @play="onPlayerPlay($event)"
                  @ready="onPlayerReady($event)">
        </video-player>
        <!-- todo DASH stream-->
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Graphs',
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
  data() {
    return {
      pieChartData: [],
      lightChartData: {},
      tempChartData: {},
      playerOptions: {
        autoplay: true,
        controls: true,
        controlBar: {
          timeDivider: false,
          durationDisplay: false
        }
        // poster: 'https://surmon-china.github.io/vue-quill-editor/static/images/surmon-5.jpg'
      }
    }
  },
  computed: {
    player () {
      return this.$refs.videoPlayer.player
    }
  },
  methods: {
    onPlayerPlay (player) {
      console.log('player play!', player)
    },
    onPlayerReady (player) {
      console.log('player ready!', player)
      this.player.play()
    },
    playVideo: function (source) {
      const video = {
        withCredentials: false,
        type: 'application/x-mpegurl',
        src: source
      }
      this.player.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,
      this.player.src(video)
      // this.player.load()
      this.player.play()
    }
  },
  mounted () {
    const src = 'https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8'
    this.playVideo(src)
  }
}
</script>

<style scoped>
.player {
    position: absolute !important;
    width: 100%;
}
</style>
