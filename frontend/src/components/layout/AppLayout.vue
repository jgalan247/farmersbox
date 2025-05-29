<template>
  <div class="app-layout">
    <AppHeader />
    <main class="main-content">
      <div class="container">
        <slot />
      </div>
    </main>
  </div>
</template>

<script setup>
import AppHeader from './AppHeader.vue'
</script>

<style scoped>
.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 2rem 0;
}
</style>
