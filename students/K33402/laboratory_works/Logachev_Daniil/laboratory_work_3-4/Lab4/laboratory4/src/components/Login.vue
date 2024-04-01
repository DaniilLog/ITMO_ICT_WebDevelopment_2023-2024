<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <label for="username">Username:</label>
        <input v-model="username" type="text" id="username" required>
  
        <label for="password">Password:</label>
        <input v-model="password" type="password" id="password" required>
  
        <button type="submit">Login</button>
      </form>
      <router-link to="/registration" class="link">I don't have an account</router-link>
    </div>
  </template>
  
  <script>
  import api from '@/services/api';

  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },

    methods: {
      login() {
        const credentials = {
          username: this.username,
          password: this.password,
        };
  
        api.post('auth/token', credentials)
          .then(response => {
            const token = response.data.token;
            localStorage.setItem('token', token);
            this.$router.push('/books');
          })
          .catch(error => {
            console.error('Login failed:', error);
          });
      },
    },
  };
  </script>

<style scoped>
  .link {
    color: #fff;
    font-size: 17px;
  }

  form {
    margin-bottom: 20px;
  }
</style>
  