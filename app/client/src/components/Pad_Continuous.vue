<template>
  <div
    v-ripple
    ref="padcontinuous"
    class="padcontinuous"
    v-on:click="on_click"
    v-on:mousedown="mouseDown"
    v-on:mouseup="mouseUp"
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
      this.$socket.emit('log', 'down')

      var target = this.$refs.padcontinuous

      // Get border to avoid offsetting on ripple container position
      var targetBorder = parseInt((getComputedStyle(target).borderWidth).replace('px', ''));

      // Get necessary variables
      var rect        = target.getBoundingClientRect(),
          left        = rect.left,
          top         = rect.top,
          width       = target.offsetWidth,
          height      = target.offsetHeight,
          dx          = event.clientX - left,
          dy          = event.clientY - top,
          maxX        = Math.max(dx, width - dx),
          maxY        = Math.max(dy, height - dy),
          style       = window.getComputedStyle(target),
          radius      = Math.sqrt((maxX * maxX) + (maxY * maxY)),
          border      = (targetBorder > 0 ) ? targetBorder : 0;

      // Create the ripple and its container
      var ripple = document.createElement("div"),
          rippleContainer = document.createElement("div");
          rippleContainer.className = 'ripple-container';
          ripple.className = 'ripple';

      //Styles for ripple
      ripple.style.marginTop= '0px';
      ripple.style.marginLeft= '0px';
      ripple.style.width= '1px';
      ripple.style.height= '1px';
      ripple.style.transition= 'all 600ms cubic-bezier(0.4, 0, 0.2, 1)';
      ripple.style.borderRadius= '50%';
      ripple.style.pointerEvents= 'none';
      ripple.style.position= 'relative';
      ripple.style.zIndex= '9999';
      ripple.style.backgroundColor  = 'rgba(0, 0, 0, 0.35)';

      //Styles for rippleContainer
      rippleContainer.style.position= 'absolute';
      rippleContainer.style.left = 0 - border + 'px';
      rippleContainer.style.top = 0 - border + 'px';
      rippleContainer.style.height = '0';
      rippleContainer.style.width = '0';
      rippleContainer.style.pointerEvents = 'none';
      rippleContainer.style.overflow = 'hidden';


      // Store target position to change it after
      var storedTargetPosition =  ((target.style.position).length > 0) ? target.style.position : getComputedStyle(target).position;
      // Change target position to relative to guarantee ripples correct positioning
      if (storedTargetPosition !== 'relative') {
          target.style.position = 'relative';
      }

      rippleContainer.appendChild(ripple);
      target.appendChild(rippleContainer);

      ripple.style.marginLeft   = dx + "px";
      ripple.style.marginTop    = dy + "px";

      // No need to set positioning because ripple should be child of target and to it's relative position.
      // rippleContainer.style.left    = left + (((window.pageXOffset || document.scrollLeft) - (document.clientLeft || 0)) || 0) + "px";
      // rippleContainer.style.top     = top + (((window.pageYOffset || document.scrollTop) - (document.clientTop || 0)) || 0) + "px";
      rippleContainer.style.width   = width + "px";
      rippleContainer.style.height  = height + "px";
      rippleContainer.style.borderTopLeftRadius  = style.borderTopLeftRadius;
      rippleContainer.style.borderTopRightRadius  = style.borderTopRightRadius;
      rippleContainer.style.borderBottomLeftRadius  = style.borderBottomLeftRadius;
      rippleContainer.style.borderBottomRightRadius  = style.borderBottomRightRadius;

      rippleContainer.style.direction = 'ltr';

      setTimeout(function() {
           ripple.style.width  = radius * 2 + "px";
           ripple.style.height = radius * 2 + "px";
           ripple.style.marginLeft   = dx - radius + "px";
           ripple.style.marginTop    = dy - radius + "px";
       }, 0);

    },
    mouseUp: function(event) {
      this.$socket.emit('log', 'up')

      var ripple

      var target = this.$refs.padcontinuous

      var ripple = target.querySelector('.ripple');
      var rippleContainer = target.querySelector('.ripple-container');

      setTimeout(function() {
          ripple.style.backgroundColor = "rgba(0, 0, 0, 0)";
      }, 250);

      // Timeout set to get a smooth removal of the ripple
      setTimeout(function() {
          rippleContainer.parentNode.removeChild(rippleContainer);
      }, 850);

      // After removing event set position to target to it's original one
      // Timeout it's needed to avoid jerky effect of ripple jumping out parent target
      setTimeout(function () {

          var clearPosition = true;
          for(var i = 0; i < target.childNodes.length; i++) {
              if(target.childNodes[i].className === 'ripple-container') {
                  clearPosition = false;
              }
          }

          if(clearPosition) {
              if(storedTargetPosition !== 'static') {
                  target.style.position = storedTargetPosition;
              } else {
                  target.style.position = '';
              }
          }

      }, props.transition + 250)


    }
  }
}

</script>

<style>
/* global styles */

.padcontinuous {
  background-color: rgba(200, 200, 200, 1);
}

/* .padcontinuous:active {
  background-color: rgba(100, 100, 100, 1);
} */


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
    margin-top: 0px;
    margin-left: 0px;
    width: 1px;
    height: 1px;
    transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 50%;
    pointer-events: none;
    position:relative;
    z-index: 9999;
}



</style>

<style scoped>
/* local styles */
</style>
