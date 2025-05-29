<template>
  <nav class="navbar" :class="{ 'scrolled': isScrolled }">
    <div class="navbar-container">
      <!-- Logo -->
      <router-link to="/" class="navbar-brand">
        <img v-if="logoUrl" :src="logoUrl" alt="HonestyBox" class="logo-img">
        <span class="logo-text">HonestyBox</span>
      </router-link>

      <!-- Mobile menu toggle -->
      <button 
        @click="toggleMobileMenu" 
        class="mobile-menu-toggle"
        :aria-expanded="isMobileMenuOpen"
        aria-label="Toggle navigation menu"
      >
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
      </button>

      <!-- Navigation links -->
      <div class="navbar-menu" :class="{ 'active': isMobileMenuOpen }">
        <div class="navbar-nav">
          <!-- Public links -->
          <router-link 
            to="/" 
            class="nav-link"
            @click="closeMobileMenu"
          >
            Home
          </router-link>
          
          <router-link 
            to="/map" 
            class="nav-link"
            @click="closeMobileMenu"
          >
            <svg class="nav-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
              <circle cx="12" cy="10" r="3"></circle>
            </svg>
            Farm Map
          </router-link>

          <!-- Authenticated farmer links -->
          <template v-if="authStore.isAuthenticated && authStore.isFarmer">
            <router-link 
              to="/dashboard" 
              class="nav-link"
              @click="closeMobileMenu"
            >
              Dashboard
            </router-link>
            
            <router-link 
              to="/products" 
              class="nav-link"
              @click="closeMobileMenu"
            >
              Products
            </router-link>
          </template>

          <!-- Admin links -->
          <router-link 
            v-if="authStore.isAdmin" 
            to="/admin" 
            class="nav-link admin-link"
            @click="closeMobileMenu"
          >
            <svg class="nav-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
            </svg>
            Admin Panel
          </router-link>
        </div>

        <!-- Auth section -->
        <div class="navbar-auth">
          <template v-if="!authStore.isAuthenticated">
            <router-link 
              to="/login" 
              class="nav-link"
              @click="closeMobileMenu"
            >
              Login
            </router-link>
            
            <router-link 
              to="/register" 
              class="btn btn-primary btn-small"
              @click="closeMobileMenu"
            >
              Register Farm
            </router-link>
          </template>
          
          <template v-else>
            <!-- User dropdown -->
            <div class="user-dropdown" ref="dropdownRef">
              <button 
                @click="toggleDropdown" 
                class="user-dropdown-toggle"
                :aria-expanded="isDropdownOpen"
              >
                <div class="user-avatar">
                  {{ userInitials }}
                </div>
                <span class="user-name">{{ authStore.user?.name }}</span>
                <svg class="dropdown-arrow" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
              </button>
              
              <div v-if="isDropdownOpen" class="dropdown-menu">
                <div class="dropdown-header">
                  <p class="dropdown-user-name">{{ authStore.user?.name }}</p>
                  <p class="dropdown-user-email">{{ authStore.user?.email }}</p>
                  <span class="dropdown-user-role" :class="authStore.user?.role">
                    {{ authStore.user?.role === 'super_admin' ? 'Administrator' : 'Farmer' }}
                  </span>
                </div>
                
                <div class="dropdown-divider"></div>
                
                <router-link 
                  v-if="authStore.isFarmer"
                  to="/dashboard" 
                  class="dropdown-item"
                  @click="closeDropdown"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                  </svg>
                  Dashboard
                </router-link>
                
                <router-link 
                  v-if="authStore.isFarmer"
                  to="/profile" 
                  class="dropdown-item"
                  @click="closeDropdown"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  Profile Settings
                </router-link>
                
                <div class="dropdown-divider"></div>
                
                <button @click="handleLogout" class="dropdown-item logout">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                    <polyline points="16 17 21 12 16 7"></polyline>
                    <line x1="21" y1="12" x2="9" y2="12"></line>
                  </svg>
                  Logout
                </button>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'

// Props
const props = defineProps({
  logoUrl: {
    type: String,
    default: ''
  }
})

// Stores and Router
const authStore = useAuthStore()
const router = useRouter()

// State
const isMobileMenuOpen = ref(false)
const isDropdownOpen = ref(false)
const isScrolled = ref(false)
const dropdownRef = ref(null)

// Computed
const userInitials = computed(() => {
  if (!authStore.user?.name) return '?'
  return authStore.user.name
    .split(' ')
    .map(word => word[0])
    .join('')
    .toUpperCase()
    .slice(0, 2)
})

// Methods
function toggleMobileMenu() {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
  if (isMobileMenuOpen.value) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
}

