<template>
    <div class="new-copy_container">
        <h1>New Copy</h1>
        <form @submit="addNewCopy">

            <label>Book:</label><br>
            <select v-model="book" id="book">
                <option v-for="book in books" :key="book.id" :value="book.id">{{ book.name }} {{ book.author }}</option>
            </select><br><br>

            <label>Hall:</label><br>
            <select v-model="hall" id="hall">
                <option v-for="hall in halls" :key="hall.id" :value="hall.id">{{ hall.sequence_number }}. {{ hall.name }}</option>
            </select><br><br>

            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import api from '@/services/api';

export default {
    data() {
        return {
            books: [],
            halls: [], 
            book: null,
            hall: null,
        }
    },
    methods: {
        addNewCopy(event) {
            const userData = {
                hall: this.hall,
                book: this.book,
            }

            api.post('/copys/new', userData)
            .then(response => {
                localStorage.setItem('formData', JSON.stringify(userData));
            })
            .catch(error => {
                console.error(error);
            })
        }
    },

    mounted () {
        api.get('/books/all')
        .then(response => {
            this.books = response.data;
        })
        .catch(error => {
            console.error(error);
        })

        api.get('/halls/all')
        .then(response => {
            this.halls = response.data;
        })
        .catch(error => {
            console.error(error);
        })
    }
}
</script>

<style scoped>
    input {
        margin-bottom: 20px;
    }
</style>