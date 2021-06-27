<template>
	<ion-page>
		<ion-content :fullscreen="true">

			<div class="px-5 pt-6">
				<img src="../assets/85418.svg" style="opacity:0.08;top:0;left:0;z-index:-1" class="opacity-5 w-full absolute z-0 mt-2 align-bottom col-span-5" >

				<!-- Content Header -->
				<div class="grid grid-cols-6 mb-5">
				<img src="../assets/logo.png" class="w-32 mt-2 align-bottom col-span-5">
					
					<!-- Notifications 
					<ion-icon class="rounded-full h-5 w-5 p-2" :icon="notifications" style="background-color: #F59E0B"/>-->
					
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

						<!-- BLOCKCHAIN CHECKED
				<div :class="{'bg-green-500':blockchain.valid, 'bg-red-500': !blockchain.valid}" 
            class="h-full rounded-md p-3 text-white text-xs font-bold" style="font-family:'Inter'">
            <ion-icon v-if="blockchain.valid" class="mr-1 text-xl" :icon="shieldCheckmark" />
            <ion-icon v-if="!blockchain.valid" class="mr-1 text-xl" :icon="close" />
            <span>Blockchain </span> 
            <span v-if="blockchain.valid">Valid</span>
            <span v-else>Tidak Valid</span>
            </div> 
						BLOCKCHAIN CHECKED -->

         </div>

	<!--	<div style="font-family:Inter">
				<ion-progress-bar v-if="showProgressBar" type="indeterminate"></ion-progress-bar>
			</div>
			<div class="h-20"></div>
		
		<div class="mx-4">
			<div	class="border-b border-gray-400 pb-3 mb-5"
				 	v-for="clinic in clinics" :key="clinic.clinicId"
		    	   @click="proceedToMakeToken(clinic)">
				<p class="font-bold text-sm">{{clinic.clinicName}}</p>
				<p class="text-sm mt-0 text-gray-600">{{clinic.clinicAddress}}</p>
		   </div>

		</div> -->
            
		</ion-content>
	</ion-page>
</template>

<script type="text/javascript">
	
	import { IonAvatar, IonPage, IonContent, IonIcon} from '@ionic/vue';
	import { medical, timer, book, notifications, shieldCheckmark, lockClosed, close} from 'ionicons/icons';
	import Tokenization from '@/components/Tokenization.vue';
	import MedRec from '@/components/MedicalRecord.vue';


	export default{
		components : {IonAvatar, IonPage, IonContent, IonIcon, Tokenization, MedRec},
		data(){
			return{
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
				],
				book,shieldCheckmark,notifications,
				user : {},
				blockchain : {
					valid : true
				}
			}
		},
		created(){
			var app = this;
			let loginCredential = localStorage.getItem('logged');
			setTimeout(function(){	
				if (loginCredential) {
					let data = localStorage.getItem(loginCredential); 
					app.user = JSON.parse(data);
				}
			}, 1000)
		}
	}
</script>