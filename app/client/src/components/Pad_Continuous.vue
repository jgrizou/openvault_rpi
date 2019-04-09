<template>
  <div
    ref="padcontinuous"
    class="padcontinuous"
    v-on:click="on_click"
    v-on:mousedown="mouseDown"
  >
  </div>
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
    },
    mouseDown: function (event) {
      var elem_data = this.$refs.padcontinuous

      // Get necessary variables
      var rect        = elem_data.getBoundingClientRect(),
          left        = rect.left,
          top         = rect.top,
          width       = elem_data.offsetWidth,
          height      = elem_data.offsetHeight,
          dx          = event.clientX - left,
          dy          = event.clientY - top,
          maxX        = Math.max(dx, width - dx),
          maxY        = Math.max(dy, height - dy),
          style       = window.getComputedStyle(elem_data),
          radius      = Math.sqrt((maxX * maxX) + (maxY * maxY));


      var ripple_center_X = dx
      var ripple_center_Y = dy
      // modified center for the rpi screen that is 90degree rotated
      // var ripple_center_X = (480-dy)
      // var ripple_center_Y = dx

      //Ripple
      var rippleEffect = document.createElement("div");
      rippleEffect.className = 'ripple-effect';
      rippleEffect.style.marginLeft = ripple_center_X + "px";
      rippleEffect.style.marginTop  = ripple_center_Y + "px";

      //rippleContainer
      var rippleContainer = document.createElement("div");
      rippleContainer.className = 'ripple-container';
      rippleContainer.appendChild(rippleEffect);
      rippleContainer.style.width   = width + "px";
      rippleContainer.style.height  = height + "px";

      elem_data.appendChild(rippleContainer);

      // timeout needed to ensure the previous is applied first
      setTimeout(function() {
          rippleEffect.style.marginLeft   = ripple_center_X - radius + "px";
          rippleEffect.style.marginTop    = ripple_center_Y - radius + "px";
           rippleEffect.style.width  = radius * 2 + "px";
           rippleEffect.style.height = radius * 2 + "px";
       }, 0);

       setTimeout(function() {
           rippleEffect.style.backgroundColor = "rgba(0, 0, 0, 0)";
       }, 250);

       setTimeout(function() {
           rippleContainer.parentNode.removeChild(rippleContainer);
       }, 1000);
    }
  }
}

</script>

<style>
/* global styles */

.padcontinuous {
  background-color: rgba(255, 255, 255, 1);
}

.ripple-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
    pointer-events: none;
    overflow: hidden;
}

.ripple-effect {
    position:relative;
    margin-top: 0px;
    margin-left: 0px;
    width: 1px;
    height: 1px;
    transition: all 1s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 50%;
    pointer-events: none;
    z-index: 9999;
    background-color: rgba(0, 0, 0, 0.35);
}

</style>

<style scoped>
/* local styles */
</style>
