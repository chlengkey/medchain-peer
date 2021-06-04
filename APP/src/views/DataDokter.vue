<template>

      <form>

         <div class="flex justify-center py-2">
            <avatar fullname="Chrisdityra Lengkey" size="60"></avatar>
         </div>

         <div class="grid grid-cols-2 gap-x-10 gap-y-4">
            <div>
               <label>Email:</label>
               <input placeholder="contoh: tekotok@gmail.com" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="email"  v-model="email" id="email" required>
            </div>

            <div>
               <label>Password:</label>
               <input placeholder="min.8 karakter yang berisi huruf dan angka" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="password" v-model="password" id="password" required>
            </div>

            <div>
               <label>Nama Depan:</label>
               <input placeholder="contoh: Tekotok" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text"  v-model="text" id="fName" required>
            </div>

            <div>
               <label>Nama Belakang:</label>
               <input placeholder="contoh: Vernalta" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text" v-model="text" id="lName" required>
            </div>
         </div>

         <div>
            <label>Jenis Kelamin</label>
               <div class="grid grid-cols-2 gap-x-5">
                  <div class="flex mt-3 text-sm">
                     <input class="mt-1 mr-1" type="radio" value="a" v-model="picked">Pria
                  </div>

                  <div class="flex mt-2 text-sm">
                     <input class="mt-1 mr-1" type="radio" value="b" v-model="picked">Wanita
                  </div>
               </div>
         </div>

         <div>
            <label class="pt-4 ">nomor str:</label>
            <input placeholder="contoh: 31.2.1.100.*.**.******" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="number" v-model="number" id="nomorSTR" required>

            <label class="pt-4">Tempat Praktek:</label>
            <input placeholder="contoh: RS. Siloam Manado" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text" v-model="text" id="tempatPraktek" required>
         </div>

         <div class="grid grid-cols-2 gap-x-3 w-48">
            <p class="mt-3 text-center yellow-glow-button">Edit</p>
            <p class="mt-3 text-center yellow-glow-button">Simpan</p>
         </div>

      </form>

      

</template>

<script>
import Select from '../components/form_component/select.vue'
import Avatar from 'vue-avatar-component'


export default {
   data(){
      return {
         email : '',
         password : '',
         picked : '',
         text : '',
         number : ''
      }
   },
   components: {Avatar}

}
</script>

<style scoped>

input::-webkit-outer-spin-button,
        input::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
  
        input[type=number] {
            -moz-appearance: textfield;
        }

form {
   background: white;
   text-align: left;
   padding: 40px;
   border-radius: 8px;
}
label {
   color: #aaa;
   display: inline-block;
   margin: 20px 0 0 5px;
   font-size: 10px;
   text-transform: uppercase;
   letter-spacing: 1px;
   font-weight: bold;
}
/*
input {
   display: block;
   box-sizing: border-box;
   border-width: 2px;
   border-radius: 4px;
   border-color: #4d79ff;
}*/
</style>
