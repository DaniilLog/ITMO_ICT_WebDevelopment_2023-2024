<template>
    <div class="new-book_container">
        <h1>New Book</h1>
        <form @submit="addNewBook">
            <label>Book name:</label><br>
            <input v-model="name" type="text" id="name" name="name"><br>

            <label>Author:</label><br>
            <input v-model="author" type="text" id="author" name="author"><br>

            <label>Publisher:</label><br>
            <input v-model="publisher" type="text" id="publisher" name="publisher"><br>

            <label>Publishing year:</label><br>
            <input v-model="publishingYear" type="date" id="publishingYear" name="publishingYear"><br>

            <label>Cipher:</label><br>
            <input v-model="cipher" type="text" id="cipher" name="cipher"><br>

            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import api from '@/services/api';

export default {
    data() {
        return {
            name: '',
            author: '',
            publisher: '',
            publishingYear: '',
            cipher: ''
        }
    },
    methods: {
        addNewBook(event) {
            const userData = {
                name: this.name,
                author: this.author,
                publisher: this.publisher,
                publishing_year: this.publishingYear,
                cipher: this.cipher
            }

            api.post('/books/new', userData)
                .then(response => {
                    localStorage.setItem('formData', JSON.stringify(userData));
                })
                .catch(error => {
                    console.log(userData);
                    console.log(error);
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