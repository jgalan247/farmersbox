import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '../services/api'
import router from '../router'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))
  const loading = ref(false)
  const error = ref(null)

  const isAuthenticated = computed(() => !!token.value)
  const isFarmer = computed(() => user.value?.role === 'farmer')
  const isAdmin = computed(() => user.value?.role === 'super_admin')
  const isApproved = computed(() => user.value?.is_approved)

  async function login(credentials) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.login(credentials)
      token.value = response.data.access_token
      user.value = response.data.user
      localStorage.setItem('token', token.value)
      
      if (isAdmin.value) {
        router.push('/admin')
      } else {
        router.push('/dashboard')
      }
    } catch (err) {
      error.value = err.response?.data?.error || 'Login failed'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function register(data) {
    loading.value = true
    error.value = null
    
    try {
      await api.register(data)
      router.push('/login')
    } catch (err) {
      error.value = err.response?.data?.error || 'Registration failed'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function logout() {
    user.value = null
    token.value = null
    localStorage.removeItem('token')
    router.push('/')
  }

  async function checkAuth() {
    if (!token.value) return
    
    try {
      const response = await api.getMe()
      user.value = response.data.user
    } catch (err) {
      logout()
    }
  }

  return {
    user,
    token,
    loading,
    error,
    isAuthenticated,
    isFarmer,
    isAdmin,
    isApproved,
    login,
    register,
    logout,
    checkAuth
  }
})