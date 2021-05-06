<template>

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

  <button @click="toggleModal">Tambahkan Data</button>
  
</template>

<script>
import { Modal } from './views/Modal.vue'

export default {
  name: 'App',
  views: { 
      Modal
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  border-bottom: 1px solid #ddd;
  display: inline-block;
  padding-bottom: 10px;
}
</style>
