<template>
  <AppLayout>
    <div class="auth-container">
      <form @submit.prevent="handleLogin" class="auth-form">
        <h2>Login to HonestyBox</h2>
        
        <div v-if="authStore.error" class="alert alert-error">
          {{ authStore.error }}
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
          />
        </div>
        
        <button type="submit" class="btn btn-block" :disabled="authStore.loading">
          {{ authStore.loading ? 'Logging in...' : 'Login' }}
        </button>
        
        <p class="auth-link">
          Don't have an account? 
          <router-link to="/register">Register here</router-link>
        </p>
        
        <div class="admin-note">
          <p><strong>Admin Login:</strong></p>
          <p>Email: admin@honestybox.com</p>
          <p>Password: admin123</p>
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
  email: '',
  password: ''
})

async function handleLogin() {
  try {
    await authStore.login(form.value)
  } catch (err) {
    console.error('Login failed:', err)
  }
}
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 70vh;
}

.auth-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
}

.auth-form h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #333;
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

.admin-note {
  margin-top: 2rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 4px;
  font-size: 0.9rem;
}

.admin-note p {
  margin: 0.25rem 0;
  color: #666;
}
</style>
