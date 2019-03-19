<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>

:root {
  --screen_width: 480px;
  --screen_height: 800px;
  --display_height: 150px;
  --digit_height: calc( var(--screen_width) / 5 * 2); /* 5 digits per row on 2 column */
  --pad_height: calc( var(--screen_height) - var(--display_height) - var(--digit_height));

  --on_color: rgba(0, 200, 255, 1);
  --on_color_active: rgba(0, 150, 205);
  --off_color: rgba(255, 200, 0, 1);
  --off_color_active: rgba(205, 150, 0, 1);
  --neutral_color: rgba(200, 200, 200, 1);
  --neutral_color_active: rgba(150, 150, 150, 1);
}

#app {
  position: fixed;
  left: 0px;
  top: 0px;
  width: var(--screen_width);
  height: var(--screen_height);
  transform: rotate(270deg) translateX(160px) translateY(160px);
}

.noflash {
  background-color: var(--off_color);
  color: var(--off_color_active);
}

.noflash:active {
  background-color: var(--off_color_active);
}

.flash {
  background-color: var(--on_color);
  color: var(--on_color_active);
}

.flash:active {
  background-color: var(--on_color_active);
}

.neutral {
  background-color: var(--neutral_color);
  color: var(--neutral_color_active);
}

.neutral:active {
  background-color: var(--neutral_color_active);
}


.fullscreen {
  position: absolute;
  top: 0px;
  width: var(--screen_width);
  height: var(--screen_height);
  background-color: rgba(255, 255, 255, 1);
}

.display {
  position: absolute;
  top: 0px;
  width: var(--screen_width);
  height: var(--display_height);
  background-color: rgba(255, 255, 255, 1);
}

.digit {
  position: absolute;
  top: var(--display_height);
  width: var(--screen_width);
  height: var(--digit_height);
  background-color: rgba(255, 255, 255, 1);
}

.pad {
  position: absolute;
  top: calc( var(--display_height) + var(--digit_height) );
  width: var(--screen_width);
  height: var(--pad_height);
  background-color: rgba(255, 255, 255, 1);
}

.btn {
  border-radius: 15px; /* rounding */
  box-shadow: 0 20px rgba(130, 130, 130, 1);
}

.btn:active {
  box-shadow: 0 5px rgba(100, 100, 100, 1);
  transform: translateY(15px);
}

</style>
