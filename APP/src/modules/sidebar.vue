<template>
	<div class="h-full">
		<TokenModal ref="tokenModal" />

		<div class="md:w-56"></div>
		<div class=" fixed w-56 bg-blue-500 h-full shadow">
			
			<div class="px-4 mt-5">
				<img src="@/assets/logo.png" class="w-8 mb-5">
			</div>
			
			<!-- divider -->
			<hr class="my-5 border-white opacity-30" />

			<div class="w-full px-5 text-sm relative">

				<p class="yellow-glow-button w-full" @click="$refs.tokenModal.open()"><Plus class="mr-1" />Pemeriksaan Baru</p>
				
				<router-link to="/" class="flex">
					<p class="nav-item"><Home class="-mt-0.5 mr-2"/>Dashboard</p>
				</router-link>
				
				<router-link to="/pasien/:token">
					<p class="nav-item"><UserGroup class="-mt-0.5 mr-2"/>Data Pasien</p>
				</router-link>

				<router-link to="/dataDokter">
					<p class="nav-item"><UserAdd class="-mt-0.5 mr-2"/>Data Dokter</p>
				</router-link>
				
				<router-link to="/pengaturan">
					<p class="nav-item"><Cog class="-mt-0.5 mr-2"/>Pengaturan</p>
				</router-link>

			</div>

		</div>
	</div>
</template>

<style type="text/css">
	
	.nav-item{
		@apply text-white font-semibold mt-2 hover:text-gray-800 transition rounded-md  cursor-pointer py-2;
	}

</style>

<script type="text/javascript">
	
	//import axios from 'axios';

	// Components
	import TokenModal from '@/modules/tokenModal.vue';

	// Icons
	import Plus from '@/assets/icons/plus.vue'
	import Home from '@/assets/icons/home.vue'
	import UserAdd from '@/assets/icons/userAdd.vue';
	import UserGroup from '@/assets/icons/userGroup.vue'
	import LogOut from '@/assets/icons/logout.vue'
	import Cog from '@/assets/icons/cog.vue'
	import ShieldCheck from '@/assets/icons/shieldCheck.vue'

	export default{
		components : {
			// components
			TokenModal,
			// icons
			Plus, Home, UserAdd, UserGroup, LogOut, Cog, ShieldCheck
		},

		data(){
			return{

				// immutable
				blockchainValidity : false,
			
				// mutable
				klinik : {
					dokter     : "Cleyra Lovelace",
					medical_service_name  : "TOMOHON",
					medical_service_level : "KLINIK"
				}
			}
		},

		methods : {
			logOut : function(){
				alert("Logging out!");
			}
		},
		created(){
			//this.$axios.get("ger");
		}
	}
</script>