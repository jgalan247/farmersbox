<template>
  <AppLayout>
    <div class="admin-page">
      <h1>Admin Dashboard</h1>
      
      <div class="admin-sections">
        <FarmerApproval />
        
        <div class="all-farmers">
          <h3>All Registered Farmers</h3>
          
          <div v-if="adminStore.loading" class="loading">Loading...</div>
          
          <table v-else-if="adminStore.allFarmers.length > 0" class="table">
            <thead>
              <tr>
                <th>Farm Name</th>
                <th>Owner</th>
                <th>Email</th>
                <th>Status</th>
                <th>Registered</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="farmer in adminStore.allFarmers" :key="farmer.id">
                <td>{{ farmer.farm_name }}</td>
                <td>{{ farmer.name }}</td>
                <td>{{ farmer.email }}</td>
                <td>
                  <span :class="['status', farmer.is_approved ? 'approved' : 'pending']">
                    {{ farmer.is_approved ? 'Approved' : 'Pending' }}
                  </span>
                </td>
                <td>{{ new Date(farmer.created_at).toLocaleDateString() }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAdminStore } from '../stores/admin'
import AppLayout from '../components/layout/AppLayout.vue'
import FarmerApproval from '../components/admin/FarmerApproval.vue'

const adminStore = useAdminStore()

onMounted(() => {
  adminStore.fetchAllFarmers()
})
</script>

<style scoped>
.admin-page h1 {
  margin-bottom: 2rem;
  color: #333;
}

.admin-sections {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.all-farmers {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.all-farmers h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.status {
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.875rem;
}

.status.approved {
  background: #d4edda;
  color: #155724;
}

.status.pending {
  background: #fff3cd;
  color: #856404;
}
</style>