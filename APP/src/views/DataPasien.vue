<template>


<div>

    
    <!-- Data Diri Pasien -->
    <div class="flex h-36 mx-2 my-5 items-center justify-center">
        <div class="grid bg-blue-500 rounded-lg shadow-xl mt-8 md:w-2/4 lg:w-2/4">

            <div class="flex p-3 mx-3 items-center">

                <!-- Foto Profil -->
                <img class="inline object-cover w-16 h-16 mr-2 rounded-full" src="https://images.unsplash.com/photo-1612061279301-c1bd3a484fcf?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80" />

                <!-- Nama dan Usia -->
                <div>
                    <h2 class="text-2xl text-white px-2 font-semibold">{{user.username}}</h2>
                    <h1 class="text-xl text-white font-bold px-2">{{user.umur}} tahun</h1>
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

    <!-- Riwayat Pemeriksaan -->
    <div class="flex items-center justify-center">
    <div class="bg-blue-500 rounded-lg shadow-xl mt-8 mx-10 w-full">

        <div class="grid grid-cols-2">
            <div>
                <p class="ml-5 mt-5 text-sm leading-4 text-xl font-extrabold text-white">Riwayat Pemeriksaan</p>
                <p class="ml-5 my-3 text-sm leading-4 font-bold text-white">Hasil Pemeriksaan Pasien Sebelumnya</p>
            </div>
            
            <div>
                <div class="container py-6 px-5 grid justify-items-end">
                <input class="w-3/5 items-right h-7 rounded focus:outline-none focus:shadow-outline text-sm px-3 shadow-lg" type="search" placeholder="Tulis disini untuk mencari...">
                </div>
            </div>
        </div>

        <div class="px-5 py-4">
            <table class="table-auto border-seperate border border-black-800">
                <thead>
                    <tr class="bg-blue-200">
                    <th class="w-2/5 p-2">Tanggal Pemeriksaan</th>
                    <th class="w-2/5 p-2">Tempat Pemeriksaan</th>
                    <th class="w-1/5 p-2">Nama Dokter</th>
                    <th class="w-1/5 p-2">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td class="border border-black-600 p-2">00/00/0000</td>
                    <td class="border border-black-600 p-2">Puskesmas</td>
                    <td class="border border-black-600 p-2">Dr. Medical Chain</td>
                    <td class="border border-black-600 p-2" @click="open()"><Folder/></td>
                    </tr>
                    <tr>
                    <td class="border border-black-600 p-2">00/00/0000</td>
                    <td class="border border-black-600 p-2">Klinik</td>
                    <td class="border border-black-600 p-2">Medical, S.Ked</td>
                    <td class="border border-black-600 p-2" @click="open()"><Folder/></td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <div>
            <router-link to="/pasien/periksa/tambah/:token">
            <button class="p-2 ml-3 mb-3 bg-blue-600 rounded-lg text-white"><Plus/>Tambah</button>
            </router-link>
        </div>

    </div>

    </div>

</div>


</template>

<script>
  import Avatar from 'vue-avatar-component'
  import Folder from '@/assets/icons/folder.vue'
  import Plus from '@/assets/icons/plus.vue'

  export default {
    components: { Avatar, Folder, Plus },

    data(){
        return{
            // mutable
				user : {
					username : "Patient",
					umur  : "19",
					berat_badan : "0",
                    tinggi_badan : "0",
                    golongan_darah : "A",
                    penyakit : "none",
                    alergi_obat : "none",
                    alergi_makanan : "none"
            }
        }
    }
  }

   
</script>