<template>
  <AppLayout>
    <div class="home-view">
      <div class="hero">
        <h1>Welcome to HonestyBox</h1>
        <p class="hero-subtitle">Connect with local farmers and buy fresh produce directly from the source</p>
        
        <div class="hero-actions">
          <router-link to="/map" class="btn">Browse Farms</router-link>
          <router-link to="/register" class="btn btn-secondary">Register Your Farm</router-link>
        </div>
      </div>
      
      <div class="features">
        <div class="feature">
          <h3>For Customers</h3>
          <p>Find fresh, local produce directly from farmers in your area. View available products and contact farmers directly.</p>
        </div>
        
        <div class="feature">
          <h3>For Farmers</h3>
          <p>List your products online, manage inventory, and connect with customers looking for fresh, local produce.</p>
        </div>
        
        <div class="feature">
          <h3>Trust & Transparency</h3>
          <p>All farmers are verified by our admin team to ensure quality and authenticity.</p>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import AppLayout from '../components/layout/AppLayout.vue'
</script>

<style scoped>
.home-view {
  max-width: 1200px;
  margin: 0 auto;
}

.hero {
  text-align: center;
  padding: 4rem 0;
}

.hero h1 {
  font-size: 3rem;
  color: #333;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: #666;
  margin-bottom: 2rem;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 4rem;
}

.feature {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  text-align: center;
}

.feature h3 {
  color: #4CAF50;
  margin-bottom: 1rem;
}

.feature p {
  color: #666;
  line-height: 1.6;
}
</style>