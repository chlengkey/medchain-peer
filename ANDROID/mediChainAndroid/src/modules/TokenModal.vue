<template>
  <ion-header>
    <ion-toolbar>
      <ion-title>Buat Token</ion-title>
    </ion-toolbar>
  </ion-header>
  <ion-progress-bar type="indeterminate"></ion-progress-bar>
  <ion-content class="ion-padding">
    <p @click="dismiss()">Close</p>
    <div>
    	<div class="border-b border-gray-400 pb-3" v-for="clinic in clinics">
    		<p class="font-bold">{{clinic.clinicName}}</p>
    		<p class="text-sm mt-0 text-gray-600">{{clinic.clinicAddress}}</p>
    	</div>
    </div>
  </ion-content>
</template>

<script type="text/javascript">
	
	import { modalController, alertController, IonProgressBar} from '@ionic/vue';

	export default{
		name : "Generate Token",
		data(){
			return{	
				clinics : [
					{
						clinicName    : "Puskesmas Tomohon",
						clinicAddress : "Jl. Raya Manado Tomohon",
						clinicId      : "KEYYY" 
					}
				]
			}
		},
		methods : {
			dismiss : function(){
				modalController.dismiss();
			}
		}
	}
</script>