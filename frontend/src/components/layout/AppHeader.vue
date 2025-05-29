<template>
  <header class="app-header">
    <div class="container">
      <nav class="nav">
        <router-link to="/" class="logo">HonestyBox</router-link>
        
        <div class="nav-links">
          <router-link to="/map">Farm Map</router-link>
          
          <template v-if="!authStore.isAuthenticated">
            <router-link to="/login">Login</router-link>
            <router-link to="/register" class="btn btn-small">Register Farm</router-link>
          </template>
          
          <template v-else>
            <router-link v-if="authStore.isFarmer" to="/dashboard">Dashboard</router-link>
            <router-link v-if="authStore.isFarmer" to="/products">Products</router-link>
            <router-link v-if="authStore.isAdmin" to="/admin">Admin Panel</router-link>
            <button @click="authStore.logout" class="btn btn-secondary btn-small">Logout</button>
          </template>
        </div>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { useAuthStore } from '../../stores/auth'

const authStore = useAuthStore()
</script>

<style scoped>
.app-header {
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #4CAF50;
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.nav-links a {
  color: #333;
  text-decoration: none;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: #4CAF50;
}
</style>