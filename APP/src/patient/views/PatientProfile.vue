<template>
	<div class="flex my-1">

		<!-- Profil Dasar Pasien -->
		<div class="bg-blue-500 rounded-md shadow-lg mt-5 w-7/12">
			
			<!-- Avatar dan Nama Pasien -->
			<div class="flex p-3 mx-3 items-center mt-1">
				<avatar :fullname="patient.name" size="60"></avatar>
				<div class="pl-3">
					<h2 class="text-xl text-white font-semibold -mb-1">{{patient.name}}</h2>
					<!-- <p class="text-l text-white mt-0">{{patient.gender}}</p> -->
				</div>
			</div>

			<!-- Kondisi Pasien -->
			<div class="mr-2 grid grid-cols-3 mx-6 mt-5">

				<!-- <div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Berat Badan (Kg)</p>
					<input type="number" class="bg-transparent text-white w-2/3 border-b border-gray-300" v-model="patient.weight">
				</div> 
				
				<div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Tinggi Badan (Cm)</p>
					<input type="text" class="bg-transparent text-white w-2/3 border-b border-gray-300" v-model="patient.height">
				</div>
				
				<div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Golongan Darah</p>
					<input type="text" class="bg-transparent text-white w-2/3 border-b border-gray-300" v-model="patient.blood_type">
				</div>
				-->

				<div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Berat Badan</p>
					<input placeholder= "Mis. 50 kg" class=" px-1 py-1 w-2/3 border-b bg-transparent text-white" required="true" v-model="patient.weight" type="number">
				</div>

				<div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Tinggi Badan</p>
					<input placeholder= "Mis. 170 cm" class=" px-1 py-1 w-2/3 border-b bg-transparent text-white" required="true" v-model="patient.height" type="number">
				</div>
				
				<div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Golongan Darah</p>
					<select class="py-1 px-1 mt-1 w-2/3 border-b bg-blue-500 text-white" required="true" v-model="patient.blood_type" type="text">
						<option selected="selected" value="" disabled="true">Pilih Gol.Darah</option>
						<option>A</option>
						<option>B</option>
						<option>AB</option>
						<option>O</option>
					</select>

					<!--<input class="w-2/3 border-b bg-transparent text-white" required="true" v-model="patient.blood_type" type="text"> -->

				</div>
			</div>
		</div>

		<div class="grid grid-rows-2 px-5 bg-white rounded-lg shadow-xl mt-8 w-5/12">
			
			<div class="flex p-5 items-center">
				<div class="mx-3">
					<p class="text-sm leading-4 text-base font-bold text-gray-700">Penyakit</p>
					<input class="mt-1 w-3/4 border-b bg-transparent text-black" required="true" v-model="patient.anamnesis" type="text">
					<!-- <p class="mt-2 text-sm leading-4 text-sm text-gray-700">-</p>-->
				</div>
			</div>

			<div class="px-5 mb-2 flex mx-3 items-center grid grid-cols-2 gap-10">
				<div>
					<p class="text-sm leading-4 text-base font-bold text-gray-700">Alergi Obat</p>
					<input class="mt-2 w-3/4 border-b bg-transparent text-blaxk" required="true" v-model="patient.drugs_allergy" type="text">
					<!-- <p class="mt-2 text-sm leading-4 text-sm text-gray-700">-</p>-->
				</div>
				<div>
					<p class="text-sm leading-4 text-base font-bold text-gray-700">Alergi Makanan</p>
					<input class="mt-2 w-3/4 border-b bg-transparent text-black" required="true" v-model="patient.allergy" type="text">
					<!-- <p class="mt-2 text-sm leading-4 text-sm text-gray-700">-</p>-->
				</div>
			</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	
	import Avatar from 'vue-avatar-component'
	import Patient from '@/patient/models/Patient.js'

	export default{
		props : {
			patient : {
				type : Object,
				default : new Patient()
			}
		},
		components : {Avatar}
	}
</script>

<style scoped>
	input::-webkit-outer-spin-button,
        input::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
  
        input[type=number] {
            -moz-appearance: textfield;
        }
	
	::placeholder { 
		color: white;
		font-size: 12px;
		opacity: 0.8;
	}

	option {
		color: white;
		font-size: 12px;
		opacity: 0.8; 
	}

</style>