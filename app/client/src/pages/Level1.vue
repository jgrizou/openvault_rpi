<template>
  <div>

    <div v-if="vault_control">
      <lock ref="lock" :callback="hide_vault_control"></lock>
    </div>
    <div v-else>
      <display ref="display" class="display"></display>
      <div v-if="check_combination">
        <check ref="check"></check>
      </div>
      <div v-else>
        <digit ref="digit" class='digit'></digit>
        <pad ref="pad" class='pad' :callback="pad_callback"></pad>
      </div>
    </div>
  </div>
</template>


<script>
import Lock from './../components/Lock.vue'
import Check from './../components/Check.vue'
import Display from './../components/Display.vue'
import Digit from './../components/Digit.vue'
import Pad from './../components/1x2Pad.vue'

export default {
  name: 'Level1',
  components: { Lock, Check, Display, Digit, Pad},
  data() {
    return {
      vault_control: false,
      check_combination: false
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
    update_code: function (code_json) {
      this.$refs.digit.show_message = true
      this.$refs.pad.paused = true // disable the pad button

      setTimeout( () => {
        this.$refs.display.code = code_json
        this.$refs.digit.show_message = false
        this.$refs.pad.paused = false // enable the pad button
      }, 800);
    },
    update_flash: function (flash) {
      this.$refs.digit.flash = flash
      this.$refs.pad.awaiting_flash = false // enable the pad button
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
    pad_callback: function (click_info) {
      this.$refs.pad.awaiting_flash = true // disable the pad button

      var feedback_info = {}
      feedback_info.symbol = click_info.button
      feedback_info.flash = this.$refs.digit.flash
      this.$socket.emit('feedback_info', feedback_info)
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
