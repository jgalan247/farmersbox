import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '../services/api'

export const useAdminStore = defineStore('admin', () => {
  const pendingFarmers = ref([])
  const allFarmers = ref([])
  const loading = ref(false)
  const error = ref(null)

  async function fetchPendingFarmers() {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.getPendingFarmers()
      pendingFarmers.value = response.data.farmers
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to fetch pending farmers'
    } finally {
      loading.value = false
    }
  }

  async function fetchAllFarmers() {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.getAllFarmers()
      allFarmers.value = response.data.farmers
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to fetch farmers'
    } finally {
      loading.value = false
    }
  }

  async function approveFarmer(id) {
    loading.value = true
    error.value = null
    
    try {
      await api.approveFarmer(id)
      pendingFarmers.value = pendingFarmers.value.filter(f => f.id !== id)
      await fetchAllFarmers()
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to approve farmer'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function rejectFarmer(id) {
    loading.value = true
    error.value = null
    
    try {
      await api.rejectFarmer(id)
      pendingFarmers.value = pendingFarmers.value.filter(f => f.id !== id)
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to reject farmer'
      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    pendingFarmers,
    allFarmers,
    loading,
    error,
    fetchPendingFarmers,
    fetchAllFarmers,
    approveFarmer,
    rejectFarmer
  }
})