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

#app {
  position: fixed;
  left: 0px;
  top: 0px;
  width: 480px;
  height: 800px;
  transform: rotate(270deg) translateX(160px) translateY(160px);
}

</style>
