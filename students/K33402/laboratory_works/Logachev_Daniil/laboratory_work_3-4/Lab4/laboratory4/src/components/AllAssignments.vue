<template>
    <h1>All Assignments</h1>
    <hr/>
    <div v-for="assignment in Assignments" :key="assignment.id">
        <h3> {{ assignment.copy.book.name }}</h3>
        <h4>{{ assignment.reader.surname }} {{ assignment.reader.name }}</h4>
        <br/>
        <button @click="pushRouter(assignment.id)">Full assignemnt information</button>
        <hr/>
    </div>
</template>

<script>
import api from '@/services/api'
import router from '@/router'

export default {
    data() {
        return {
            Assignments: [],
        }
    },

    methods: {
        pushRouter(id) {
            const url = '/assignments/' + id.toString();
            router.push(url);
        }
    },

    mounted () {
        api.get('/assignments/all')
                .then(response => {
                    this.Assignments = response.data;
                })
                .catch(error => {
                    console.error(error);
                })
    }
}
</script>