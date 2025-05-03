<template>
    <h1>登入頁面</h1>
    <input v-model="username" placeholder="帳號" />
    <input v-model="password" type="password" placeholder="密碼" />
    <button @click="login">登入</button>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const username = ref('')
  const password = ref('')
  
  async function login() {
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/token/', {
        username: username.value,
        password: password.value
      })
      localStorage.setItem('access_token', res.data.access)
      localStorage.setItem('refresh_token', res.data.refresh)
      alert('登入成功！')
      window.location.reload()

    } catch (err) {
      alert('登入失敗：' + err.response?.data?.detail || err.message)
    }
  }
  </script>
  