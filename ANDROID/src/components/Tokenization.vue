<template>
	<!--<div @click="tokenOpen()"-->
	<div @click="showModal()"
		class="bg-orange-500 h-full rounded-md p-3 text-white text-xs font-bold" style="font-family:'Inter'">
		<ion-icon class="mr-1" :icon="timer" />
		<ion-icon :icon="lockClosed" />
		<br/>Buat Token<br/>
		<span class="font-normal">Membantu pemeriksaan lebih aman</span>
   </div>
</template>

<script type="text/javascript">

	// Modules
	import TokenModal from '@/modules/TokenModal.vue';
	import { modalController, alertController, IonIcon } from '@ionic/vue';

	// Components and Icons
	import { timer, lockClosed } from 'ionicons/icons';

	// API
	import {VUE_APP_API} from '@/function.js'
	const axios = require('axios');
	
	export default{
		components : {IonIcon},
		data(){
			return{
				clinicData : [
					{
						klinikNama : "Puskesmas Tomohon",
						klinikAlamat : "Jl. Tomohon",
						klinikId     : "public_key"
					}
				],
				lockClosed,
				timer,
				tokenLocal  : "",
				expiredTime : 9999999999999,
			}
		},
		props : ['token'],
		methods : {
			
			showModal : async function(){
				const modal = await modalController.create({
					component: TokenModal,
				})
				await modal.present()
			},
			
			getTimestamp : function() {
				const timestamp = new Date();
				const timestampNow = timestamp.getTime();
				return timestampNow;
			},

			getTokenExpireTime : function() {
				return parseInt((this.expiredTime - this.getTimestamp()) / 3600000 * 60); 
			},

			generateToken : function(){

				// PAYLOAD
				// enkripsi private_key dengan menggunakan public_key fasilitas kesehatan
				axios.get(VUE_APP_API + "/token/generate")
					.then(response => {
						console.log(response);
					})

				//const min = 10000;
				//const max = 99999;
				//const token = Math.floor(Math.random() * (max-min)) + min;
				//return token
			},
			
			getToken : function(){
				return this.tokenLocal;
			},

			tokenOpen : function(){

				/* 
					Mengecek Jika Token sudah expire atau belum
				*/
				if (this.getTokenExpireTime() <= 0) {
					this.tokenExpired();
					this.tokenLocal = "";
					this.expiredTime = 0;
				}

				else {

					/*
						Membuat Token Baru
					*/
					if (this.tokenLocal == "") {
						this.tokenNew();
					}

					/*
						Menampilkan Token yang sudah di generate
					*/
					else {
						this.tokenMain();
					}
				}
			},

			async tokenNew(){
				const app = this;
				const alert = await alertController.create({
					header    : 'Buat Token',
					subHeader : "Anda Setuju?",
					message   : "<p class='text-sm'>Dengan membuat token anda setuju memberikan data rekam medis anda</p>",
					buttons   : ['Batal',
						{
							text:'Setuju', 
							handler : () => {
								app.tokenLocal  = app.generateToken();
								app.expiredTime = app.getTimestamp() + 1800000;
								//app.tokenMain();
							}
						}
					]
				});
				await alert.present();
			},

			async tokenExpired(){
				const app = this;
				const alert = await alertController.create({
					header    : 'Mengambil Token Gagal',
					subHeader : "Token sudah expire",
					message   : "<p class='text-sm'>Token anda telah melewati batas waktu yang ditentukan, silahkan buat lagi</p>",
					buttons   : [{text:'Ok', handler : () => {
						app.tokenNew();
					}}]
				});
				await alert.present();
				await alert.onDidDismiss();	
			},

			async tokenMain() {
				let htmlAlert = "";
				htmlAlert += "<p class='text-sm'>"
				htmlAlert += "Silahkan memberikan token kepada staff medis untuk mengizinkan pengaksesan data rekam medis anda</p>";
				htmlAlert += "<p class='text-center text-4xl text-orange-600 font-bold'>" + this.tokenLocal + "</p>";
				htmlAlert += "<p class='text-xs text-center'>Sisa Waktu : <span class='text-red-500 font-bold'>" + this.getTokenExpireTime() + " Menit</span></p>"

				const alert = await alertController.create({
					cssClass: 'my-custom-class',
					header: 'Token',
					subHeader: 'Berhasil dibuat',
					message: htmlAlert,
					buttons: ['OK'],
				});
				await alert.present();
			}

		},

		created(){
			if (this.token) {
				this.tokenLocal = this.token;
			}
		},
	}
</script>