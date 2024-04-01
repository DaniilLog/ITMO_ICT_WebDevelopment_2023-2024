<template>
    <div class="new-hall_container">
        <h1>New Hall</h1>
        <form @submit="addNewHall">
            <label>Hall name:</label><br>
            <input v-model="name" type="text" id="name"><br>

            <label>Sequence number:</label><br>
            <input v-model="sequenceNumber" type="number" id="sequenceNumber"><br>

            <label>Capacity:</label><br>
            <input v-model="capacity" type="number" id="capacity"><br>

            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import api from '@/services/api';

export default {
    data() {
        return {
            name: null,
            sequenceNumber: null,
            capacity: null
        }
    },
    methods: {
        addNewHall(event) {
            const userData = {
                name: this.name,
                sequence_number: this.sequenceNumber,
                capacity: this.capacity
            }

            api.post('/halls/new', userData)
                .then(response => {
                    localStorage.setItem('formData', JSON.stringify(userData));
                })
                .catch(error => {
                    console.error(error);
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