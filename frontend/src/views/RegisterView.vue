<template>
  <AppLayout>
    <div class="auth-container">
      <form @submit.prevent="handleRegister" class="auth-form">
        <h2>Register Your Farm</h2>
        
        <div v-if="authStore.error" class="alert alert-error">
          {{ authStore.error }}
        </div>
        
        <div class="form-group">
          <label class="form-label">Your Name</label>
          <input 
            v-model="form.name" 
            type="text" 
            class="form-control" 
            required
          />
        </div>
        
        <div class="form-group">
          <label class="form-label">Email</label>
          <input 
            v-model="form.email" 
            type="email" 
            class="form-control" 
            required
          />
        </div>
        
        <div class="form-group">
          <label class="form-label">Password</label>
          <input 
            v-model="form.password" 
            type="password" 
            class="form-control" 
            required
            minlength="6"
          />
        </div>
        
        <div class="form-group">
          <label class="form-label">Farm Name</label>
          <input 
            v-model="form.farm_name" 
            type="text" 
            class="form-control" 
            required
          />
        </div>
        
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">Latitude</label>
            <input 
              v-model.number="form.latitude" 
              type="number" 
              step="0.000001"
              class="form-control" 
              required
              placeholder="e.g., 40.7128"
            />
          </div>
          
          <div class="form-group">
            <label class="form-label">Longitude</label>
            <input 
              v-model.number="form.longitude" 
              type="number" 
              step="0.000001"
              class="form-control" 
              required
              placeholder="e.g., -74.0060"
            />
          </div>
        </div>
        
        <div class="form-group">
          <label class="form-label">Phone (Optional)</label>
          <input 
            v-model="form.phone" 
            type="tel" 
            class="form-control"
          />
        </div>
        
        <div class="form-group">
          <label class="form-label">Address (Optional)</label>
          <textarea 
            v-model="form.address" 
            class="form-control" 
            rows="3"
          ></textarea>
        </div>
        
        <button type="submit" class="btn btn-block" :disabled="authStore.loading">
          {{ authStore.loading ? 'Registering...' : 'Register Farm' }}
        </button>
        
        <p class="auth-link">
          Already have an account? 
          <router-link to="/login">Login here</router-link>
        </p>
        
        <div class="info-note">
          <p><strong>Note:</strong> Your registration will be reviewed by our admin team before your farm becomes visible to customers.</p>
        </div>
      </form>
    </div>
  </AppLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import AppLayout from '../components/layout/AppLayout.vue'

const authStore = useAuthStore()

const form = ref({
  name: '',
  email: '',
  password: '',
  farm_name: '',
  latitude: null,
  longitude: null,
  phone: '',
  address: ''
})

async function handleRegister() {
  try {
    await authStore.register(form.value)
    alert('Registration successful! Please wait for admin approval.')
  } catch (err) {
    console.error('Registration failed:', err)
  }
}
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem 0;
}

.auth-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 500px;
}

.auth-form h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #333;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.btn-block {
  width: 100%;
}

.auth-link {
  text-align: center;
  margin-top: 1rem;
  color: #666;
}

.auth-link a {
  color: #4CAF50;
  text-decoration: none;
}

.auth-link a:hover {
  text-decoration: underline;
}

.info-note {
  margin-top: 1.5rem;
  padding: 1rem;
  background: #e8f5e9;
  border-radius: 4px;
  font-size: 0.9rem;
}

.info-note p {
  margin: 0;
  color: #2e7d32;
}
</style>