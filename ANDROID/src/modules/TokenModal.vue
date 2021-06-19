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
		<div class="h-20"></div>
		
		<div class="mx-4 mt-4">
			<div	class="border-b border-gray-400 pb-3 mb-5"
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
						clinicHost    : "http://192.168.1.13",
						clinicId      : "b'-----BEGIN PUBLIC KEY-----\nMIICSDANBgkqhkiG9w0BAQEFAAOCAjUAMIICMAKCAicAtiONJExI/bu+GhPMY8Xl\nYdN1FtGuBgoxuCEHeAZeJ1TCllWcTMswBS5aooIFYEMgbgtA4Od8Ru5Zk9ZHbhSA\n1pKkiK/KuIoTSNMcxcTkC6TKjfNNGYW3UcXgBc624NIPqKZfwAueYsUYx4jIixDU\nULinGzc+SfIcBRnoCVWt4bcF/0iozOhe8BmQQbmktJo4dbdDLYfWN/x6gsKXyaPG\nRbZQ4+LjT3b+qIT65Y44w7lcXQ0OfzbgHYGzdOrNuNqgEBrCfkR4JZsGedPHPSra\nyJT4BGzhTbkBTzNWzhalM/s8EmWJlI/Glg6+pNxcInJUODrZkXqVCupP5Qgfe4HI\nZ1rrpLxdI6/G+IelGoceUoweBqYzjIkjVvZm3sq781i9CpyHzxcnTTu5XJsBrHgc\nSyDzVzIifCNB+yV2J7DT0gTNgBHpooxK8cAilaJYkDWf+AhIla6n5SqrMsg1Ax6Q\nLUAwEE5X9dDQVcT93tsOtHoPhZsDj6ewkrO999UrC3ZIDjTLsfIgNsUj6zsCBfIo\nV69nQXGyuRHf3d0tVM2rgt8FUbvFm2ivM1awf0nNr7LUqRUOyGjgHqgFlnj5g73L\nV+cYzwq0sTiGHFr0y5anRMpZTrgPHZvU7Ag+E+iB2QfmD8QvP476uYSOhw72FZCv\nhIZjowVrwl4ArM17fUtlQLEgp60XvRiScCS7wqxb6h6Xc+GQIJkUtDKT84iPoD8F\nb1dK0pjKuQIDAQAB\n-----END PUBLIC KEY-----'" 
					},
					{
						clinicName    : "Puskesmas Manado",
						clinicAddress : "Jl. Raya Manado Tomohon",
						clinicHost    : "http://192.168.1.10",
						clinicId      : "b'-----BEGIN PUBLIC KEY-----\nMIICSDANBgkqhkiG9w0BAQEFAAOCAjUAMIICMAKCAicAr9Wlj3LCYQXdMifsCXUu\nt4f0snZqIamj4+g89rIb8ms+LPpJkR9slmGk2KirxlQggrVgWAkoLU/lGrfs6pV5\n4Rem3Gp+SfMt8C9lg10eFtu1H2ZGrp3lcpBwW84RjR3pqUbBC0NOLKWQN1HA0k1n\nZUXgDWe6sgwkWPQ0cEeK5e/QE8GQavIPOgNu2HMW3JnEAZpDw/gni/h5jbPcjTtf\nsM7X1PFwU+LqPwZq3AVze5x7tvQMmfMH9cSSkZ4bdJ6n0/kYOjn3W0tKYurUOzBJ\nuciJBiozStc5LM4Rv5H5pZOvuczEEyV7G43OSVNp1m25P6z+5ww/Z4TtKCXnVIJa\n+7ybDkYhB+8+hq9z8RGzwXgGNFJ9TkgPAHgoCTDUORvZG9lMIcvbybzz5vkxgBbI\nqtFnPwUbRCG97ysNXpHroRXqx089IAUSqxaHKMFa+QTteB5BSc2UstuhNedpa7oP\n1YVGM7EVBZvfICvZhBrh5XWegS1arZF2obVTw6W0lpoJLjqMzT9AVk22lSDrTg0a\nby65fIhEcOtQhzsoaxD3hETRVMFm4SS2X1EFshwf0CiCFghBPH78cBUz6afPu64R\nvdXLYMECI6Pyy5fAuySOa4BVtdBpOFXB0vUbQ/Mo97bAqvrpnoJqttposCl4ZHKu\nQNUXQ9B6OGaR7AHNKy7nK52FH5of8VkZurTerOKcgn19nPr8sDMy5LuamOq0PE3D\ntailv+qOxQIDAQAB\n-----END PUBLIC KEY-----'" 
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
				//let privateData = cryptoFunc.encryptUsingPublicKey(clinic.clinicId, "riwayat pasien");
				let data = {
					payload : privateData,
					patient : "patient"
				};
				axios.post(clinic.clinicHost + ":5000/token/generate", data)
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