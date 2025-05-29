import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '../services/api'

export const useProductsStore = defineStore('products', () => {
  const products = ref([])
  const loading = ref(false)
  const error = ref(null)

  async function fetchProducts() {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.getProducts()
      products.value = response.data.products
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to fetch products'
    } finally {
      loading.value = false
    }
  }

  async function createProduct(data) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.createProduct(data)
      products.value.push(response.data.product)
      return response.data.product
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to create product'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function updateProduct(id, data) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.updateProduct(id, data)
      const index = products.value.findIndex(p => p.id === id)
      if (index !== -1) {
        products.value[index] = response.data.product
      }
      return response.data.product
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to update product'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function deleteProduct(id) {
    loading.value = true
    error.value = null
    
    try {
      await api.deleteProduct(id)
      products.value = products.value.filter(p => p.id !== id)
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to delete product'
      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    products,
    loading,
    error,
    fetchProducts,
    createProduct,
    updateProduct,
    deleteProduct
  }
})