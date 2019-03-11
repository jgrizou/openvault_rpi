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

.flash {
  background-color: var(--on_color);
  color: var(--on_color_active);
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

</style>
