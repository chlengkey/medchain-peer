<template>
  <ion-page>

    <!-- content -->
    <ion-content :fullscreen="true">

      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 1</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <div class="px-5 pt-6">
        <img src="../assets/85418.svg" style="opacity:0.08;top:0;left:0;z-index:-1" class="opacity-5 w-full absolute z-0 mt-2 align-bottom col-span-5" >
        
        <!-- content header -->
        <div class="grid grid-cols-6 mb-5">
          <img src="../assets/logo.png" class="w-32 mt-2 align-bottom col-span-5">
          <div class="relative">
            <div class="absolute right-0">
              <div class=" w-10 h-10 bg-black rounded-fulltext-transparent">t</div>
            </div>
          </div>
        </div>

        <div class="my-16" style="font-family:Inter">
          <p class="text-xl text-center font-semibold">Hi, {{profile.name.split(" ")[0]}}</p>
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

      <!-- button group -->
      <div class="grid px-5 grid-cols-3 gap-2">
        <div class="border border-red-500 h-full rounded-md p-3 text-red-500 text-xs font-bold" style="font-family:'Inter'"><ion-icon class="mr-1" :icon="book" />
          <br/>Medis<br/><span class="font-normal">Lihat seluruh blok rekam medis anda</span>
        </div>
        <div>
          <Tokenization ref="tokenization"/>
        </div>
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

      <div class="mt-5" style="font-family:Inter">
        <p class="px-5 font-bold text-lg text-gray-800">Riwayat Medis</p>
       
        <div class="px-5">
          <div v-if="record.length > 0">
            <div v-for="data in record" :key="data.hash">
              <p class="text-xs text-gray-600 mt-2">{{data.tanggal}}</p>
              <p class="text-sm mt-1 mb-1">{{data.pasien_nama}}</p>
              <p class="mb-3">{{data.pasien_keluhan}}</p>
              <hr>
            </div>
          </div>
          <div v-else class="flex w-full bg-gray-200 pl-2 relative mt-3 dark:bg-gray-800">
            <img src="../assets/no_data.png" class="w-16">
            <div class="relative w-full">
              <div class="text-xs ml-2" style="font-family:Inter;position:absolute;top:50%;transform:translateY(-50%)">
                <p class="font-bold">Oops</p>
                <p>Anda belum memiliki riwayat medis</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent} from '@ionic/vue';
import { medical, timer, book, shieldCheckmark, lockClosed, close} from 'ionicons/icons';
import Tokenization from '@/components/Tokenization.vue';

export default  {
  name: 'Tab1',
  components: {IonHeader, IonToolbar, IonTitle, IonContent, IonPage, Tokenization},
  data(){
    return{
      user : 'tes',
      profile : {
        name : "Chrisdityra Lengkey"
      },
      blockchain : {
        valid : 1
      },

      // ionicons
      medical,
      close,
      shieldCheckmark,
      lockClosed,
      book,
      timer,

      record  : [
        {
          "hash" : "98913n1jnjbugdsug2323",
          "tanggal" : "19-05-2021",
          "pasien_nama" : "Chrisdityra Lengkey",
          "pasien_keluhan" : "Sakit pinggang dan  perut"
        }
      ],
      values : "2008-09-02"
    }
  },
  methods : {
    tes : function(){
      const app = this;
      console.log(this.user);
    }
  },

  created(){
    this.tes();
    /*let loginCredential = localStorage.getItem('logged');
    if (loginCredential) {
      let data = localStorage.getItem('47deb444a873b5bb877c35196a56c086'); 
      this.profile = "user";
    }
    this.profile = "user";*/
  },
}
</script>