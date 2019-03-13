<template>
  <div>

    <div class="check">

    </div>

  </div>
</template>

<script>

export default {
  name: "Check",
}

</script>

<style>
/* global styles */

.check {
  position: absolute;
  top: var(--display_height);
  width: var(--screen_width);
  height: calc( var(--screen_height) - var(--display_height) );
  background-color: rgba(255, 0, 0, 1);
}

</style>

<style scoped>
/* local styles */
</style>
