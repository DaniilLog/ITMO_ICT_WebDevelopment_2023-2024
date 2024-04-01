<template>
    <h1>All Copies</h1>
    <hr/>
    <div v-for="copy in Copies" :key="copy.id">
        <p>Book: <strong>{{ copy.book.name }} {{ copy.book.author }}</strong></p>
        <p>Hall: <strong>{{ copy.hall.name }}</strong></p>
        <hr/>
    </div>
</template>

<script>
import api from '@/services/api'

export default {
    data () {
        return {
            Copies: []
        }
    },

    mounted () {
        api.get('/copys/all')
        .then(response => {
            this.Copies = response.data;
        })
        .catch (error => {
            console.error(error);
        })
    }
}
</script>
