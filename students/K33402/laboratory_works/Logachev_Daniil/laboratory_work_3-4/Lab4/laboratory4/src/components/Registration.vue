<template>
    <div class="registraton_container">
        <h1>Registration</h1>
        <form @submit="register">
            <label for="email">Email:</label><br>
            <input v-model="email" type="text" id="email" name="email"><br>
            <label for="username">Username:</label><br>
            <input  v-model="username" type="text" id="username" name="username"><br>
            <label for="password">Password:</label><br>
            <input  v-model="password" type="text" id="password" name="password"><br>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            username: '',
            password: ''
        }
    },
    methods: {
        register(event) {
            event.preventDefault();
            const userData = {
                email: this.email,
                username: this.username,
                password: this.password
            }

            axios.post('http://127.0.0.1:8000/api/auth/users/', userData)
                .then(response => {
                    localStorage.setItem('userData', JSON.stringify(formData));
                })
                .catch(error => {
                    // console.log(userData);
                    // console.log(error);
                    console.log('Something went wrong :(')
                })
        }
    }
}
</script>


<style scoped>
    input {
        margin-bottom: 20px;
    }
</style>