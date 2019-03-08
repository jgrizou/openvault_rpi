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

:root {
  --screen_width: 480px;
  --screen_height: 800px;
  --display_height: 150px;
  --digit_height: calc( var(--screen_width) / 5 * 2); /* 5 digits per row on 2 column */
  --pad_height: calc( var(--screen_height) - var(--display_height) - var(--digit_height));

  --on_color: rgba(0, 200, 255, 1);
  --on_color_active: rgba(0, 150, 205);
  --off_color: rgba(255, 200, 0, 1);
  --off_color_active: rgba(205, 150, 0, 1);
}

.display {
  position: absolute;
  top: 0px;
  width: var(--screen_width);
  height: var(--display_height);
  background-color: rgba(0, 255, 0, 1);
}

.digit {
  position: absolute;
  top: var(--display_height);
  width: var(--screen_width);
  height: var(--digit_height);
  background-color: rgba(255, 255, 255, 1);
}

.pad {
  position: absolute;
  top: calc( var(--display_height) + var(--digit_height) );
  width: var(--screen_width);
  height: var(--pad_height);
  background-color: rgba(255, 255, 255, 1);
}

</style>

<style scoped>
/* local styles */
</style>
