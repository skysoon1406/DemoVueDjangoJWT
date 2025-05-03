<template>
    <h1>保護列表</h1>
    <button @click="getList">取得資料</button>
    <ul>
      <li v-for="item in list" :key="item">{{ item }}</li>
    </ul>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const list = ref([])
  
  async function getList() {
    const token = localStorage.getItem('access_token')
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/list/', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      list.value = res.data.items
    } catch (err) {
      alert('取得失敗：' + err.response?.data?.detail || err.message)
    }
  }
  </script>
  