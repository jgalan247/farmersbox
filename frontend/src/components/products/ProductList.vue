<template>
  <div class="products-list">
    <div v-if="productsStore.loading" class="loading">Loading products...</div>
    
    <div v-else-if="productsStore.error" class="alert alert-error">
      {{ productsStore.error }}
    </div>
    
    <div v-else-if="productsStore.products.length === 0" class="empty-state">
      <p>No products yet. Add your first product!</p>
    </div>
    
    <table v-else class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Price</th>
          <th>Unit</th>
          <th>Quantity</th>
          <th>Available</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in productsStore.products" :key="product.id">
          <td>
            <input 
              v-if="editingId === product.id" 
              v-model="editForm.name"
              class="edit-input"
            />
            <span v-else>{{ product.name }}</span>
          </td>
          <td>
            <input 
              v-if="editingId === product.id" 
              v-model="editForm.description"
              class="edit-input"
            />
            <span v-else>{{ product.description || '-' }}</span>
          </td>
          <td>
            <input 
              v-if="editingId === product.id" 
              v-model.number="editForm.price"
              type="number"
              step="0.01"
              class="edit-input"
            />
            <span v-else>${{ product.price.toFixed(2) }}</span>
          </td>
          <td>
            <input 
              v-if="editingId === product.id" 
              v-model="editForm.unit"
              class="edit-input"
            />
            <span v-else>{{ product.unit }}</span>
          </td>
          <td>
            <input 
              v-if="editingId === product.id" 
              v-model.number="editForm.quantity_available"
              type="number"
              step="0.01"
              class="edit-input"
            />
            <span v-else>{{ product.quantity_available }}</span>
          </td>
          <td>
            <input 
              v-if="editingId === product.id" 
              v-model="editForm.is_available"
              type="checkbox"
            />
            <span v-else>{{ product.is_available ? 'Yes' : 'No' }}</span>
          </td>
          <td>
            <div class="actions">
              <template v-if="editingId === product.id">
                <button @click="saveEdit" class="btn btn-small">Save</button>
                <button @click="cancelEdit" class="btn btn-secondary btn-small">Cancel</button>
              </template>
              <template v-else>
                <button @click="startEdit(product)" class="btn btn-small">Edit</button>
                <button @click="confirmDelete(product)" class="btn btn-danger btn-small">Delete</button>
              </template>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useProductsStore } from '../../stores/products'

const productsStore = useProductsStore()
const editingId = ref(null)
const editForm = ref({})

function startEdit(product) {
  editingId.value = product.id
  editForm.value = { ...product }
}

function cancelEdit() {
  editingId.value = null
  editForm.value = {}
}

async function saveEdit() {
  try {
    await productsStore.updateProduct(editingId.value, editForm.value)
    editingId.value = null
    editForm.value = {}
  } catch (err) {
    console.error('Failed to save:', err)
  }
}

async function confirmDelete(product) {
  if (confirm(`Are you sure you want to delete "${product.name}"?`)) {
    try {
      await productsStore.deleteProduct(product.id)
    } catch (err) {
      console.error('Failed to delete:', err)
    }
  }
}
</script>

<style scoped>
.empty-state {
  text-align: center;
  padding: 3rem;
  color: #666;
}

.edit-input {
  width: 100%;
}
</style>
