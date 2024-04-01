<template>
    <h1>All Halls</h1>
    <hr/>
    <div v-for="hall in Halls" :key="hall.id">
        <h3> {{ hall.sequence_number }}. {{ hall.name }}</h3>
        <p>Capacity: {{ hall.capacity }}</p>
        <hr/>
    </div>
</template>

<script>
import api from '@/services/api'

export default {
    data() {
        return {
            Halls: [],
        }
    },

    mounted () {
        api.get('/halls/all')
                .then(response => {
                    this.Halls = response.data;
                })
                .catch(error => {
                    console.error(error);
                })
    }
}
</script>