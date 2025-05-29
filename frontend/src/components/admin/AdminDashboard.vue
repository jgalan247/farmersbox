<template>
  <div class="admin-dashboard">
    <div class="dashboard-header">
      <h2>Admin Dashboard</h2>
      <p class="welcome-message">Welcome back, {{ authStore.user?.name }}</p>
    </div>

    <!-- Stats Overview -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon farmers">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
          </svg>
        </div>
        <div class="stat-content">
          <h3>Total Farmers</h3>
          <p class="stat-value">{{ stats.totalFarmers }}</p>
          <p class="stat-change">
            <span :class="stats.newFarmersThisWeek > 0 ? 'positive' : 'neutral'">
              +{{ stats.newFarmersThisWeek }} this week
            </span>
          </p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon pending">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
        </div>
        <div class="stat-content">
          <h3>Pending Approvals</h3>
          <p class="stat-value">{{ stats.pendingApprovals }}</p>
          <p class="stat-change">
            <span :class="stats.pendingApprovals > 0 ? 'warning' : 'neutral'">
              {{ stats.pendingApprovals > 0 ? 'Requires attention' : 'All clear' }}
            </span>
          </p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon products">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <path d="M16 10a4 4 0 0 1-8 0"></path>
          </svg>
        </div>
        <div class="stat-content">
          <h3>Total Products</h3>
          <p class="stat-value">{{ stats.totalProducts }}</p>
          <p class="stat-change">
            <span class="neutral">Across all farms</span>
          </p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon active">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
          </svg>
        </div>
        <div class="stat-content">
          <h3>Active Farms</h3>
          <p class="stat-value">{{ stats.activeFarms }}</p>
          <p class="stat-change">
            <span class="positive">{{ stats.activePercentage }}% of total</span>
          </p>
        </div>
      </div>
    </div>

    <!-- Recent Activity -->
    <div class="activity-section">
      <h3>Recent Activity</h3>
      <div class="activity-list">
        <div v-if="loadingActivity" class="loading">Loading activity...</div>
        <div v-else-if="recentActivity.length === 0" class="empty-state">
          No recent activity
        </div>
        <div v-else>
          <div v-for="activity in recentActivity" :key="activity.id" class="activity-item">
            <div class="activity-icon" :class="activity.type">
              <svg v-if="activity.type === 'registration'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="8.5" cy="7" r="4"></circle>
                <line x1="20" y1="8" x2="20" y2="14"></line>
                <line x1="23" y1="11" x2="17" y2="11"></line>
              </svg>
              <svg v-else-if="activity.type === 'product'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <path d="M16 10a4 4 0 0 1-8 0"></path>
              </svg>
            </div>
            <div class="activity-content">
              <p class="activity-message">{{ activity.message }}</p>
              <p class="activity-time">{{ formatTime(activity.timestamp) }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="quick-actions">
      <h3>Quick Actions</h3>
      <div class="action-buttons">
        <button @click="navigateToPending" class="action-btn pending">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M9 11l3 3L22 4"></path>
            <path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"></path>
          </svg>
          Review Pending Farmers
        </button>
        
        <button @click="exportData" class="action-btn export">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="7 10 12 15 17 10"></polyline>
            <line x1="12" y1="15" x2="12" y2="3"></line>
          </svg>
          Export Farmer Data
        </button>
        
        <button @click="viewAllFarmers" class="action-btn view">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
            <circle cx="12" cy="12" r="3"></circle>
          </svg>
          View All Farmers
        </button>
      </div>
    </div>

    <!-- Farmers Table Preview -->
    <div class="farmers-preview">
      <div class="section-header">
        <h3>Recently Registered Farmers</h3>
        <router-link to="/admin" class="view-all-link">View All →</router-link>
      </div>
      
      <div v-if="loadingFarmers" class="loading">Loading farmers...</div>
      <table v-else-if="recentFarmers.length > 0" class="farmers-table">
        <thead>
          <tr>
            <th>Farm Name</th>
            <th>Owner</th>
            <th>Location</th>
            <th>Status</th>
            <th>Registered</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="farmer in recentFarmers" :key="farmer.id">
            <td>{{ farmer.farm_name }}</td>
            <td>{{ farmer.name }}</td>
            <td>{{ farmer.address || `${farmer.latitude}, ${farmer.longitude}` }}</td>
            <td>
              <span :class="['status-badge', farmer.is_approved ? 'approved' : 'pending']">
                {{ farmer.is_approved ? 'Approved' : 'Pending' }}
              </span>
            </td>
            <td>{{ formatDate(farmer.created_at) }}</td>
          </tr>
        </tbody>
      </table>
      <div v-else class="empty-state">
        No farmers registered yet
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'
import { useAdminStore } from '../../stores/admin'
import api from '../../services/api'

const router = useRouter()
const authStore = useAuthStore()
const adminStore = useAdminStore()

// State
const stats = ref({
  totalFarmers: 0,
  pendingApprovals: 0,
  totalProducts: 0,
  activeFarms: 0,
  newFarmersThisWeek: 0,
  activePercentage: 0
})

const recentActivity = ref([])
const recentFarmers = ref([])
const loadingActivity = ref(true)
const loadingFarmers = ref(true)

// Computed
const pendingCount = computed(() => adminStore.pendingFarmers.length)

// Methods
async function loadDashboardData() {
  try {
    // Load farmers
    await adminStore.fetchAllFarmers()
    await adminStore.fetchPendingFarmers()
    
    // Calculate stats
    const allFarmers = adminStore.allFarmers
    stats.value.totalFarmers = allFarmers.length
    stats.value.pendingApprovals = adminStore.pendingFarmers.length
    
    // Calculate active farms (approved farmers)
    const approvedFarmers = allFarmers.filter(f => f.is_approved)
    stats.value.activeFarms = approvedFarmers.length
    stats.value.activePercentage = allFarmers.length > 0 
      ? Math.round((approvedFarmers.length / allFarmers.length) * 100)
      : 0
    
    // Calculate new farmers this week
    const oneWeekAgo = new Date()
    oneWeekAgo.setDate(oneWeekAgo.getDate() - 7)
    stats.value.newFarmersThisWeek = allFarmers.filter(f => 
      new Date(f.created_at) > oneWeekAgo
    ).length
    
    // Get recent farmers (last 5)
    recentFarmers.value = allFarmers
      .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      .slice(0, 5)
    
    // Simulate total products count (in real app, this would be an API call)
    stats.value.totalProducts = approvedFarmers.length * 8 // Dummy calculation
    
    // Generate recent activity
    generateRecentActivity(allFarmers)
    
    loadingFarmers.value = false
    loadingActivity.value = false
  } catch (error) {
    console.error('Failed to load dashboard data:', error)
    loadingFarmers.value = false
    loadingActivity.value = false
  }
}

function generateRecentActivity(farmers) {
  // In a real app, this would come from an activity log API
  const activities = []
  
  // Add recent registrations
  farmers
    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
    .slice(0, 3)
    .forEach(farmer => {
      activities.push({
        id: `reg-${farmer.id}`,
        type: 'registration',
        message: `${farmer.name} registered ${farmer.farm_name}`,
        timestamp: farmer.created_at
      })
    })
  
  // Add some dummy product activities
  if (stats.value.activeFarms > 0) {
    activities.push({
      id: 'prod-1',
      type: 'product',
      message: 'New products added by Green Valley Farm',
      timestamp: new Date().toISOString()
    })
  }
  
  recentActivity.value = activities.sort((a, b) => 
    new Date(b.timestamp) - new Date(a.timestamp)
  ).slice(0, 5)
}

function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

function formatTime(dateString) {
  const date = new Date(dateString)
  const now = new Date()
  const diffMs = now - date
  const diffHours = Math.floor(diffMs / (1000 * 60 * 60))
  
  if (diffHours < 1) {
    const diffMinutes = Math.floor(diffMs / (1000 * 60))
    return `${diffMinutes} minutes ago`
  } else if (diffHours < 24) {
    return `${diffHours} hours ago`
  } else {
    const diffDays = Math.floor(diffHours / 24)
    return `${diffDays} days ago`
  }
}

function navigateToPending() {
  router.push('/admin')
}

function viewAllFarmers() {
  router.push('/admin')
}

function exportData() {
  // Simple CSV export
  const farmers = adminStore.allFarmers
  const csv = [
    ['Farm Name', 'Owner', 'Email', 'Phone', 'Address', 'Status', 'Registered'],
    ...farmers.map(f => [
      f.farm_name,
      f.name,
      f.email,
      f.phone || '',
      f.address || `${f.latitude}, ${f.longitude}`,
      f.is_approved ? 'Approved' : 'Pending',
      formatDate(f.created_at)
    ])
  ].map(row => row.join(',')).join('\n')
  
  const blob = new Blob([csv], { type: 'text/csv' })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `farmers-export-${new Date().toISOString().split('T')[0]}.csv`
  a.click()
  window.URL.revokeObjectURL(url)
}

// Lifecycle
onMounted(() => {
  loadDashboardData()
})
</script>

<style scoped>
.admin-dashboard {
  max-width: 1400px;
  margin: 0 auto;
}

.dashboard-header {
  margin-bottom: 2rem;
}

.dashboard-header h2 {
  color: #333;
  margin-bottom: 0.5rem;
}

.welcome-message {
  color: #666;
  font-size: 1.1rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  gap: 1rem;
  transition: transform 0.2s, box-shadow 0.2s;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-icon.farmers {
  background: #e3f2fd;
  color: #1976d2;
}

.stat-icon.pending {
  background: #fff3e0;
  color: #f57c00;
}

.stat-icon.products {
  background: #e8f5e9;
  color: #388e3c;
}

.stat-icon.active {
  background: #f3e5f5;
  color: #7b1fa2;
}

.stat-content h3 {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 0.25rem;
}

.stat-change {
  font-size: 0.875rem;
}

.stat-change .positive {
  color: #388e3c;
}

.stat-change .warning {
  color: #f57c00;
}

.stat-change .neutral {
  color: #666;
}

/* Activity Section */
.activity-section {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.activity-section h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.activity-list {
  max-height: 300px;
  overflow-y: auto;
}

.activity-item {
  display: flex;
  gap: 1rem;
  padding: 1rem 0;
  border-bottom: 1px solid #eee;
}

.activity-item:last-child {
  border-bottom: none;
}

.activity-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.activity-icon.registration {
  background: #e3f2fd;
  color: #1976d2;
}

.activity-icon.product {
  background: #e8f5e9;
  color: #388e3c;
}

.activity-message {
  color: #333;
  margin-bottom: 0.25rem;
}

.activity-time {
  font-size: 0.875rem;
  color: #666;
}

/* Quick Actions */
.quick-actions {
  margin-bottom: 2rem;
}

.quick-actions h3 {
  margin-bottom: 1rem;
  color: #333;
}

.action-buttons {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.action-btn.pending {
  background: #fff3e0;
  color: #f57c00;
}

.action-btn.pending:hover {
  background: #ffe0b2;
}

.action-btn.export {
  background: #e8f5e9;
  color: #388e3c;
}

.action-btn.export:hover {
  background: #c8e6c9;
}

.action-btn.view {
  background: #e3f2fd;
  color: #1976d2;
}

.action-btn.view:hover {
  background: #bbdefb;
}

/* Farmers Preview */
.farmers-preview {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.section-header h3 {
  color: #333;
}

.view-all-link {
  color: #4CAF50;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}

.view-all-link:hover {
  color: #45a049;
}

.farmers-table {
  width: 100%;
  border-collapse: collapse;
}

.farmers-table th {
  text-align: left;
  padding: 0.75rem;
  border-bottom: 2px solid #eee;
  color: #666;
  font-weight: 600;
  font-size: 0.875rem;
}

.farmers-table td {
  padding: 0.75rem;
  border-bottom: 1px solid #f5f5f5;
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.875rem;
  font-weight: 500;
}

.status-badge.approved {
  background: #e8f5e9;
  color: #388e3c;
}

.status-badge.pending {
  background: #fff3e0;
  color: #f57c00;
}

.loading {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.empty-state {
  text-align: center;
  padding: 3rem;
  color: #999;
}

/* Responsive */
@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .action-buttons {
    grid-template-columns: 1fr;
  }
  
  .farmers-table {
    font-size: 0.875rem;
  }
  
  .farmers-table th,
  .farmers-table td {
    padding: 0.5rem;
  }
}
</style>