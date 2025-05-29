<template>
  <AppLayout>
    <div class="products-page">
      <h1>Manage Products</h1>
      
      <div v-if="!authStore.isApproved" class="alert alert-warning">
        Your account is pending approval. You cannot manage products yet.
      </div>
      
      <template v-else>
        <ProductForm />
        <ProductList />
      </template>
    </div>
  </AppLayout>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useProductsStore } from '../stores/products'
import AppLayout from '../components/layout/AppLayout.vue'
import ProductForm from '../components/products/ProductForm.vue'
import ProductList from '../components/products/ProductList.vue'

const authStore = useAuthStore()
const productsStore = useProductsStore()

onMounted(() => {
  if (authStore.isApproved) {
    productsStore.fetchProducts()
  }
})
</script>

<style scoped>
.products-page h1 {
  margin-bottom: 2rem;
  color: #333;
}
</style>

# ===== frontend/src/views/PublicMapView.vue =====
<template>
  <AppLayout>
    <div class="map-page">
      <h1>Find Local Farms</h1>
      <p class="subtitle">Click on markers to view farm details and available products</p>
      
      <FarmMap />
    </div>
  </AppLayout>
</template>

<script setup>
import AppLayout from '../components/layout/AppLayout.vue'
import FarmMap from '../components/map/FarmMap.vue'
</script>

<style scoped>
.map-page h1 {
  margin-bottom: 0.5rem;
  color: #333;
}

.subtitle {
  margin-bottom: 2rem;
  color: #666;
}
</style>