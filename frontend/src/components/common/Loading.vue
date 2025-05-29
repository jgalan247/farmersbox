<template>
  <div class="loading-container" :class="{ 'full-screen': fullScreen }">
    <div class="loading-spinner" :class="size">
      <div class="spinner">
        <div class="double-bounce1"></div>
        <div class="double-bounce2"></div>
      </div>
      <p v-if="text" class="loading-text">{{ text }}</p>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

// Props
const props = defineProps({
  text: {
    type: String,
    default: 'Loading...'
  },
  size: {
    type: String,
    default: 'medium',
    validator: (value) => ['small', 'medium', 'large'].includes(value)
  },
  fullScreen: {
    type: Boolean,
    default: false
  }
})
</script>

<style scoped>
.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.loading-container.full-screen {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255, 255, 255, 0.9);
  z-index: 9999;
}

.loading-spinner {
  text-align: center;
}

.spinner {
  position: relative;
  display: inline-block;
}

/* Size variations */
.small .spinner {
  width: 30px;
  height: 30px;
}

.medium .spinner {
  width: 40px;
  height: 40px;
}

.large .spinner {
  width: 60px;
  height: 60px;
}

.double-bounce1, .double-bounce2 {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #4CAF50;
  opacity: 0.6;
  position: absolute;
  top: 0;
  left: 0;
  animation: sk-bounce 2.0s infinite ease-in-out;
}

.double-bounce2 {
  animation-delay: -1.0s;
}

@keyframes sk-bounce {
  0%, 100% { 
    transform: scale(0.0);
  } 50% { 
    transform: scale(1.0);
  }
}

.loading-text {
  margin-top: 1rem;
  color: #666;
  font-size: 0.875rem;
}

.small .loading-text {
  font-size: 0.75rem;
  margin-top: 0.5rem;
}

.large .loading-text {
  font-size: 1rem;
  margin-top: 1.5rem;
}

/* Alternative spinner style - you can swap by changing the template */
.spinner-alt {
  display: inline-block;
  position: relative;
}

.spinner-alt:after {
  content: " ";
  display: block;
  border-radius: 50%;
  width: 0;
  height: 0;
  margin: 8px;
  box-sizing: border-box;
  border: 32px solid #4CAF50;
  border-color: #4CAF50 transparent #4CAF50 transparent;
  animation: spinner-alt 1.2s infinite;
}

.small .spinner-alt:after {
  border-width: 20px;
  margin: 5px;
}

.large .spinner-alt:after {
  border-width: 40px;
  margin: 10px;
}

@keyframes spinner-alt {
  0% {
    transform: rotate(0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  50% {
    transform: rotate(900deg);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  100% {
    transform: rotate(1800deg);
  }
}
</style>