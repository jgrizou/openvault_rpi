<template>
  <div>
    <div v-for="(item, index) in code">
      <div :class="{
        'tile': true,
        ['c' + index]: true,
        'found': item['found'],
        'ongoing': item['ongoing'],
        }"
      >
        {{ item['text'] }}
      </div>
    </div>

    <button :class="{'reset' : true, 'reset_active': reset_active}" v-on:click="reset">{{ n_iteration }} Reset</button>

  </div>
</template>

<script>

export default {
  name: 'Display',
  data() {
    return {
      n_iteration: 0,
      reset_active: false,
      code: [
        {'found': false, 'ongoing': false, 'text': ''},
        {'found': false, 'ongoing': false, 'text': ''},
        {'found': false, 'ongoing': false, 'text': ''},
        {'found': false, 'ongoing': false, 'text': ''}
      ]
    }
  },
  sockets: {
    n_iteration: function (n_iteration) {
      this.n_iteration = n_iteration
      this.reset_active = n_iteration > 0
    }
  },
  methods: {
    reset: function () {
      this.$socket.emit('reset')
    }
  }
}

</script>

<style>
/* global styles */

:root {
  --tile_width: 80px;
  --tile_height: 100px;
  --top_offset: 10px;
  --tile_offset: 70px;
  --tile_spacing: calc( ( (var(--screen_width) - 2*var(--tile_offset)) - 4*var(--tile_width)) / 3 );
  --tile_color: rgba(200, 200, 200, 1);
  --tile_border: 5px;
}

.reset {
  position: absolute;
  top: 40px;
  right: 5px;
  width: 45px;
  height: 35px;
  outline: none; /* remove contour when clicked */
  border: none;
  border-radius: 5px; /* rounding */
  background-color: rgba(230, 230, 230, 1);
}

.reset_active {
  background-color: rgba(255, 100, 100, 1);
}

.tile {
  position: absolute;
  width: var(--tile_width);
  height: var(--tile_height);
  border-radius: 5px; /* rounding */
  text-align: center;
  vertical-align: middle;
  font-size: 90px;
  font-weight: 700;
  font-family: "Helvetica";
  line-height: var(--tile_height);
  background-color: var(--tile_color);
}

.ongoing {
  width: calc( var(--tile_width) - 2*var(--tile_border) );
  height: calc( var(--tile_height) - 2*var(--tile_border) );
  line-height: calc( var(--tile_height) - var(--tile_border) );
  border-width: var(--tile_border);
  border-style: solid;
  border-color: rgba(100, 100, 100, 1);
  background-color: rgba(230, 230, 230, 1);
}

.found {
  background-color: rgba(230, 230, 230, 1);
}

.c0 {
  top: var(--top_offset);
  left: calc( var(--tile_offset) + 0 * (var(--tile_width) + var(--tile_spacing)) );
}

.c1 {
  top: var(--top_offset);
  left: calc( var(--tile_offset) + 1 * (var(--tile_width) + var(--tile_spacing)) );
}

.c2 {
  top: var(--top_offset);
  left: calc( var(--tile_offset) + 2 * (var(--tile_width) + var(--tile_spacing)) );
}

.c3 {
  top: var(--top_offset);
  left: calc( var(--tile_offset) + 3 * (var(--tile_width) + var(--tile_spacing)) );
}


</style>

<style scoped>
/* local styles */
</style>
