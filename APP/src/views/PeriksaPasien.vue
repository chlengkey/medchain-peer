<template>
	<div>
		<div class="flex items-center justify-center">
      	<div class="grid bg-blue-500 rounded-lg shadow-xl md:w-2/4 lg:w-2/4 mt-8">

            <div class="flex p-6 mt-1 items-center">

                <!-- Foto Profil -->
                <avatar fullname="Chrisdityra Lengkey" size="60"></avatar>

                <!-- Nama dan Usia -->
                <div>
                    <p class="mx-5 my-2 text-sm leading-4 text-2xl font-extrabold text-white">{{user.username}}</p>
                    <p class="mx-5 my-2 text-sm leading-4 text-xl font-medium font-extrabold text-white">{{user.umur}}</p>
                </div>
                
            </div>

            <!-- Biodata Pasien -->
            <div>
                <div class="grid grid-cols-3">

                    <div>
                        <p class="mx-7 text-sm leading-4 text-base font-bold text-white">Berat Badan</p>
                        <p class="mx-7 my-2 pb-3 text-sm leading-4 text-sm text-white">{{user.berat_badan}}</p>
                    </div>

                    <div>
                        <p class="text-sm leading-4 text-base font-bold text-white">Tinggi Badan</p>
                        <p class="my-2 text-sm leading-4 text-sm text-white">{{user.tinggi_badan}}</p>
                    </div>

                    <div>
                        <p class="text-sm leading-4 text-base font-bold text-white">Golongan Darah</p>
                        <p class="my-2 text-sm leading-4 text-sm text-white">{{user.golongan_darah}}</p>
                    </div>

                </div>
            </div>

        </div>

        <!-- Penyakit dan Alergi Pasien -->
        <div class="grid grid-rows-2 bg-white rounded-lg shadow-xl mt-8">
            <div class="flex p-4 items-center">

                <div>
                    <p class="mx-3 text-sm leading-4 text-base font-bold text-gray-700">Penyakit</p>
                    <p class="mx-3 my-2 text-sm leading-4 text-sm text-gray-700">{{user.penyakit}}</p>
                </div>
        
            </div>

            <div class="flex p-4 items-center grid grid-cols-2 gap-10">

                <div>
                    <p class="mx-3 pt-2 text-sm leading-4 text-base font-bold text-gray-700">Alergi Obat</p>
                    <p class="mx-3 my-2 text-sm leading-4 text-sm text-gray-700">{{user.alergi_obat}}</p>
                </div>

                <div>
                    <p class="mx-3 pt-2 text-sm leading-4 text-base font-bold text-gray-700">Alergi Makanan</p>
                    <p class="mx-3 my-2 text-sm leading-4 text-sm text-gray-700">{{user.alergi_makanan}}</p>
                </div>
        
            </div>
            
        </div>
        
    </div>
		
      <form>
			<div class="grid grid-cols-2 gap-x-10 gap-y-4">
            <div>
               <label>Nama Dokter :</label>
               <p class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500">{{pemeriksaan.nama_dokter}}</p>
            </div>

            <div>
               <label>Nama Layanan Kesehatan :</label>
               <p class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500">{{pemeriksaan.layanan_kesehatan}}</p>
            </div>
			</div>

         <div>
            <label class="pt-4 ">Hasil Pemeriksaan :</label>
            <input placeholder="contoh: Pasien mengalami penyakit sesak nafas" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text" v-model="text" id="hasil_pemeriksaan" required>

            <label class="pt-4">Obat yang Diberikan :</label>
            <input placeholder="contoh: Paracetamol, CTM, Vit.B" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text" v-model="text" id="obat" required>
         </div>

         <div class="grid grid-cols-2 gap-x-3 w-48">
            <p class="mt-5 text-center yellow-glow-button">Simpan</p>
         </div>

      </form>
	</div>
      

</template>

<script>
import Avatar from 'vue-avatar-component'


export default {
   data(){
      return {
			pemeriksaan : {
				nama_dokter : "Cleyra Lovelace",
				layanan_kesehatan : "RS. Pancaran Kasih",
				hasil_pemeriksaan : "",
				obat : ""
			},

         user : {
				username : "Chrisdityra Lengkey",
				umur  : "20 tahun",
				berat_badan : "58 kg",
            tinggi_badan : "169 cm",
            golongan_darah : "A+",
            penyakit : "Amandel dan Maag",
            alergi_obat : "Asam Sulfat",
            alergi_makanan : "Kacang Tanah"
         }
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
   padding: 30px;
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
