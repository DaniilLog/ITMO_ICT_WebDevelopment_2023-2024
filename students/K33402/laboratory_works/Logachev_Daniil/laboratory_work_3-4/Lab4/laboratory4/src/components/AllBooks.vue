<template>
    <h1>All Books</h1>
    <hr/>
    <div v-for="book in Books" :key="book.id">
        <h3> {{ book.name }}</h3>
        <h4>{{ book.author }}</h4>
        <br/>
        <p>{{ book.publisher }}, {{ book.publishing_year }}</p>
        <p>cipher: {{ book.cipher }}</p>
        <hr/>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            Books: [],
        }
    },

    mounted () {
        axios.get('http://127.0.0.1:8000/api/books/all')
                .then(response => {
                    this.Books = response.data;
                })
                .catch(error => {
                    console.log('Something went wrong :(')
                })
    }
}
</script>