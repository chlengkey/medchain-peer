<template>

      <form>

         <div class="top h-55 w-full bg-blue-600 overflow-hidden rounded-lg relative" >
            <div class="flex flex-col justify-center items-center relative h-full bg-black bg-opacity-50 text-white p-3">
               <img src="https://images.unsplash.com/photo-1603030431751-f3109cd8d53b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80" class="h-24 w-24 object-cover rounded-full">
               <h1 class="text-xl font-semibold pt-2">dr. {{doctor.name}}</h1>
               <h4 class="text-sm font-semibold mt-1">{{doctor.specialist}}</h4>
            </div>
         </div>

         <div class="grid grid-cols-2 gap-x-10 gap-y-4">
            <div>
               <label>Email:</label>
               <input placeholder="medical.chain@gmail.com" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="email"  v-model="email" id="email" required>
            </div>

            <div>
               <label>Password:</label>
               <input placeholder="min.8 karakter yang berisi huruf dan angka" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="password" v-model="password" id="password" required>
            </div>

            <div>
               <label>Nama Depan:</label>
               <input placeholder="Medical" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text"  v-model="text" id="fName" required>
            </div>

            <div>
               <label>Nama Belakang:</label>
               <input placeholder="Chain" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text" v-model="text" id="lName" required>
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
            <input placeholder="31.2.1.100.*.**.******" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="number" v-model="number" id="nomorSTR" required>

            <label class="pt-4">Tempat Praktek:</label>
            <input placeholder="Puskesmas Wenang" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text" v-model="text" id="tempatPraktek" required>
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
         doctor : {
            name : 'Cleyra Lovelace, S.Ked',
            specialist : 'Dokter Umum',
         },
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
