<template>
	<div class="flex my-1">

		<!-- Profil Dasar Pasien -->
		<div class="bg-blue-500 rounded-md shadow-lg mt-5 w-7/12">
			
			<!-- Avatar dan Nama Pasien -->
			<div class="flex p-3 mx-3 items-center mt-1">
				<avatar :fullname="patient.name" size="60"></avatar>
				<div class="pl-3">
					<h2 class="text-xl text-white font-semibold -mb-1">{{patient.name}}</h2>
					<p class="text-l text-white mt-0">-</p>
				</div>
			</div>

			<!-- Kondisi Pasien -->
			<div class="grid grid-cols-3 mx-6 mt-1">
				<div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Berat Badan (Kg)</p>
					<input type="text" class="bg-transparent text-white" v-model="patient.weight">
				</div>
				<div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Tinggi Badan (Cm)</p>
					<input type="text" class="bg-transparent text-white" v-model="patient.height">
				</div>
				<div>
					<p class="mb-1.5 text-sm leading-4 text-base font-bold text-white">Golongan Darah</p>
					<input type="text" class="bg-transparent text-white" v-model="patient.blood_type">
				</div>
			</div>
		</div>

		<div class="grid grid-rows-2 px-5 bg-white rounded-lg shadow-xl mt-8 w-5/12">
			<div class="flex p-5 items-center">
				<div class="mx-3">
					<p class="text-sm leading-4 text-base font-bold text-gray-700">Penyakit</p>
					<p class="mt-2 text-sm leading-4 text-sm text-gray-700">-</p>
				</div>
			</div>

			<div class="px-5 mt-1 flex mx-3 items-center grid grid-cols-2 gap-10">
				<div>
					<p class="text-sm leading-4 text-base font-bold text-gray-700">Alergi Obat</p>
					<p class="mt-2 text-sm leading-4 text-sm text-gray-700">-</p>
				</div>
				<div>
					<p class="text-sm leading-4 text-base font-bold text-gray-700">Alergi Makanan</p>
					<p class="mt-2 text-sm leading-4 text-sm text-gray-700">-</p>
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