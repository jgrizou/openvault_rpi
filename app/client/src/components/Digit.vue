<template>
  <div>
    <div v-for="(value, index) in flashing">
      <div :class="{
        'round': true,
        ['n' + index]: true,
        'flash': value
        }"
      >
        {{ index }}
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Digit",
  data() {
    return {
      flashing: [true, false, false, false, false, false, false, false, false, true]
    };
  },
  sockets: {
    flash: function (data) {
      this.flashing = data
      this.$socket.emit('log', data)
    }
  }
}

</script>

<style>
/* global styles */

:root {
  --digit_diameter: 90px;
  --digit_spacing: calc(var(--screen_width) / 5);
  --digit_offset: calc( (var(--digit_spacing) - var(--digit_diameter)) / 2);
}

.round {
  position: absolute;
  width: var(--digit_diameter);
  height: var(--digit_diameter);
  border-radius: calc(var(--digit_diameter) / 2); /* rounding */
  text-align: center;
  vertical-align: middle;
  font-size: 80px;
  font-weight: 700;
  font-family: "Helvetica";
  line-height: var(--digit_diameter);
  background-color: var(--off_color);
}

.flash {
  background-color: var(--on_color);
}

.n0 {
  top: calc(0*var(--digit_spacing) + var(--digit_offset));
  left: calc(0*var(--digit_spacing) + var(--digit_offset));
}
.n1 {
  top: calc(0*var(--digit_spacing) + var(--digit_offset));
  left: calc(1*var(--digit_spacing) + var(--digit_offset));
}
.n2 {
  top: calc(0*var(--digit_spacing) + var(--digit_offset));
  left: calc(2*var(--digit_spacing) + var(--digit_offset));
}
.n3 {
  top: calc(0*var(--digit_spacing) + var(--digit_offset));
  left: calc(3*var(--digit_spacing) + var(--digit_offset));
}
.n4 {
  top: calc(0*var(--digit_spacing) + var(--digit_offset));
  left: calc(4*var(--digit_spacing) + var(--digit_offset));
}
.n5 {
  top: calc(1*var(--digit_spacing) + var(--digit_offset));
  left: calc(0*var(--digit_spacing) + var(--digit_offset));
}
.n6 {
  top: calc(1*var(--digit_spacing) + var(--digit_offset));
  left: calc(1*var(--digit_spacing) + var(--digit_offset));
}
.n7 {
  top: calc(1*var(--digit_spacing) + var(--digit_offset));
  left: calc(2*var(--digit_spacing) + var(--digit_offset));
}
.n8 {
  top: calc(1*var(--digit_spacing) + var(--digit_offset));
  left: calc(3*var(--digit_spacing) + var(--digit_offset));
}
.n9 {
  top: calc(1*var(--digit_spacing) + var(--digit_offset));
  left: calc(4*var(--digit_spacing) + var(--digit_offset));
}


</style>

<style scoped>
/* local styles */
</style>
