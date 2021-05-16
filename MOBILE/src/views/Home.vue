<template>
  <div class="home">
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

        <div class="my-16" style="z-index:99">
          <p class="text-xl text-center font-semibold">Hi, {{profile.name.split(" ")[0]}}</p>
          <p class="text-sm text-center text-gray-500 mb-4">Ada yang bisa kami bantu untuk anda?</p>
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

      </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data(){
    return{


      profile : {
        name : "Chrisdityra Lengkey"
      },

      blockchain : {
        valid : 1
      },

      record  : [
        /*{
          "hash" : "98913n1jnjbugdsug2323",
          "tanggal" : "19-05-2021",
          "pasien_nama" : "Chrisdityra Lengkey",
          "pasien_keluhan" : "Sakit pinggang dan  perut"
        }*/
      ],
      values : "2008-09-02"
    }
}
}
</script>
