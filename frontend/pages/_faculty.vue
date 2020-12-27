<template>
    <section>
        <h1>{{title}}</h1>
        <p v-html="message">no message.</p>
    </section>
</template>

<script>
export default {
    data: function(){
        return {
            title: 'hoge',
        };
    },
    computed: {
        message: function(){
            let faculty = this.$route.params.faculty;
            return faculty + 'のページ';
        },
    },
}
</script>