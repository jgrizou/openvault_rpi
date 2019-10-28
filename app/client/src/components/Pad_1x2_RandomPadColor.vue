<template>
  <div>
    <div v-for="(color, index) in button_color">

      <button
        :class="{
          'btn btn-elongated': true,
          ['btn-elongated-' + index]: true,
          [color]: true
          }"
        :disabled="disabled"
        v-on:click="on_click(index.toString())">
      </button>

    </div>

  </div>
</template>

<script>

export default {
  name: 'Pad12Random',
  props: {
    callback: {
      type: Function,
      required: true
    }
  },
  data() {
    return {
      paused: false,
      awaiting_flash: false,
      button_color: ['noflash', 'flash'],
      button_color_1: ['noflash', 'flash'],
      button_color_2: ['flash', 'noflash'],
      button_color_history: []
    }
  },
  computed: {
    disabled: function () {
      return this.paused || this.awaiting_flash
    }
  },
  methods: {
    on_click: function (button_name, event) {
      var click_info = {}
      click_info.button = button_name
      this.callback(click_info)
      this.update_button_color()
    },
    toggle_button_color: function () {
      if (this.button_color === this.button_color_2) {
        this.button_color = this.button_color_1
      } else {
        this.button_color = this.button_color_2
      }
    },
    update_button_color: function () {
      // we do random color but limit to a maximum of twice the same color in a row
      var new_button_color
      if ( Math.random() < 0.5 ) {
        new_button_color = this.button_color_1
      } else {
        new_button_color = this.button_color_2
      }
      // check two last values
      var last_two_colors = this.button_color_history.slice(-2)
      if (last_two_colors.length > 1) {
        if (last_two_colors[0] == last_two_colors[1]) {
          // if new color is the same as two previous ones
          if (new_button_color == last_two_colors[1]) {
            // flip it
            new_button_color = [new_button_color[1], new_button_color[0]]
          }
        }
      }
      // assign values
      this.button_color = new_button_color
      this.button_color_history.push(new_button_color)
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
