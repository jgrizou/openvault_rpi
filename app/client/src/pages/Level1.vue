<template>
  <div>
    <display ref="display" class="display"></display>
    <digit ref="digit" class='digit'></digit>
    <pad ref="pad" class='pad' :callback="pad_callback"></pad>
  </div>
</template>


<script>
import Display from './../components/Display.vue'
import Digit from './../components/Digit.vue'
import Pad from './../components/1x2Pad.vue'

export default {
  name: 'Level1',
  components: { Display, Digit, Pad},
  sockets: {
    connect: function () {
      this.$socket.emit('is_spawn')
    },
    spawn_state: function (state) {
      if (!state) {
        this.spawn_learner()
      }
    }
  },
  methods: {
    spawn_learner: function () {
      // spawn the learner given link given in url
      this.$socket.emit('spawn_learner', this.$route.params.pathMatch)
    },
    pad_callback: function (click_info) {
      var feedback_info = {}
      feedback_info.symbol = click_info.button
      feedback_info.flash = this.$refs.digit.flash
      this.$socket.emit('feedback_info', feedback_info)
    },
  },
  mounted() {
    this.spawn_learner()
  }
}
</script>


<style>
/* global styles */
</style>

<style scoped>
/* local styles */
</style>