function closeMobileMenu() {
  isMobileMenuOpen.value = false
  document.body.style.overflow = ''
}

function toggleDropdown() {
  isDropdownOpen.value = !isDropdownOpen.value
}

function closeDropdown() {
  isDropdownOpen.value = false
}

async function handleLogout() {
  closeDropdown()
  closeMobileMenu()
  await authStore.logout()
  router.push('/')
}

function handleScroll() {
  isScrolled.value = window.scrollY > 10
}

function handleClickOutside(event) {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    closeDropdown()
  }
}

// Lifecycle
onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  document.removeEventListener('click', handleClickOutside)
  document.body.style.overflow = ''
})
</script>

<style scoped>
.navbar {
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
  transition: all 0.3s ease;
}

.navbar.scrolled {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 64px;
}

/* Logo */
.navbar-brand {
  display: flex;
  align-items: center;
  text-decoration: none;
  gap: 0.5rem;
}

.logo-img {
  height: 32px;
  width: auto;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: bold;
  color: #4CAF50;
}

/* Mobile menu toggle */
.mobile-menu-toggle {
  display: none;
  flex-direction: column;
  justify-content: space-around;
  width: 30px;
  height: 24px;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
}

.hamburger-line {
  width: 100%;
  height: 3px;
  background-color: #333;
  transition: all 0.3s ease;
}

/* Navigation menu */
.navbar-menu {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.navbar-nav {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.nav-link {
  color: #333;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.nav-link:hover {
  color: #4CAF50;
}

.nav-link.router-link-active {
  color: #4CAF50;
}

.nav-icon {
  width: 16px;
  height: 16px;
}

.admin-link {
  color: #f57c00;
}

.admin-link:hover {
  color: #e65100;
}

/* Auth section */
.navbar-auth {
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* User dropdown */
.user-dropdown {
  position: relative;
}

.user-dropdown-toggle {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
  background: transparent;
  border: none;
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s ease;
}

.user-dropdown-toggle:hover {
  background-color: #f5f5f5;
}

.user-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: #4CAF50;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
}

.user-name {
  font-weight: 500;
  color: #333;
}

.dropdown-arrow {
  transition: transform 0.3s ease;
}

.user-dropdown-toggle[aria-expanded="true"] .dropdown-arrow {
  transform: rotate(180deg);
}

/* Dropdown menu */
.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 0.5rem;
  min-width: 240px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  animation: dropdownFadeIn 0.2s ease;
}

@keyframes dropdownFadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.dropdown-header {
  padding: 1rem;
  background-color: #f8f9fa;
}

.dropdown-user-name {
  font-weight: 600;
  color: #333;
  margin-bottom: 0.25rem;
}

.dropdown-user-email {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.dropdown-user-role {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 500;
}

.dropdown-user-role.farmer {
  background-color: #e8f5e9;
  color: #388e3c;
}

.dropdown-user-role.super_admin {
  background-color: #fff3e0;
  color: #f57c00;
}

.dropdown-divider {
  height: 1px;
  background-color: #eee;
  margin: 0;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  color: #333;
  text-decoration: none;
  transition: background-color 0.2s ease;
  border: none;
  background: none;
  width: 100%;
  text-align: left;
  cursor: pointer;
  font-size: 0.875rem;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}

.dropdown-item.logout {
  color: #dc3545;
}

.dropdown-item.logout:hover {
  background-color: #fee;
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
}

.btn-primary {
  background-color: #4CAF50;
  color: white;
}

.btn-primary:hover {
  background-color: #45a049;
}

.btn-small {
  padding: 0.375rem 0.875rem;
  font-size: 0.875rem;
}

/* Mobile styles */
@media (max-width: 768px) {
  .mobile-menu-toggle {
    display: flex;
  }

  .navbar-menu {
    position: fixed;
    top: 64px;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: white;
    flex-direction: column;
    padding: 2rem;
    gap: 2rem;
    transform: translateX(100%);
    transition: transform 0.3s ease;
  }

  .navbar-menu.active {
    transform: translateX(0);
  }

  .navbar-nav {
    flex-direction: column;
    gap: 1rem;
    width: 100%;
  }

  .nav-link {
    padding: 0.75rem 0;
    width: 100%;
    border-bottom: 1px solid #eee;
  }

  .navbar-auth {
    flex-direction: column;
    width: 100%;
    gap: 1rem;
  }

  .user-dropdown {
    width: 100%;
  }

  .user-dropdown-toggle {
    width: 100%;
    justify-content: space-between;
    padding: 0.75rem;
    background-color: #f8f9fa;
  }

  .dropdown-menu {
    position: static;
    box-shadow: none;
    margin-top: 1rem;
  }
}
</style>