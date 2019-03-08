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
import Pad from './../components/ContinuousPad.vue'

export default {
  name: 'Level5',
  components: { Display, Digit, Pad },
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

.display {
  position: fixed;
  left: 0px;
  top: 0px;
  width: 480px;
  height: 150px;
  background-color: rgba(0, 255, 0, 1);
}

.digit {
  position: fixed;
  left: 0px;
  top: 150px;
  width: 480px;
  height: 200px;
  background-color: rgba(0, 0, 255, 1);
}

.pad {
  position: fixed;
  left: 0px;
  top: 350px;
  width: 480px;
  height: 450px;
  background-color: rgba(255, 0, 0, 1);
}


</style>

<style scoped>
/* local styles */
</style>
