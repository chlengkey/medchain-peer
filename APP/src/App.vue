<template>

  <div class="flex">
    <Sidebar/>
    URL : {{BASE_URL}}
    <router-view/>
  </div>
</template>

<script>
import Sidebar from '@/modules/sidebar.vue';
export default {
  name: 'App',
  components : {Sidebar},
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