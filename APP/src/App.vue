<template>

  <div class="flex">
    <Sidebar/>
    <router-view/>
  </div>
  <!--
  <h1>{{ title }}</h1>
  <p>Selesai Menambahkan Data?</p>

  <div v-if="showModal">

    <Modal theme="sale" @close="toggleModal">
      <template v-slot:links>
        <a href="#">more info</a>
        <a href="#">status blockchain</a>
      </template>

      <h1>Berhasil Ditambahkan</h1>
      <p>Data yang telah ditambahkan tidak dapat diubah kembali</p>
    </Modal>

  </div>

  <button @click="toggleModal">Tambahkan Data</button>-->
  
</template>

<script>
//import { Modal } from '@/views/Modal.vue'
import Sidebar from '@/modules/sidebar.vue'
import Dashboard from '@/views/Dashboard.vue'

export default {
  name: 'App',
  components : {Sidebar, Dashboard},
  views: { 
  //    Modal,
      Dashboard
  },
  data() {
    return {
      title: 'Medical Chain',
      showModal: false,
      showModalTwo: false
    }
  },
  methods: {
    toggleModal(){
      this.showModal = !this.showModal
    },
    toggleModalTwo(){
      this.showModalTwo = !this.showModalTwo
    }
  }
}
</script>

<style>

</style>