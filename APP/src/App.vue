<template>

  <div class="flex">
    <Sidebar/>
    <div class="w-full">
      <Header />
      <router-view/>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/modules/sidebar.vue';
import Header from '@/modules/header.vue';

export default {
  name: 'App',
  components : {Sidebar, Header},
  data() {
    return {
      title: 'Medical Chain',
      BASE_URL: process.env.VUE_APP_API
    }
  },
}
</script>

<style>

</style>