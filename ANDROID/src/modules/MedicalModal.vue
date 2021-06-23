<template>
	<div style="font-family:Inter">
		<div class="pt-4 fixed w-full border-b">
			<div class="px-4 grid grid-cols-12 mb-4">
				<div class="col-span-9">
					<p class="font-semibold">Medical Record</p>
					<p class="text-xs text-gray-500">Hasil Pemeriksaan Pasien Sebelumnya</p>
				</div>
				<button @click="dismiss()" class="col-span-3 text-sm text-center bg-red-100 px-4 py-2 transition hover:bg-gray-900 hover:text-white cursor-pointer rounded-md text-red-600 inline-block font-semibold">Periksa</button>
			</div>
			<ion-progress-bar v-if="showProgressBar" type="indeterminate"></ion-progress-bar>
		</div>
		<div class="h-20"></div>
		
		<div class="mx-4 mt-4">
			<div	class="border-b border-gray-400 pb-3 mb-5">
				<p class="font-bold text-sm">{{MedicalRecord.date}}</p>
				<p class="text-sm mt-0 text-gray-600">{{MedicalRecord.doctor}}</p>
		   </div>
		</div>

	</div>
</template>

<script type="text/javascript">
	
	// API
	const NodeRSA = require('node-rsa');
	const axios = require('axios');

	// UI
	import { modalController, IonProgressBar, IonContent} from '@ionic/vue';

	// Settings
	import { crypto } from '@/function.js';
	let cryptoFunc = new crypto();
	

	export default{
		components : {IonContent, IonProgressBar},
		name : "Generate Token",
		data(){
			return{
				showProgressBar : false,
				MedicalRecord : [
					{
						date    : "19/05/2019",
						doctor  : "Cleyra Lovelace",
						clinic  : "Puskesmas Tomohon"
					},
					{
						date   : "29/01/2020",
                  doctor : "Aura Tuff",
                  clinic : "RS. Pancaran Kasih Manado"
					}
				]
			}
		},
		methods : {

			dismiss : function(){
				modalController.dismiss();
			},
		},
		created(){
		}
	}
</script>