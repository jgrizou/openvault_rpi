<template>
  <div>
    <button
      class='btn btn-left'
      v-on:click="on_click('left')">
    </button>
    <button
      class='btn btn-right'
      v-on:click="on_click('right')">
    </button>
  </div>
</template>

<script>

export default {
  name: 'Pad',
  methods: {
    on_click: function (button_name, event) {
      var click_info = {}
      click_info.feedback_info = button_name
      this.$socket.emit('click', click_info)
    }
  }
}

</script>

<style>
/* global styles */

.btn {
  position: absolute;
  top: 50px;
  width: 200px;
  height: 350px;
  outline: none; /* remove contour when clicked */
  border: none;
  border-radius: 15px; /* rounding */
  box-shadow: 0 20px rgba(130, 130, 130, 1);
}

.btn:active {
  box-shadow: 0 5px rgba(100, 100, 100, 1);
  transform: translateY(15px);
}

.btn-left {
  left: 20px;
  background-color: var(--off_color);
}

.btn-left:active {
  background-color: var(--off_color_active);
}

.btn-right {
  right: 20px;
  background-color: var(--on_color);
}

.btn-right:active {
  background-color: var(--on_color_active);
}

</style>

<style scoped>
/* local styles */
</style>
