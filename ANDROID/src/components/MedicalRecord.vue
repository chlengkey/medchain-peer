<template>
   
   <div @click="showModal()"
		class="border border-red-500 h-full rounded-md p-3 text-red-500 text-xs font-bold" style="font-family:'Inter'">
		<ion-icon class="mr-1" :icon="book" />
		<br/>Medis<br/><span class="font-normal">Lihat seluruh blok rekam medis anda</span>
   </div>

</template>

<script type="text/javascript">

import MedicalModal from '@/modules/MedicalModal.vue';
import { modalController, IonIcon } from '@ionic/vue';

import { book } from 'ionicons/icons';

export default {
   components : {IonIcon},
		data(){
			return{
            medicalData : [
					{
						medrec_tanggal : "19/05/2019",
						medrec_dokter : "Cleyra Lovelace",
						medrec_klinik : "Puskesmas Tomohon"
					}
				],

            book
         }
      },
   
   methods : {
      showModal: async function(){
				const modal = await modalController.create({
					component: MedicalModal,
				})
				await modal.present()
			},
   },

      
}
</script>
