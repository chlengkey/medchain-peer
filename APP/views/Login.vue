<template>
    <form @Masuk.prevent="handleMasuk">
        <label>Email:</label>
        <input type="email" required v-model="email">

        <label>Password:</label>
        <input type="password" required v-model="password">
        <div v-if="passwordError" class="error">{{ passwordError }}</div>

        <div class="Masuk">
            <button>Masuk</button>
        </div>
    </form>
</template>

<script>

export default {
    data() {
        return {
            email: '',
            password: '',
            passwordError: ''
        }
    },
    methods: {
        handleMasuk() {
            this.passwordError = this.password.length > 5 ? '' : 'Password min.8 karakter'
        }
    }
}
</script>

<style>
    form {
        max-width: 420px;
        margin: 30px auto;
        background: white;
        text-align: left;
        padding: 40px;
        border-radius: 10px;
    }
    label{
        color: #aaa;
        display: inline-block;
        margin: 25px 0 15px;
        font-size: 0.6em;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }
    input{
        display: block;
        padding: 10px 6px;
        width: 100%;
        box-sizing: border-box;
        border: none;
        border-bottom: 1px solid #ddd;
        color: #555;
    }
    button {
        background: orangered;
        border: 0;
        padding: 10px 20px;
        margin-top: 20px;
        color: white;
        border-radius: 10px;
    }
</style>
