<template xmlns:v-bind="http://www.w3.org/1999/xhtml">
  <div id="app">
    <nav class="navbar navbar-expand">
      <a href="/" class="navbar-brand">PBS</a>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <a href="/products" class="nav-link">Products</a>
        </li>
      </div>
    </nav>
    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class App extends Vue {
}
</script>

<style>
  body {
    background-color: #b3b2b2
  }
  nav {
    background-color: #4c55ed;
  }
  a {
    color: black;
  }
</style>
