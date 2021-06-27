<template>
	<ion-page style="font-family:Inter">
		<ion-content>
			<div class="mb-3 px-6 pt-8">
				<img class="w-24 mb-2" src="../assets/logo.png">
				<p class="text-xl font-bold">Masuk</p>
				<p class="text-sm text-gray-500">Silahkan masuk menggunakan akun yang telah terdaftar sebelumnya</p>
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
				<div class="mx-3 mt-4">
					<a class="text-sm text-gray-500 no-underline hover:underline" href="/account/register">Anda belum punya akun? klik disini</a><br/>
					<button @click="login()" class="font-semibold bg-green-100 text-green-700 px-4 py-2 rounded mt-2">Masuk</button>
				</div>
			</div>
		</ion-content>
	</ion-page>
</template>

<script type="text/javascript">
	const md5 = require('md5');

	export default{
		data(){
			return{
				user : {
					username : "",
					password : ""
				}
			}
		},
		methods : {
			login(){
				if (localStorage.getItem(md5(this.user.username + this.user.password))) {
					localStorage.setItem('logged', md5(this.user.username + this.user.password));
					this.$router.replace("/");
				}
				else{
					alert('Nama pengguna dan kata sandi anda tidak cocok');
				}
			}
		}
	}
</script>