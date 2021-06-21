<template>
	<div>
        
		<!-- Data Diri Pasien -->
    <div class="flex h-36 mx-2 my-5 items-center justify-center">
        <div class="grid bg-blue-500 rounded-lg shadow-xl mt-8 md:w-2/4 lg:w-2/4">

            <div class="flex p-3 mx-3 items-center">

                <!-- Foto Profil -->
                <avatar fullname="Chrisdityra Lengkey" size="60"></avatar>

                <!-- Nama dan Usia -->
                <div>
                    <h2 class="text-2xl text-white px-2 font-semibold">{{user.username}}</h2>
                    <h1 class="text-xl text-white font-bold px-2">{{user.umur}}</h1>
                </div>
                
            </div>

            <!-- Biodata Pasien -->
            <div>
                <div class="grid grid-cols-3 mx-6 my-3">

                    <div>
                        <p class="mb-1 text-sm leading-4 text-base font-bold text-white">Berat Badan</p>
                        <p class="text-sm leading-4 text-sm text-white">{{user.berat_badan}}</p>
                    </div>

                    <div>
                        <p class="mb-1 text-sm leading-4 text-base font-bold text-white">Tinggi Badan</p>
                        <p class="text-sm leading-4 text-sm text-white">{{user.tinggi_badan}}</p>
                    </div>

                    <div>
                        <p class="mb-1 text-sm leading-4 text-base font-bold text-white">Golongan Darah</p>
                        <p class="text-sm leading-4 text-sm text-white">{{user.golongan_darah}}</p>
                    </div>

                </div>
            </div>

        </div>

        <!-- Penyakit dan Alergi Pasien -->
        <div class="grid grid-rows-2 px-5 bg-white h-36 rounded-lg shadow-xl mt-8">
            <div class="flex p-5 items-center">

                <div class="mx-3">
                    <p class="text-sm leading-4 text-base font-bold text-gray-700">Penyakit</p>
                    <p class="mt-2 text-sm leading-4 text-sm text-gray-700">{{user.penyakit}}</p>
                </div>
        
            </div>

            <div class="px-5 mt-1 flex mx-3 items-center grid grid-cols-2 gap-10">

                <div class="">
                    <p class="text-sm leading-4 text-base font-bold text-gray-700">Alergi Obat</p>
                    <p class="mt-2 text-sm leading-4 text-sm text-gray-700">{{user.alergi_obat}}</p>
                </div>

                <div>
                    <p class="text-sm leading-4 text-base font-bold text-gray-700">Alergi Makanan</p>
                    <p class="mt-2 text-sm leading-4 text-sm text-gray-700">{{user.alergi_makanan}}</p>
                </div>
                
            </div>
            
        </div>
        
    </div>
		
      <form>
			<div class="grid grid-cols-2 gap-x-10 gap-y-4 px-5">
            <div>
               <label>Nama Dokter :</label>
               <p class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500">{{pemeriksaan.nama_dokter}}</p>
            </div>

            <div>
               <label>Nama Layanan Kesehatan :</label>
               <p class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500">{{pemeriksaan.layanan_kesehatan}}</p>
            </div>
			</div>

         <div class="px-5">
            <label class="pt-4 ">Hasil Pemeriksaan :</label>
            <input placeholder="contoh: Pasien mengalami penyakit sesak nafas" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text" v-model="text" id="hasil_pemeriksaan" required>

            <label class="pt-4">Obat yang Diberikan :</label>
            <input placeholder="contoh: Paracetamol, CTM, Vit.B" class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500" type="text" v-model="text" id="obat" required>
         </div>

         <div class="gap-x-3 w-48 pl-5">
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
            alergi_obat : "Asam Mefenamat",
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
