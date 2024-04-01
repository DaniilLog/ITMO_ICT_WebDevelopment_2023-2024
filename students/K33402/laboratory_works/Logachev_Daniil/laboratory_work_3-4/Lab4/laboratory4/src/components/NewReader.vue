<template>
    <div class="new-reader_container">
        <h1>New Reader</h1>
        <form @submit="addNewReader">
            <label>Name:</label><br>
            <input v-model="name" type="text" id="name" name="name"><br>

            <label>Second Name:</label><br>
            <input v-model="secondName" type="text" id="second_name" name="second_name"><br>

            <label>Surname:</label><br>
            <input v-model="surname" type="text" id="surname" name="surname"><br>

            <label>Passport:</label><br>
            <input v-model="passport" type="text" id="passport" name="passport"><br>

            <label>Birth date:</label><br>
            <input v-model="birthDate" type="date" id="birth_date" name="birth_date"><br>

            <label>Address:</label><br>
            <input v-model="address" type="text" id="address" name="address"><br>

            <label>Phone number:</label><br>
            <input v-model="phoneNumber" type="text" id="phone_number" name="phone_number"><br>

            <label>Education:</label><br>
            <select v-model="education" id="phone_number">
                <option value="0">Pre-elementary</option>
                <option value="1">Elementary</option>
                <option value="2">Middle</option>
                <option value="3">Secondary</option>
                <option value="4">Professional</option>
                <option value="5">Bachelor</option>
                <option value="6">Master</option>
            </select><br><br>

            <label>Reader has PhD?</label>
            <input v-model="ifPhd" type="checkbox" id="if_phd"><br>

            <label>Hall:</label><br>
            <select v-model="hall" id="hall">
                <option v-for="hall in halls" :key="hall.id" :value="hall.id">{{ hall.name }}</option>
            </select><br><br>

            <label>Card number:</label><br>
            <input v-model="cardNumber" type="text" id="card_number" name="card_number"><br>

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
            secondName: '',
            surname: '',
            passport: '',
            birthDate: '',
            address: '',
            phoneNumber: '',
            education: '0',
            ifPhd: false,
            hall: '',
            cardNumber: '',
            halls: [], 
        }
    },
    methods: {
        addNewReader(event) {
            const userData = {
                name: this.name,
                second_name: this.secondName,
                surname: this.surname,
                passport: this.passport,
                birth_date: this.birthDate,
                address: this.address,
                phone_number: this.phoneNumber,
                education: this.education,
                if_phd: this.ifPhd,
                hall: this.hall,
                library_card_number: this.cardNumber,
            }

            api.post('/readers/new', userData)
            .then(response => {
                localStorage.setItem('formData', JSON.stringify(userData));
            })
            .catch(error => {
                console.error(error);
            })
        }
    },

    mounted () {
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