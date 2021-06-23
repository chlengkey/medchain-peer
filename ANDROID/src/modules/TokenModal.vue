<template>
	<div style="font-family:Inter">
		<div class="pt-4 fixed w-full border-b">
			<div class="px-4 grid grid-cols-12 mb-4">
				<div class="col-span-9">
					<p class="font-semibold">Buat Token</p>
					<p class="text-xs text-gray-500">Masa berlaku 60 menit</p>
				</div>
				<button @click="dismiss()" class="col-span-3 text-sm text-center bg-red-100 px-4 py-2 transition hover:bg-gray-900 hover:text-white cursor-pointer rounded-md text-red-600 inline-block font-semibold">Batal</button>
			</div>
			<ion-progress-bar v-if="showProgressBar" type="indeterminate"></ion-progress-bar>
		</div>

		<!-- Buka Pemisah -->
		<div class="h-20"></div>
		<!-- Tutup Pemisah -->

		<div class="mx-4 mt-4">
			<div class="border-b border-gray-400 pb-3 mb-5"
				 v-for="clinic in clinics" :key="clinic.clinicId"
		    	 @click="proceedToMakeToken(clinic)">
				<p class="font-bold text-sm">{{clinic.clinicName}}</p>
				<p class="text-sm mt-0 text-gray-600">{{clinic.clinicAddress}}</p>
		   </div>
		</div>

	</div>
</template>

<script type="text/javascript">
	
	// API
	const NodeRSA = require('node-rsa');
	const axios = require('axios');

	// UI
	import { modalController, alertController, IonProgressBar, IonContent} from '@ionic/vue';

	// Settings
	import { crypto } from '@/function.js';
	let cryptoFunc = new crypto();
	

	export default{
		components : {IonContent, IonProgressBar},
		name : "Generate Token",
		data(){
			return{
				showProgressBar : false,
				clinics : [
					{
						clinicName    : "Puskesmas Tomohon",
						clinicAddress : "Jl. Raya Manado Tomohon",
						clinicHost    : "http://127.0.0.1",
						clinicId      : "b'-----BEGIN PUBLIC KEY-----\n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\nAAE=\n-----END PUBLIC KEY-----'" 
					}
				]
			}
		},
		methods : {

			dismiss : function(){
				modalController.dismiss();
			},

			proceedToMakeToken : function(clinic){
				const app = this;
				this.showProgressBar = true;
				let privateData = cryptoFunc.encryptPrivateKeyUsingPublic(clinic.clinicId);
				let patientId = localStorage.getItem("logged")
				let patientData = JSON.parse(localStorage.getItem(patientId))
				let patientName = patientData.firstname + " " + patientData.lastname
				let rebuildPatientData = {
					"id" : patientId,
					"name" : patientName,
					"publicKey" : patientData.publicKey
				}

				let data = {
					payload : privateData,
					patient : rebuildPatientData
				}
				
				axios.post(clinic.clinicHost + ":5000/token/create", data)
				     .then(response => {
						  console.log(response.data);
						  alert("Token berhasil digenerate : " + response.data.token);
						  app.showProgressBar = false;
				     })
					  .catch(error => {
						  console.log(error);
					  })
			}
		},
		created(){
		}
	}
</script>