<template>
	<div @click="tokenOpen()"
		class="bg-orange-500 h-full rounded-md p-3 text-white text-xs font-bold" style="font-family:'Inter'">
		<ion-icon class="mr-1" :icon="timer" />
		<ion-icon :icon="lockClosed" /><br/>Buat Token<br/><span class="font-normal">Membantu pemeriksaan lebih aman</span>
    </div>
</template>

<script type="text/javascript">

import { timer, lockClosed } from 'ionicons/icons';
import {alertController} from '@ionic/vue';

	export default{
		data(){
			return{
				lockClosed,
				timer,
				tokenLocal  : "",
				expiredTime : 9999999999999
			}
		},
		props : ['token'],
		methods : {

			getTimestamp : function() {
				const timestamp = new Date();
				const timestampNow = timestamp.getTime();
				return timestampNow;
			},

			getTokenExpireTime : function() {
				return parseInt((this.expiredTime - this.getTimestamp()) / 3600000 * 60); 
			},

			generateToken : function(){
				const min = 10000;
				const max = 99999;
				const token = Math.floor(Math.random() * (max-min)) + min;
				return token
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
					buttons   : ['Batal',{text:'Setuju', handler : () => {
						app.tokenLocal  = app.generateToken();
						app.expiredTime = app.getTimestamp() + 1800000;
						app.tokenMain();
					}}]
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