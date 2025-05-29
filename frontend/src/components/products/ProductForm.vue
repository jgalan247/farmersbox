<template>
  <form @submit.prevent="handleSubmit" class="product-form">
    <h3>Add New Product</h3>
    
    <div class="form-group">
      <label class="form-label">Product Name</label>
      <input 
        v-model="form.name" 
        type="text" 
        class="form-control" 
        required
      />
    </div>
    
    <div class="form-group">
      <label class="form-label">Description</label>
      <textarea 
        v-model="form.description" 
        class="form-control" 
        rows="3"
      ></textarea>
    </div>
    
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Price</label>
        <input 
          v-model.number="form.price" 
          type="number" 
          step="0.01"
          class="form-control" 
          required
        />
      </div>
      
      <div class="form-group">
        <label class="form-label">Unit</label>
        <select v-model="form.unit" class="form-control" required>
          <option value="">Select unit</option>
          <option value="kg">Kilogram (kg)</option>
          <option value="g">Gram (g)</option>
          <option value="lb">Pound (lb)</option>
          <option value="piece">Piece</option>
          <option value="dozen">Dozen</option>
          <option value="bunch">Bunch</option>
          <option value="box">Box</option>
          <option value="bag">Bag</option>
        </select>
      </div>
      
      <div class="form-group">
        <label class="form-label">Quantity Available</label>
        <input 
          v-model.number="form.quantity_available" 
          type="number" 
          step="0.01"
          class="form-control" 
          required
        />
      </div>
    </div>
    
    <div class="form-group">
      <label class="checkbox-label">
        <input 
          v-model="form.is_available" 
          type="checkbox"
        />
        Currently available
      </label>
    </div>
    
    <button type="submit" class="btn" :disabled="loading">
      {{ loading ? 'Adding...' : 'Add Product' }}
    </button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useProductsStore } from '../../stores/products'

const productsStore = useProductsStore()
const loading = ref(false)

const form = ref({
  name: '',
  description: '',
  price: 0,
  unit: '',
  quantity_available: 0,
  is_available: true
})

async function handleSubmit() {
  loading.value = true
  
  try {
    await productsStore.createProduct(form.value)
    // Reset form
    form.value = {
      name: '',
      description: '',
      price: 0,
      unit: '',
      quantity_available: 0,
      is_available: true
    }
  } catch (err) {
    console.error('Failed to create product:', err)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.product-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.product-form h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.checkbox-label input {
  width: auto;
}

@media (max-width: 768px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}
</style>