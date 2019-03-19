<template>
  <button
    ref="padcontinuous"
    class="padcontinuous"
    v-on:click="on_click"
  >
  </button>
</template>

<script>

export default {
  name: 'PadContinuous',
  props: {
    callback: {
      type: Function,
      required: true
    }
  },
  methods: {
    on_click: function (event) {
      var elem_data = this.$refs.padcontinuous.getBoundingClientRect()

      var relative_click = {}
      relative_click.x = (event.clientX - elem_data.x) / elem_data.width
      relative_click.y = (event.clientY - elem_data.y) / elem_data.height

      var click_info = {}
      click_info.relative_click = relative_click
      this.callback(click_info)
    }
  }
}

</script>

<style>
/* global styles */

.padcontinuous {
  outline: none; /* remove contour when clicked */
  border: none;
  background-color: rgba(150, 100, 100, 1)
}

.padcontinuous:active {
  background-color: rgba(100, 100, 100, 1);
}

</style>

<style scoped>
/* local styles */
</style>
