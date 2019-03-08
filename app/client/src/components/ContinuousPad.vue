<template>
  <div
    ref='pad'
    v-on:click="on_click"
  >
    <h1>Continuous Pad</h1>
  </div>
</template>

<script>

export default {
  name: 'Pad',
  methods: {
    on_click: function (event) {
      var elem_data = this.$refs.pad.getBoundingClientRect()

      var relative_click = {}
      relative_click.x = (event.clientX - elem_data.x) / elem_data.width
      relative_click.y = (event.clientY - elem_data.y) / elem_data.height

      var feedback_info = {}
      feedback_info.relative_click = relative_click

      this.$socket.emit('click', feedback_info)
    }
  }
}

</script>

<style>
/* global styles */

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
