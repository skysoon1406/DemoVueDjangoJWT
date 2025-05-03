<template>
    <div>
      <h1>我的專案</h1>
      <nav>
        <router-link to="/">首頁</router-link> |
        <router-link to="/register">註冊</router-link> |
        <router-link to="/login">登入</router-link> |
        <router-link to="/list">保護列表</router-link>
      </nav>
  
      <div v-if="userInfo">
        <p>{{ userInfo.username }}，已登入</p>
        <button @click="logout">登出</button>
      </div>
      <div v-else>
        <p>未登入</p>
      </div>
  
      <router-view />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const userInfo = ref(null)
  const token = ref(localStorage.getItem('access_token') || '')
  
  async function getUserInfo() {
      if (!token.value) {
          userInfo.value = null
          return
      }
      try {
          const res = await axios.get('http://127.0.0.1:8000/api/userinfo/', {
              headers: {
                  Authorization: `Bearer ${token.value}`
              }
          })
          userInfo.value = res.data
      } catch (err) {
          userInfo.value = null
      }
  }
  
  function logout() {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      token.value = ''
      userInfo.value = null
      alert('已登出')
  }
  
  onMounted(() => {
      getUserInfo()
  })
  </script>
  
  <style>
  nav a {
    margin: 0 10px;
  }
  </style>
  
  


<!-- <template>
  <h1>Vue + Django JWT Demo</h1>

  <div v-if="userInfo">
    <p>{{ userInfo.username }}，已登入</p>
    <button @click="logout">登出</button>
  </div>
  <div v-else>
    <p>未登入</p>
  </div>

  <h2>註冊</h2>
  <input v-model="registerUsername" placeholder="New Username" />
  <input v-model="registerPassword" type="password" placeholder="New Password" />
  <button @click="register">註冊</button>

  <h2>登入</h2>
  <input v-model="username" placeholder="Username" />
  <input v-model="password" type="password" placeholder="Password" />
  <button @click="login">登入</button>

  <h2>Protected List (需要登入)</h2>
  <button @click="getList">取得列表</button>
  <ul>
    <li v-for="item in list" :key="item">{{ item }}</li>
  </ul>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')
const registerUsername = ref('')
const registerPassword = ref('')
const list = ref([])
const userInfo = ref(null)
const token = ref(localStorage.getItem('access_token') || '')

// 註冊
async function register() {
    try {
        await axios.post('http://127.0.0.1:8000/api/register/', {
            username: registerUsername.value,
            password: registerPassword.value
        })
        alert('註冊成功！請登入。')
    } catch (err) {
        alert('註冊失敗：' + err.response.data.error)
    }
}

// 登入
async function login() {
    try {
        const res = await axios.post('http://127.0.0.1:8000/api/token/', {
            username: username.value,
            password: password.value
        })
        token.value = res.data.access
        localStorage.setItem('access_token', res.data.access)
        localStorage.setItem('refresh_token', res.data.refresh)
        alert('登入成功！')
        await getUserInfo()
    } catch (err) {
        alert('登入失敗：' + err.response.data.detail)
    }
}

// 登出
function logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    token.value = ''
    userInfo.value = null
    list.value = []
    alert('已登出')
}

// 取得保護資料
async function getList() {
    if (!token.value) {
        alert('請先登入。')
        return
    }
    try {
        const res = await axios.get('http://127.0.0.1:8000/api/list/', {
            headers: {
                Authorization: `Bearer ${token.value}`
            }
        })
        list.value = res.data.items
    } catch (err) {
        if (err.response && err.response.status === 401) {
            alert('未授權，請重新登入。')
        } else {
            alert('發生錯誤。')
        }
    }
}

// 顯示登入狀態
async function getUserInfo() {
    if (!token.value) {
        userInfo.value = null
        return
    }
    try {
        const res = await axios.get('http://127.0.0.1:8000/api/userinfo/', {
            headers: {
                Authorization: `Bearer ${token.value}`
            }
        })
        userInfo.value = res.data
    } catch (err) {
        userInfo.value = null
    }
}

// 畫面一進來時就檢查一次
onMounted(() => {
    getUserInfo()
})
</script> -->
