<template>
	<div>
		
		<Modal ref="modal" width="10/12">
			<template v-slot:content>
				<PatientProfile :patient="patient" readonly="true"/>
				<PatientExamine :anamnesis="anamnesis" readonly="true"/>
			</template>
		</Modal>

		<p class="text-2xl text-gray-800 font-bold mt-2 mb-0.5">Riwayat Pemeriksaan Pasien</p>
            <span class="text-gray-400 text-sm">Hasil pemeriksaan dapat dilihat disini</span>

		<div class="relative text-gray-600 focus-within:text-gray-400 mt-2">
			<span class="absolute inset-y-0 left-0 flex items-center pl-2">
				<button type="submit" class="p-1 focus:outline-none focus:shadow-outline"><Search/>
				</button>
			</span>
			
			<input type="search" name="pencarian" class="py-1 text-sm text-white bg-gray-900 w-5/6 h-8 rounded-md pl-10 focus:outline-none focus:bg-white focus:text-gray-900" placeholder="Mencari Pemeriksaan..." autocomplete="off">
		</div>

		<table class="overflow-x-auto w-full text-md bg-white rounded mb-20 mt-4">
			<thead>
				<tr class="text-xs text-gray-500 bg-gray-50 border-t border-b border-gray-200 rounded">
					<td class="text-left p-3 px-6 font-semibold">TANGGAL</td>
					<td class="text-left p-3 px-6 font-semibold">FASILITAS KESEHATAN</td>
					<td class="text-left p-3 px-6 font-semibold">DIAGNOSA</td>
					<td class="text-left p-3 px-6 font-semibold">OBAT</td>
					<td class="text-left p-3 px-6 font-semibold">AKSI</td>
				</tr>
			</thead>
			<tbody v-if="record.length > 0">
				<tr v-for="record_data in record" class="transition border-b border-gray-200 pointer text-sm font-semibold text-gray-800">

					<td class="p-3 px-6 py-3">
						<span v-if="record_data.anamnesis.date_time">{{record_data.anamnesis.date_time}}</span>
						<span v-else>05-10-2021</span>
					</td>

					<!-- Nama Fasilitas Kesehatan -->
					<td class="p-3 px-6 py-3">
						<span v-if="record_data.anamnesis.facility">{{record_data.anamnesis.facility}}</span>
						<span v-else>-</span>
					</td>
					
					<!-- Diagnosa -->
					<td class="p-3 px-6 py-3">
						<span v-if="record_data.anamnesis.diagnosis">{{record_data.anamnesis.diagnosis}}</span>
						<span v-else>-</span>
					</td>

					<!-- Obat -->
					<td class="p-3 px-6 py-3">
						<span v-if="record_data.anamnesis.drugs">
						{{record_data.anamnesis.drugs}}</span>
						<span v-else>-</span>
					</td>

					<td class="px-6">
						<InformationCircle class="transition hover:text-blue-600 cursor-pointer" @click="openModal(record_data)"/>
					</td>
				</tr>				
			</tbody>
			<p v-else class="bg-yellow-50 rounded-lg mt-1 text-yellow-600 font-semibold text-sm px-6 py-3">Pasien belum punya data riwayat</p> 
		</table>
	</div>
</template>

<script type="text/javascript">
	
	import InformationCircle from '@/assets/icons/informationCircle.vue'
	import Search from '@/assets/icons/search.vue'
	import Modal from '@/components/Modal.vue'
	import PatientExamine from '@/patient/views/PatientExamine.vue'
	import PatientProfile from '@/patient/views/PatientProfile.vue'

	export default{
		components : {InformationCircle, Search, Modal, PatientProfile, PatientExamine},
		props : {
			record : {
				type : Array,
				default : []
			}
		}, 
		data(){
			return{
				patient : {},
				anamnesis : {}
			}
		},
		methods : {
			openModal(record_data){
				this.patient = record_data.patient;
				this.anamnesis = record_data.anamnesis;
				this.$refs.modal.openModal();
			}
		}
	}
</script>