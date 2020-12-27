<template>
    <section class="conatiner">
        <h1>{{title}}</h1>
        <p>{{message}}</p>
        <pre>{{html_data}}</pre>
    </section>
</template>

<script>
const axios = require('axios');

// let url = '/README.md';
// let url = 'http://localhost:8000'
let url = process.env.BACKEND_URL

export default {
    data: function(){
        return {
            title: 'Axios',
            message: 'axios sample.',
        };
    },
    asyncData: async function(){
        let result = await axios.get(url);
        return {html_data: result.data.text};
    },
}
</script>

<style>

</style>