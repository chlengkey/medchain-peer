<template>

   <div class="h-full">
		<TokenModal ref="tokenModal" />
   
   <div class="container mx-auto p-5 px-6">
         <div class="h-64 rounded-md overflow-hidden bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1612537783705-8be992d21502?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=667&q=80')">
             <div class="bg-gray-900 bg-opacity-50 flex items-center h-full">
                 <div class="px-10 max-w-xl">
                     <h2 class="text-2xl text-white font-semibold">Hallo, {{klinik.dokter}}</h2>
                     <p class="text-xs text-white mb-2 mt-0.5">{{klinik.medical_service_level}} {{klinik.medical_service_name}}</p>
                     <button class="flex items-center mt-4 px-3 py-2 bg-blue-600 text-white text-sm uppercase font-medium rounded hover:bg-blue-500 focus:outline-none focus:bg-blue-500" @click="$refs.tokenModal.open()">
                        <span>Pemeriksaan Baru</span>
                           <svg class="h-5 w-5 mx-2" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor"><path d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                     </button>
                  </div>
            </div>
         </div>
   </div>

   <div class="p-5" >
                <h3 class="text-gray-600 text-2xl font-medium">Rekam Medis Pasien</h3>
                <div class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 mt-6">
                    <div class="w-full max-w-sm mx-auto rounded-md shadow-md overflow-hidden">
                        <div class="flex items-end justify-end h-56 w-full bg-cover" style="background-image: url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80')">
                        </div>
                        <div class="px-5 py-3">
                            <h3 class="text-gray-700 uppercase">Lihat Rekam Medis</h3>
                            <span class="text-gray-500 mt-2">Rekam Medis pemeriksaan sebelumnya</span>
                        </div>
                    </div>
                    <div class="w-full max-w-sm mx-auto rounded-md shadow-md overflow-hidden">
                        <div class="flex items-end justify-end h-56 w-full bg-cover" style="background-image: url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80')">
                        </div>
                        <div class="px-5 py-3">
                            <h3 class="text-gray-700 uppercase">Buat Rekam Medis Baru</h3>
                            <span class="text-gray-500 mt-2">Menambahkan hasil pemeriksaan yang baru</span>
                        </div>
                    </div>
                </div>
            </div>
   </div>	

</template>

<script type="text/javascript">

import TokenModal from '@/modules/tokenModal.vue';
	
	export default{
      components : {
			// components
			TokenModal
      },

		data(){
			return{
			
				// mutable
				klinik : {
					dokter     : "Cleyra Lovelace",
					medical_service_name  : "TOMOHON",
					medical_service_level : "KLINIK"
				}
			}
		},

		created(){
			//this.$axios.get("ger");
		}
	}
</script>
