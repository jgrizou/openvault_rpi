<template>
  <div>
    <display class="display"></display>
    <digit class='digit'></digit>
    <pad class='pad'></pad>
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
      this.$socket.emit('log', '## Socket connected')
    },
    disconnect: function () {
      this.$socket.emit('log', '## Socket disconnected')
    }
  }
}
</script>


<style>
/* global styles */
</style>

<style scoped>
/* local styles */
</style>
