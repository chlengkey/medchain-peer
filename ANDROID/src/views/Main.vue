<template>
	<ion-page>
		<ion-content :fullscreen="true">

			<div class="px-5 pt-6">
				<img src="../assets/85418.svg" style="opacity:0.08;top:0;left:0;z-index:-1" class="opacity-5 w-full absolute z-0 mt-2 align-bottom col-span-5" >

				<!-- Content Header -->
				<div class="grid grid-cols-6 mb-5">
					<img src="../assets/logo.png" class="w-32 mt-2 align-bottom col-span-5">
					<div class="relative">
						<div class="absolute right-0">
							<div class=" w-10 h-10 bg-black rounded-fulltext-transparent">t</div>
						</div>
					</div>
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
				<div class="border border-red-500 h-full rounded-md p-3 text-red-500 text-xs font-bold" style="font-family:'Inter'"><ion-icon class="mr-1" :icon="book" />
					<br/>Medis<br/><span class="font-normal">Lihat seluruh blok rekam medis anda</span>
				</div>
				<Tokenization ref="tokenization"></Tokenization>
				<div :class="{'bg-green-500':blockchain.valid, 'bg-red-500': !blockchain.valid}" 
             		 class="h-full rounded-md p-3 text-white text-xs font-bold" style="font-family:'Inter'">
             		 <ion-icon v-if="blockchain.valid" class="mr-1 text-xl" :icon="shieldCheckmark" />
             		 <ion-icon v-if="!blockchain.valid" class="mr-1 text-xl" :icon="close" />
             		 <span>Blockchain </span> 
             		 <span v-if="blockchain.valid">Valid</span>
             		 <span v-else>Tidak Valid</span>
             	</div>
            </div>
            <hr class="border-4 my-4" />
            
		</ion-content>
	</ion-page>
</template>

<script type="text/javascript">
	
	import { IonPage, IonContent, IonIcon} from '@ionic/vue';
	import { medical, timer, book, shieldCheckmark, lockClosed, close} from 'ionicons/icons';
	import Tokenization from '@/components/Tokenization.vue';


	export default{
		components : {IonPage, IonContent, IonIcon, Tokenization},
		data(){
			return{
				book,shieldCheckmark,
				user : {},
				blockchain : {
					valid : true
				}
			}
		},
		created(){
			let loginCredential = localStorage.getItem('logged');
			if (loginCredential) {
				let data = localStorage.getItem(loginCredential); 
				this.user = JSON.parse(data);
			}
		}
	}
</script>