<template>
	<ion-page style="font-family:Inter">
		<ion-content>
			<div class="mb-3 px-6 pt-8">
				<img class="w-24 mb-2" src="../assets/logo.png">
				<p class="text-xl font-bold">Formulir Pendaftaran</p>
				<p class="text-sm text-gray-500">Silahkan mengisi data dibawah</p>
			</div>

			<div class="px-2">

				<!-- Nama Pengguna -->
				<ion-item>
					<ion-label position="stacked">Nama Pengguna</ion-label>
					<ion-input @IonInput="user.username = $event.target.value"></ion-input>
				</ion-item>

				<!-- Kata Sandi -->
				<ion-item>
					<ion-label position="stacked">Kata Sandi</ion-label>
					<ion-input type="password" @IonInput="user.password = $event.target.value"></ion-input>
				</ion-item>

				<!-- Masukan Kata Sandi Lagi -->
				<ion-item>
					<ion-label position="stacked">Konfirmasi Kata Sandi</ion-label>
					<ion-input type="password" @IonInput="user.password_confirm = $event.target.value"></ion-input>
				</ion-item>

				<!-- Masukan Nama Depan -->
				<ion-item>
					<ion-label position="stacked">Nama Depan</ion-label>
					<ion-input @IonInput="user.firstname = $event.target.value"></ion-input>
				</ion-item>

				<!-- Masukan Nama Belakang -->
				<ion-item>
					<ion-label position="stacked">Nama Belakang</ion-label>
					<ion-input @IonInput="user.lastname = $event.target.value"></ion-input>
				</ion-item>

				<div class="mx-3 mt-4 flex text-sm">
					<button @click="presentAlertConfirm()" class="font-semibold bg-green-100 text-green-700 px-4 py-2 rounded">Mendaftar</button>
					<button class="font-semibold text-red-700 px-5 py-2 rounded">Batal</button>
				</div>
			</div>
		</ion-content>
	</ion-page>
</template>

<script type="text/javascript">
	
	// Import necessary library and framework
	import { crypto } from '@/function.js';
	import { IonButton, alertController } from '@ionic/vue';

	// API and Self Configuration
	const NodeRSA = require('node-rsa');
	const axios   = require('axios');
	const md5     = require('md5');
	const key     = new NodeRSA({b: 512});

	export default{
		data(){
			return{
				user : {
					username         : "",
					password         : "",
					password_confirm : "",
					firstname        : "",
					lastname         : "",
					privateKey       : key.exportKey("pkcs1-private-pem"),
					publicKey        : key.exportKey("pkcs8-public-pem")
				}
			}
		},
		methods : {

			async presentAlertConfirm() {
				const app = this;

				// validasi jika filed kosong
				if(app.user.username  == "" ||
				   app.user.password  == "" ||
				   app.user.firstname == "" ||
				   app.user.lastname  == ""){
					const alert = await alertController.create({
						header: 'Gagal',
						subHeader: 'Data tidak lengkap',
						message: 'Silahkan melengkapi semua data anda terlebih dahulu.',
						buttons: ['OK'],
					});
					return alert.present();
				}

				// validasi password jika sama
				if (app.user.password != app.user.password_confirm) {
					const alert = await alertController.create({
						header: 'Gagal',
						subHeader: 'Konfirmasi kata sandi gagal',
						message: 'Kolom kata sandi dan konfirmasi kata sandi harus sama',
						buttons: ['OK'],
					});
					return alert.present();
				}

				// mengecek jika user sudah terdaftar
				console.log((this.user.username + app.user.password));
				console.log(md5(this.user.username + app.user.password));
				if (localStorage.getItem(md5(app.user.username + app.user.password))) {
					const alert = await alertController.create({
						header: 'Gagal',
						subHeader: 'Pengguna sudah terdaftar',
						message: 'Pengguna dengan nama pengguna yang sama sudah ada sebelumnya',
						buttons: ['OK'],
					});
					return alert.present();
				}

				const alert = await alertController.create({
					header: 'Konfirmasi!',
					message: 'Dengan mendaftar, saya setuju bahwa semua data yang saya sudah dan akan masukan merupakan data yang sah',
					buttons: [
					{
						text: 'Batal',
					},
					{
						text: 'Ya, Setuju',
						handler: () => {
							app.register();
						},
					}],
				});
				return alert.present();
			},

			register(){
				delete this.user.password_confirm;
				let credential = md5(this.user.username + this.user.password);
				delete this.user.password;
				localStorage.setItem(credential, JSON.stringify(this.user));
				this.$router.replace("/account/login");
			}

		}
	}
</script>