<template>
    <h1>註冊頁面</h1>
    <input v-model="username" placeholder="新帳號" />
    <input v-model="password" type="password" placeholder="新密碼" />
    <button @click="register">註冊</button>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const username = ref('')
  const password = ref('')
  
  async function register() {
    try {
      await axios.post('http://127.0.0.1:8000/api/register/', {
        username: username.value,
        password: password.value
      })
      alert('註冊成功！請去登入頁面。')
    } catch (err) {
      alert('註冊失敗：' + err.response?.data?.error || err.message)
    }
  }
  </script>
  