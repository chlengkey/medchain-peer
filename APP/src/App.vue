<template>
  <div class="flex">
    <Sidebar/>
    <router-view/>
  </div>
</template>

<style>


</style>

<script type="text/javascript">
  import Sidebar from '@/modules/sidebar.vue'
  export default{
    components : {Sidebar}
  }
</script>
