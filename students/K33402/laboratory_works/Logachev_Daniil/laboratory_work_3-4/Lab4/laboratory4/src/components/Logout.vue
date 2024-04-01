<template>
    <h2>{{ username }}, are you sure you want to logout?</h2>
    <button @click="logout">Yes</button>
</template>

<script>
import api from '../services/api';
import router from '../router';

export default {
        data() {
            return {
                username: ''
            };
        },

        mounted() {
            const token = localStorage.getItem('token');
            if (!token) {
                router.push('/login');
                return;
            }
            console.log(token);
            api.get('auth/users/me/', {
                headers: {
                    Authorization: `Token ${token}`
                }
            })
            .then(response => {
                this.username = response.data.username;
                this.username = this.username.charAt(0).toUpperCase() + this.username.slice(1);
            })
            .catch(error => {
                console.error(error);
            })
        },

        methods: {
            logout() {
                localStorage.removeItem('token');
                this.$router.push('/login');
            }
        }
    }
</script>
