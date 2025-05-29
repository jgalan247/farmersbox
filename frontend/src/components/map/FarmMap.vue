<template>
  <div class="farm-map">
    <div ref="mapContainer" class="map-container"></div>
    
    <div v-if="selectedFarm" class="farm-popup">
      <div class="popup-header">
        <h3>{{ selectedFarm.farm_name }}</h3>
        <button @click="selectedFarm = null" class="close-btn">&times;</button>
      </div>
      <div class="popup-content">
        <p><strong>Farmer:</strong> {{ selectedFarm.farmer_name }}</p>
        <p v-if="selectedFarm.address"><strong>Address:</strong> {{ selectedFarm.address }}</p>
        <p v-if="selectedFarm.phone"><strong>Phone:</strong> {{ selectedFarm.phone }}</p>
        <p><strong>Products Available:</strong> {{ selectedFarm.products_count }}</p>
        
        <button @click="viewProducts(selectedFarm.id)" class="btn btn-small">
          View Products
        </button>
      </div>
    </div>
    
    <div v-if="showProducts && farmProducts" class="modal" @click.self="closeProducts">
      <div class="modal-content">
        <div class="modal-header">
          <h2>{{ farmProducts.farm.farm_name }} - Products</h2>
          <span @click="closeProducts" class="modal-close">&times;</span>
        </div>
        
        <div v-if="farmProducts.products.length === 0" class="empty-state">
          No products available at the moment.
        </div>
        
        <div v-else class="products-grid">
          <div v-for="product in farmProducts.products" :key="product.id" class="product-card">
            <h4>{{ product.name }}</h4>
            <p v-if="product.description">{{ product.description }}</p>
            <div class="product-details">
              <span class="price">${{ product.price.toFixed(2) }}/{{ product.unit }}</span>
              <span class="quantity">Available: {{ product.quantity_available }} {{ product.unit }}</span>
            </div>
          </div>
        </div>
        
        <div class="contact-info">
          <h3>Contact Information</h3>
          <p><strong>Farmer:</strong> {{ farmProducts.farm.farmer_name }}</p>
          <p v-if="farmProducts.farm.phone"><strong>Phone:</strong> {{ farmProducts.farm.phone }}</p>
          <p v-if="farmProducts.farm.address"><strong>Address:</strong> {{ farmProducts.farm.address }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import L from 'leaflet'
import api from '../../services/api'

const mapContainer = ref(null)
const map = ref(null)
const markers = ref([])
const selectedFarm = ref(null)
const showProducts = ref(false)
const farmProducts = ref(null)

onMounted(async () => {
  // Initialize map
  map.value = L.map(mapContainer.value).setView([40.7128, -74.0060], 10)
  
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map.value)
  
  // Load farms
  await loadFarms()
})

onUnmounted(() => {
  if (map.value) {
    map.value.remove()
  }
})

async function loadFarms() {
  try {
    const response = await api.getPublicFarms()
    const farms = response.data.farms
    
    // Clear existing markers
    markers.value.forEach(marker => marker.remove())
    markers.value = []
    
    // Add markers for each farm
    farms.forEach(farm => {
      if (farm.latitude && farm.longitude) {
        const marker = L.marker([farm.latitude, farm.longitude])
          .addTo(map.value)
          .bindPopup(`<strong>${farm.farm_name}</strong><br>${farm.products_count} products available`)
        
        marker.on('click', () => {
          selectedFarm.value = farm
        })
        
        markers.value.push(marker)
      }
    })
    
    // Fit map to show all markers
    if (markers.value.length > 0) {
      const group = L.featureGroup(markers.value)
      map.value.fitBounds(group.getBounds().pad(0.1))
    }
  } catch (err) {
    console.error('Failed to load farms:', err)
  }
}

async function viewProducts(farmId) {
  try {
    const response = await api.getFarmProducts(farmId)
    farmProducts.value = response.data
    showProducts.value = true
  } catch (err) {
    console.error('Failed to load products:', err)
  }
}

function closeProducts() {
  showProducts.value = false
  farmProducts.value = null
}
</script>

<style scoped>
.farm-map {
  position: relative;
}

.farm-popup {
  position: absolute;
  top: 20px;
  right: 20px;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  max-width: 300px;
  z-index: 1000;
}

.popup-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #666;
}

.popup-content p {
  margin: 5px 0;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.product-card {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 4px;
}

.product-card h4 {
  margin-bottom: 0.5rem;
  color: #4CAF50;
}

.product-details {
  display: flex;
  justify-content: space-between;
  margin-top: 0.5rem;
  font-size: 0.9rem;
}

.price {
  font-weight: bold;
  color: #333;
}

.quantity {
  color: #666;
}

.contact-info {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
}

.contact-info h3 {
  margin-bottom: 1rem;
  color: #333;
}

.contact-info p {
  margin: 0.5rem 0;
}
</style>
