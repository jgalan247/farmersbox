<template>
  <div class="farmer-approval">
    <h3>Pending Farmer Approvals</h3>
    
    <div v-if="adminStore.loading" class="loading">Loading...</div>
    
    <div v-else-if="adminStore.pendingFarmers.length === 0" class="empty-state">
      <p>No pending farmer registrations.</p>
    </div>
    
    <div v-else class="farmers-grid">
      <div v-for="farmer in adminStore.pendingFarmers" :key="farmer.id" class="farmer-card">
        <h4>{{ farmer.farm_name }}</h4>
        <p><strong>Name:</strong> {{ farmer.name }}</p>
        <p><strong>Email:</strong> {{ farmer.email }}</p>
        <p v-if="farmer.phone"><strong>Phone:</strong> {{ farmer.phone }}</p>
        <p v-if="farmer.address"><strong>Address:</strong> {{ farmer.address }}</p>
        <p><strong>Location:</strong> {{ farmer.latitude }}, {{ farmer.longitude }}</p>
        <p><strong>Registered:</strong> {{ new Date(farmer.created_at).toLocaleDateString() }}</p>
        
        <div class="actions">
          <button @click="approveFarmer(farmer.id)" class="btn btn-small">
            Approve
          </button>
          <button @click="rejectFarmer(farmer.id)" class="btn btn-danger btn-small">
            Reject
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAdminStore } from '../../stores/admin'

const adminStore = useAdminStore()

onMounted(() => {
  adminStore.fetchPendingFarmers()
})

async function approveFarmer(id) {
  if (confirm('Approve this farmer registration?')) {
    try {
      await adminStore.approveFarmer(id)
    } catch (err) {
      console.error('Failed to approve:', err)
    }
  }
}

async function rejectFarmer(id) {
  if (confirm('Reject and delete this farmer registration?')) {
    try {
      await adminStore.rejectFarmer(id)
    } catch (err) {
      console.error('Failed to reject:', err)
    }
  }
}
</script>

<style scoped>
.farmer-approval {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.farmer-approval h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.farmers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.farmer-card {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 4px;
  border: 1px solid #ddd;
}

.farmer-card h4 {
  margin-bottom: 1rem;
  color: #4CAF50;
}

.farmer-card p {
  margin: 0.5rem 0;
  font-size: 0.9rem;
}

.farmer-card .actions {
  margin-top: 1rem;
  display: flex;
  gap: 0.5rem;
}

.empty-state {
  text-align: center;
  padding: 3rem;
  color: #666;
}
</style>