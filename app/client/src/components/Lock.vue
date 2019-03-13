<template>
  <div>

    <!-- <canvas id="confetti"></canvas> -->

    <div v-if="locked" class="lock closed" v-on:click="on_click">
      <img src="./../assets/lock-solid.svg">
    </div>
    <div v-else class="lock opened" v-on:click="on_click">
      <img src="./../assets/unlock-solid.svg">
    </div>

    <div v-if="counter" class="counter">
      {{ counter }}
    </div>

    <button class="home" v-on:click="reset">HOME</button>

  </div>
</template>

<script>
// import "confetti-js"

export default {
  name: "Lock",
  // mounted () {
  //   var confettiSettings = {
  //     target: 'confetti',
  //     clock: 50,
  //     size: 2,
  //     width: 480,
  //     height: 800,
  //     max: 200,
  //   }
  //   var confetti = new ConfettiGenerator(confettiSettings)
  //   confetti.render()
  // },
  props: {
    callback: {
      type: Function,
      required: true
    }
  },
  data() {
    return {
      locked: true,
      endTime: undefined,
      remainingTime: undefined,
      interval: undefined
    };
  },
  computed: {
    counter: function () {
      return Math.max(0, Math.round(this.remainingTime / 1000))
    }
  },
  methods: {
    on_click: function (event) {
      this.$socket.emit('open_lock')
      this.locked = false

      var nowTime = new Date().getTime()
      this.remainingTime = 5000
      this.endTime = new Date(nowTime + this.remainingTime)

      // update remainingTime every second
      this.interval = setInterval(() => {
        this.timerCount()
      }, 1000)

    },
    timerCount: function() {
      var nowTime = new Date().getTime()
      this.remainingTime = this.endTime - nowTime
      if (this.remainingTime <= 0) {
        this.$socket.emit('close_lock')
        this.locked = true
        clearInterval(this.interval)
      }
    },
    reset: function () {
      this.$socket.emit('log', 'in lock callback')
      this.callback()
    }
  }
}

</script>

<style>
/* global styles */

.counter {
  position: absolute;
  top: 550px;
  width: var(--screen_width);
  height: var(--tile_height);
  border-radius: 5px; /* rounding */
  text-align: center;
  vertical-align: middle;
  font-size: 90px;
  font-weight: 700;
  font-family: "Helvetica";
  line-height: var(--tile_height);
  background-color: var(--tile_color);
}

.home {
  position: absolute;
  top: 750px;
  left: 200px;
  width: 80px;
  height: 35px;
  outline: none; /* remove contour when clicked */
  border: none;
  border-radius: 5px; /* rounding */
  text-align: center;
  vertical-align: middle;
  font-size: 20px;
  font-weight: 700;
  font-family: "Helvetica";
  background-color: rgba(230, 230, 230, 1);
}

:root {
  --lock_diameter: 150px;
  --lock_margin: 100px;
}

.lock {
  position: absolute;
  top: 200px;
  left: calc( var(--screen_width)/2 - var(--lock_margin)/2 - var(--lock_diameter)/2 );
  width: calc( var(--lock_diameter) + var(--lock_margin) );
  height: calc( var(--lock_diameter) + var(--lock_margin) );
  border-radius: calc( ( var(--lock_diameter) + var(--lock_margin) ) / 2 );
  outline: none; /* remove contour when clicked */
  border: none;
}

.lock img {
  position: absolute;
  top: calc( var(--lock_margin) / 2 );
  left: calc( var(--lock_margin) / 2 );
  width: var(--lock_diameter);
  height: var(--lock_diameter);
}

.closed {
  background-color: rgba(255, 100, 100, 1);
  box-shadow: 0 30px rgba(130, 130, 130, 1);
}

.opened {
  background-color: rgba(100, 255, 100, 1);
  box-shadow: 0 5px rgba(100, 100, 100, 1);
  transform: translateY(25px);
}

</style>

<style scoped>
/* local styles */
</style>
