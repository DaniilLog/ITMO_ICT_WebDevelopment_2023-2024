<template>
    <div v-if="assignment">
        <h1>Assignment Details</h1>
        <h3>{{ assignment.copy.book.name }} {{ assignment.copy.book.author }}</h3>
        <h4>Taken by: {{ assignment.reader.name }} {{ assignment.reader.surname }}</h4>
        <p>Assigned: {{ assignment.date_assigned }}</p>
        <p v-if="assignment.date_returned">Returned: {{ assignment.date_returned }}</p>
        <p v-else>not returned yet</p>

        <button><router-link :to="{name: 'EditAssignment', params: { assignmentId: $assignmentId } }">Edit</router-link></button><br><br>

        <router-link to="/assignments">Go back</router-link>
    </div>
    <p v-else>Loading ...</p>
</template>

<script>
import api from '@/services/api'

export default {
    data() {
        return {
            assignment: null,
            assignmentId: null,
        }
    },

    mounted() {
        this.assignmentId = this.$route.params.assignmentId;
        const url = '/assignments/' + this.assignmentId.toString();
        
        api.get(url)
        .then(response => {
            this.assignment = response.data;
        })
        .catch(error => {
            console.error(error);
        })
    }
}
</script>