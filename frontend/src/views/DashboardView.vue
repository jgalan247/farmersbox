<template>
  <AppLayout>
    <div class="dashboard">
      <h1>Farmer Dashboard</h1>
      
      <div v-if="!authStore.isApproved" class="alert alert-warning">
        Your account is pending approval. You'll be able to manage products once approved.
      </div>
      
      <div class="dashboard-grid">
        <div class="info-card">
          <h3>Farm Information</h3>
          <p><strong>Farm Name:</strong> {{ authStore.user?.farm_name }}</p>
          <p><strong>Owner:</strong> {{ authStore.user?.name }}</p>
          <p><strong>Email:</strong> {{ authStore.user?.email }}</p>
          <p><strong>Location:</strong> {{ authStore.user?.latitude }}, {{ authStore.user?.longitude }}</p>
          <p v-if="authStore.user?.phone"><strong>Phone:</strong> {{ authStore.user?.phone }}</p>
          <p v-if="authStore.user?.address"><strong>Address:</strong> {{ authStore.user?.address }}</p>
        </div>
        
        <div class="stats-card">
          <h3>Quick Stats</h3>
          <div class="stats">
            <div class="stat">
              <div class="stat-value">{{ productCount }}</div>
              <div class="stat-label">Total Products</div>
            </div>
            <div class="stat">
              <div class="stat-value">{{ availableCount }}</div>
              <div class="stat-label">Available</div>
            </div>
          </div>
          
          <router-link to="/products" class="btn btn-small" v-if="authStore.isApproved">
            Manage Products
          </router-link>
        </div>
      </div>
      
      <div class="recent-products" v-if="authStore.isApproved">
        <h2>Recent Products</h2>
        <div v-if="recentProducts.length === 0" class="empty-state">
          <p>No products yet. <router-link to="/products">Add your first product</router-link></p>
        </div>
        <div v-else class="products-preview">
          <div v-for="product in recentProducts" :key="product.id" class="product-item">
            <h4>{{ product.name }}</h4>
            <p>${{ product.price.toFixed(2) }}/{{ product.unit }}</p>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useProductsStore } from '../stores/products'
import AppLayout from '../components/layout/AppLayout.vue'

const authStore = useAuthStore()
const productsStore = useProductsStore()

const productCount = computed(() => productsStore.products.length)
const availableCount = computed(() => 
  productsStore.products.filter(p => p.is_available).length
)
const recentProducts = computed(() => 
  productsStore.products.slice(0, 5)
)

onMounted(() => {
  if (authStore.isApproved) {
    productsStore.fetchProducts()
  }
})
</script>

<style scoped>
.dashboard h1 {
  margin-bottom: 2rem;
  color: #333;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 3rem;
}

.info-card,
.stats-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.info-card h3,
.stats-card h3 {
  margin-bottom: 1.5rem;
  color: #4CAF50;
}

.info-card p {
  margin: 0.5rem 0;
}

.stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat {
  text-align: center;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #333;
}

.stat-label {
  color: #666;
  font-size: 0.9rem;
}

.recent-products {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.recent-products h2 {
  margin-bottom: 1.5rem;
  color: #333;
}

.products-preview {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.product-item {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 4px;
}

.product-item h4 {
  margin-bottom: 0.5rem;
  color: #4CAF50;
}

.empty-state {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.empty-state a {
  color: #4CAF50;
}

@media (max-width: 768px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}
</style>
