<template>
  <div>

    <div v-if="!show_message">
      <div v-for="(value, index) in flash">
        <div :class="{
          'round': true,
          ['n' + index]: true,
          'digit-flash': value,
          'digit-noflash': !value
          }"
        >
          {{ index }}
        </div>
      </div>
    </div>
    <div v-else class="message">
      Calculating...
    </div>

  </div>
</template>

<script>

export default {
  name: "Digit",
  data() {
    return {
      show_message: false,
      flash: undefined
    };
  }
}

</script>

<style>
/* global styles */

.message {
  position: relative;
  top: 60px;
  text-align: center;
  vertical-align: middle;
  font-size: 50px;
  font-weight: 600;
  color: rgba(50, 50, 50, 1);
}


.digit-noflash {
  background-color: var(--off_color_letter_background);
  color: var(--off_color_active);
}

.digit-flash {
  background-color: var(--on_color_letter_background);
  color: var(--on_color_active);
}

:root {
  --digit_diameter: 72px;
  --digit_margin: 50px;
  --digit_spacing: calc((var(--screen_width) - 2*var(--digit_margin)) / 5);
  --digit_offset: calc( (var(--digit_spacing) - var(--digit_diameter)) / 2);
}

.round {
  position: absolute;
  width: var(--digit_diameter);
  height: var(--digit_diameter);
  border-radius: calc(var(--digit_diameter) / 2);
  text-align: center;
  vertical-align: middle;
  font-size: 40px;
  font-weight: 600;
  line-height: calc( var(--digit_diameter) + var(--digit_offset));
}

.n0 {
  top: calc(0*var(--digit_spacing));
  left: calc(var(--digit_margin) + 0*var(--digit_spacing) + var(--digit_offset));
}
.n1 {
  top: calc(0*var(--digit_spacing));
  left: calc(var(--digit_margin) + 1*var(--digit_spacing) + var(--digit_offset));
}
.n2 {
  top: calc(0*var(--digit_spacing));
  left: calc(var(--digit_margin) + 2*var(--digit_spacing) + var(--digit_offset));
}
.n3 {
  top: calc(0*var(--digit_spacing));
  left: calc(var(--digit_margin) + 3*var(--digit_spacing) + var(--digit_offset));
}
.n4 {
  top: calc(0*var(--digit_spacing));
  left: calc(var(--digit_margin) + 4*var(--digit_spacing) + var(--digit_offset));
}
.n5 {
  top: calc(1*var(--digit_spacing));
  left: calc(var(--digit_margin) + 0*var(--digit_spacing) + var(--digit_offset));
}
.n6 {
  top: calc(1*var(--digit_spacing));
  left: calc(var(--digit_margin) + 1*var(--digit_spacing) + var(--digit_offset));
}
.n7 {
  top: calc(1*var(--digit_spacing));
  left: calc(var(--digit_margin) + 2*var(--digit_spacing) + var(--digit_offset));
}
.n8 {
  top: calc(1*var(--digit_spacing));
  left: calc(var(--digit_margin) + 3*var(--digit_spacing) + var(--digit_offset));
}
.n9 {
  top: calc(1*var(--digit_spacing));
  left: calc(var(--digit_margin) + 4*var(--digit_spacing) + var(--digit_offset));
}

</style>

<style scoped>
/* local styles */
</style>
