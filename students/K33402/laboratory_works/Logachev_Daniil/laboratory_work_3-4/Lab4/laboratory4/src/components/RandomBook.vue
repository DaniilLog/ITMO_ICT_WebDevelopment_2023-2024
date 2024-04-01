<template>
    <h1>{{ book.name }}</h1>
    <h2>{{ book.author }}</h2>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            book: ''
        }
    },

    mounted() {
        let books = '';
        axios.get('http://127.0.0.1:8000/api/books/all')
                .then(response => {
                    const books = response.data
                    const amount = response.data.length;
                    const number = Math.floor(Math.random() * amount);
                    this.book = books[number];
                })
                .catch(error => {
                    console.log('Something went wrong :(')
                })
    
    }
}
</script>