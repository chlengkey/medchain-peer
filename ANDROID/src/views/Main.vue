<template>
	<ion-page>
		<ion-content :fullscreen="true">

			<div class="px-5 pt-6">
				<img src="../assets/85418.svg" style="opacity:0.08;top:0;left:0;z-index:-1" class="opacity-5 w-full absolute z-0 mt-2 align-bottom col-span-5">
				<!-- Content Header -->
				<div class="grid grid-cols-6 mb-5">
					<img src="../assets/logo.png" class="w-32 mt-2 align-bottom col-span-5">
					<!-- Account -->
					<ion-router-link href="/account">
						<ion-avatar class="absolute right-0">
							<img class="h-8 w-8 ahsolute ml-3" src="../assets/avatar.png">
						</ion-avatar>
					</ion-router-link>
				</div>
				<div class="my-16" style="font-family:Inter">
					<p class="text-xl text-center font-semibold">Hi, {{user.firstname}}</p>
					<p class="text-sm text-center text-gray-500 mb-4">Ada yang bisa kami bantu untuk anda?</p>
				</div>
			</div>

			<!-- Covid Protocol -->
			<div class="mx-5 rounded-xl mb-3 flex" style="background-color:#824097;font-family:Inter">
				<img class="-ml-1 h-auto w-2/6" src="../assets/shield.svg">
				<div class="relative h-auto w-full"> 
					<div class="-ml-1 absolute w-full top-1/2 transform -translate-y-1/2" style="top:50%">
						<p class="font-semibold text-sm text-purple-300">Protokol Covid-19</p>
						<p class="text-xs text-white pr-4 text-purple-100">Jangan lupa menerapkan protokol kesehatan kemanapun anda pergi!</p>
					</div>
				</div>
			</div>
			
			<!-- Button Group -->
			<div class="grid px-5 grid-cols-3 gap-2">
				<MedRec ref="medrec"></MedRec>
				<Tokenization ref="tokenization"></Tokenization>
         	</div>

			<div class="border-b border-gray-400 pb-3 mb-5"></div>
			
			<div style="font-family:Inter" class="mb-10">
				<p class="text-lg font-bold mx-4 mt-0.5">Riwayat Pemeriksaan Anda</p>
				<p class="text-sm text-gray-600 mx-4 mb-5">Setiap riwayat kesehatan kamu, kami catat kok</p>
				<div class="mx-4">
					<div class="border-b border-gray-400 pb-3 mb-5"
						 v-for="record in record_data">
						<p class="text-xs text-gray-600 font-semibold">DIAGNOSA</p>
						<p class="text-sm mt-0 text-gray-900">{{record.anamnesis.diagnosis}}</p>
						<p class="text-xs text-gray-600 mt-2 font-semibold">KELUHAN</p>
						<p class="text-sm mt-0 text-gray-900 mb-3">{{record.anamnesis.complaint}}</p>
						<p class="text-xs text-gray-600 mt-2 font-semibold">OBAT</p>
						<p class="text-sm mt-0 text-gray-900 mb-3">{{record.anamnesis.drugs}}</p>
						<p class="font-semibold text-xs text-gray-600">{{record.anamnesis.date_time}}</p>
						<p class="text-sm mt-0 text-gray-900">{{record.anamnesis.facility}}</p>
				   </div>
				</div>
				<div class="mx-4 text-xs bg-red-100 text-red-500 py-2 px-4 font-semibold rounded" 
					 v-if="record_data.length <= 0">
					Anda belum memiliki riwayat pemeriksaan
				</div>
			</div> 
            
		</ion-content>
	</ion-page>
</template>

<script type="text/javascript">
	
	// UI and Components
	import { IonAvatar, IonPage, IonContent, IonIcon} from '@ionic/vue';
	import { medical, timer, book, notifications, shieldCheckmark, lockClosed, close} from 'ionicons/icons';
	import Tokenization from '@/components/Tokenization.vue';
	import MedRec from '@/components/MedicalRecord.vue';

	// API's
	import { crypto } from '@/function.js';
	const axios = require('axios');
	let cryptoFunc = new crypto();

	export default{
		components : {IonAvatar, IonPage, IonContent, IonIcon, Tokenization, MedRec},
		data(){
			return{
				book,shieldCheckmark,notifications,
				user : {},
				blockchain : {
					valid : true
				},
				record_data : []
			}
		},
		methods : {
			get_patient_data(){
				var app = this;
				let patientId = localStorage.getItem("logged")
				axios.get("http://127.0.0.1:5000/data/patient/raw/" + patientId)
					 .then(response => {
					 	app.record_data = response.data;
					 	response.data.forEach((patient_data,index) => {
					 		let anamnesis = patient_data.anamnesis;
					 		Object.keys(anamnesis).forEach(anamnesis_key => {
					 			if (anamnesis_key != "date_time" && anamnesis_key != "date") {
					 				let anamnesis_data = cryptoFunc.decrypt(anamnesis[anamnesis_key]);
					 				anamnesis[anamnesis_key] = anamnesis_data;
					 			}
					 		})

					 		let patient = patient_data.patient;
					 		Object.keys(patient).forEach(patient_key => {
					 			if(patient_key != "id"){
					 				let patient_data = cryptoFunc.decrypt(patient[patient_key]);
					 				patient[patient_key] = patient_data;	
					 			}			 			
					 		})
					 		app.record_data[index].anamnesis = anamnesis;
					 		app.record_data[index].patient = patient;
					 	})

					 })
		    },
		},
		created(){
			var app = this;
			let loginCredential = localStorage.getItem('logged');
			setTimeout(function(){	
				if (loginCredential) {
					let data = localStorage.getItem(loginCredential); 
					app.user = JSON.parse(data);
					app.get_patient_data();
				}
			}, 1000)
		}
	}
</script>