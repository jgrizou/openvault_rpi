<template>
  <div>

    <div v-if="vault_control">
      <Lock ref="lock" :callback="hide_vault_control"></Lock>
    </div>
    <div v-else>

      <Display ref="display" class="display"></Display>

      <div v-if="check_combination">
        <Check ref="check"></Check>
      </div>
      <div v-else>

        <Digit ref="digit" class="digit"></Digit>

        <div v-if="level == 1">
          <Pad12 ref="pad" class="pad" :callback="discrete_pad_callback"></Pad12>
        </div>
        <div v-else-if="level == 2">
          <Pad12Random ref="pad" class="pad" :callback="discrete_pad_callback"></Pad12Random>
        </div>
        <div v-else-if="level == 3">
          <Pad33 ref="pad" class="pad" :callback="discrete_pad_callback"></Pad33>
        </div>
        <div v-else-if="level == 4">
          <Pad33 ref="pad" class="pad" :callback="discrete_pad_callback"></Pad33>
        </div>
        <div v-else-if="level == 5">
          <PadContinuous ref="pad" class="pad" :callback="continuous_pad_callback"></PadContinuous>
        </div>
        <div v-else>
          <div class="pad">Level {{ level }} not implemented<div>
        </div>

      </div>
    </div>
  </div>
</template>


<script>
import Lock from './../components/Lock.vue'
import Check from './../components/Check.vue'
import Display from './../components/Display.vue'
import Digit from './../components/Digit.vue'
import Pad12 from './../components/Pad_1x2.vue'
import Pad12Random from './../components/Pad_1x2_RandomPadColor.vue'
import Pad33 from './../components/Pad_3x3.vue'
import PadContinuous from './../components/Pad_Continuous.vue'

export default {
  name: 'SPA',
  components: { Lock, Check, Display, Digit, Pad12, Pad12Random, Pad33, PadContinuous},
  data() {
    return {
      vault_control: false,
      check_combination: false
    }
  },
  computed: {
    level: function () {
      var config_file = this.$route.params.pathMatch
      var number_in_config_file = config_file.match(/\d/) // regex
      return parseInt(number_in_config_file, 10) // convert str in int
    }
  },
  sockets: {
    connect: function () {
      this.$socket.emit('is_spawn')
    },
    spawn_state: function (state) {
      if (!state) {
        this.spawn_learner()
      }
    },
    update_code: function (code_info) {
      if (code_info.apply_pause) {
        this.$refs.digit.show_message = true
        this.$refs.pad.paused = true // disable the pad button

        setTimeout( () => {
          this.$refs.display.code = code_info.code_json
          this.$refs.digit.show_message = false
          this.$refs.pad.paused = false // enable the pad button
        }, 800);
      } else {
        this.$refs.display.code = code_info.code_json
      }
    },
    update_flash: function (flash) {
      this.$refs.digit.flash = flash
      this.$refs.pad.awaiting_flash = false // enable the pad button
    },
    update_pad: function (pad_color) {
      this.$refs.pad.pad_color = pad_color
    },
    valid: function () {
      this.$socket.emit('log', 'valid')
      this.show_check_combination()

      setTimeout( () => {
        this.hide_check_combination()
        this.show_vault_control()
      }, 1000);
    },
    invalid: function () {
      this.$socket.emit('log', 'invalid')
      this.show_check_combination()

      setTimeout( () => {
        this.hide_check_combination()
      }, 1000);
    },
    inconsistent: function () {
      this.$socket.emit('log', 'inconsistent')
      this.show_check_combination()

      setTimeout( () => {
        this.hide_check_combination()
      }, 1000);
    },
  },
  methods: {
    spawn_learner: function () {
      // spawn the learner given link given in url
      this.$socket.emit('spawn_learner', this.$route.params.pathMatch)
    },
    discrete_pad_callback: function (click_info) {
      this.$refs.pad.awaiting_flash = true // disable the pad button

      var feedback_info = {}
      feedback_info.symbol = click_info.button
      feedback_info.flash = this.$refs.digit.flash
      this.$socket.emit('feedback_info', feedback_info)
    },
    continuous_pad_callback: function (click_info) {
      // this.$refs.pad.awaiting_flash = true // disable the pad button
      this.$socket.emit('log', click_info)
    },
    show_vault_control: function () {
      this.vault_control = true
    },
    hide_vault_control: function () {
      this.vault_control = false
      this.$socket.emit('reset')
    },
    show_check_combination: function () {
      this.check_combination = true
    },
    hide_check_combination: function () {
      this.check_combination = false
      this.$socket.emit('reset')
    }
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
