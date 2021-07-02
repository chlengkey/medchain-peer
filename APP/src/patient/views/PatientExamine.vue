<template>
	<div>

		<Modal ref="modal" width="3/12">
			<template v-slot:content>
				<p class="text-lg font-bold mb-1">Tambah Obat</p>
				<p class="text-sm text-gray-600 mb-2">Silahkan mengisi semua form dibawah</p>
				<label>Pilih Obat :</label>
				<select class="w-full p-2 border-b border-gray-300" required="true" v-model="drug.name">
					<option>Amoxilin</option>
					<option>Paracetamol</option>
					<option>CTM</option>
				</select>

				<label>Aturan Konsumsi :</label>
				<select class="w-full p-2 border-b border-gray-300" required="true" v-model="drug.dose">
					<option>3 x sehari</option>
					<option>2 x sehari</option>
					<option>1 x sehari</option>
				</select>

				<label>Aturan Konsumsi :</label>
				<textarea class="w-full p-2 border-b border-gray-300" placeholder="Contoh: Pasien mengalami penyakit sesak nafas" required="true" v-model="drug.notes"></textarea>

			</template>

			<template v-slot:button>
				<button @click="addDrug()" class="orange-button col-span-2 ml-2">
					<span>Tambah</span>
				</button>
			</template>
		</Modal>

	<form class="shadow-lg mt-3 mb-10" @submit.prevent="create()">

		<p class="text-2xl text-gray-800 font-bold mt-2 mb-0.5">Form Pemeriksaan Dokter</p>
		<span class="text-gray-400 text-sm"><span class="text-red-600">*</span> Masukan data pemeriksaan disini</span>
		<hr class="mt-4" />
		<div class="grid grid-cols-2 gap-x-10 gap-y-4">
			<div>
				<label>Nama Dokter :</label>
				<input class="w-full p-2 border-b border-gray-300" required="true" v-model="anamnesis.doctor" disabled type="text">
			</div>
			<div>
				<label>Nama Layanan Kesehatan :</label>
<!-- 			<select class="w-full p-2 border-b border-gray-300" required="true" v-model="anamnesis.facility" type="text">
					<option>Puskesmas Tomohon</option>
					<option>Klinik Dokter Cleyra</option>
					<option>Puskesmas Wenang</option>
				</select> -->
				 <input class="w-full p-2 border-b border-gray-300" required="true" v-model="anamnesis.facility" disabled type="text"> 
			</div>
		</div>

		<section>

			<!-- Keluhan (Complaint) -->
			<label>Keluhan Pasien :</label>
			<textarea class="w-full p-2 border-b border-gray-300" placeholder="Contoh: Pasien mengalami penyakit sesak nafas" required="true" v-model="anamnesis.complaint"></textarea>

			<!-- Diagnosa (Diagnosis) -->
			<label>Hasil Pemeriksaan :</label>
			<textarea required="true" class="w-full p-2 border-b border-gray-300" placeholder="Contoh: Pasien diduga menderita flu berat" v-model="anamnesis.diagnosis"></textarea>

			<!-- Obat (Drugs) -->
			<label @click="$refs.modal.openModal()">Obat yang Diberikan :</label>
			<div @click="$refs.modal.openModal()" class="w-full border rounded border-gray-300 p-4 mt-2">
				<input type="hidden" v-model="anamnesis.drugs">
				<p class="text-sm text-gray-600" v-if="drugs == 0">Silahkan menambahkan obat disini</p>
				<span v-for="drug_ in drugs" v-else class="relative mr-2 rounded-full bg-yellow-100 text-yellow-700 py-2 px-4 font-semibold pr-5 cursor-pointer">{{drug_.name}} | {{drug_.dose}}
					<b class="absolute top-0 -mt-3 rounded-full text-red-500 cursor-pointer">x</b>
				</span>
			</div>
		</section>

		<p v-if="!readonly" @click="create()" class="mt-5 text-center yellow-glow-button">Simpan</p>
		
	</form>
	</div>
</template>

<script type="text/javascript">
	
	import Anamnesis from "../models/Anamnesis.js";
	import Drug from "../models/Drug.js";
	import Modal from "@/components/Modal.vue"

	export default{
		components :{ 
			Modal
		},
		props :{
			anamnesis : {
				type: Object,
				default : new Anamnesis()
			},
			readonly : {
				type : Boolean,
				default : false
			}, 
		},
		data(){
			return{
				submitButtonState : true,
				drug : new Drug(),
				drugs : []
			}
		},
		methods : {
			
			create(){
				if (!this.readonly) {
					this.$emit('on-submit')	
				}
			},

			addDrug() {
				var app = this;
				let exists = false;
				if(this.drug.name == "" || this.drug.dose == "" || this.drug.notes == ""){
					alert("Anda harus melengkapi semua data obat!");
					return;
				}
				this.drugs.forEach(function(value, i){
					if(value.name == app.drug.name){
						app.drugs[i] = app.drug;
						exists = true;
					}
				});
				if(!exists){
					app.drugs.push(
						{	
							name : app.drug.name, 
							dose : app.drug.dose, 
							notes : app.drug.notes
						});
				}
				app.drug = new Drug();
				app.anamnesis.drugs = app.load_as_text(app.drugs);
				app.$refs.modal.closeModal();
			},

			removeDrug(drug_name){
				
			},

			loadDrugs(arr){
				if(arr != ""){
					arr = arr.split(",");
					let drugs = []
					arr.forEach(element => {
						element = element.split("-");
						drugs.push({
							name : element[0],
							dose : element[1],
							notes : element[2]
						})
					});
					this.drugs = drugs;
				}
			},

			load_as_text(text){
				let data = []
				text.forEach(element => {
					let arr = element.name + "-" + element.dose + "-" + element.notes;
					data.push(arr);
				})
				return data.join(",");
			}
		},

		created(){
			var app = this;
			console.log(app.anamnesis.drugs)
			app.loadDrugs(app.anamnesis.drugs);
		}
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

    form {
        background: white;
        text-align: left;
        padding: 30px;
        border-radius: 8px;
    }

    label {
        color: #aaa;
        display: inline-block;
        margin: 20px 0 0 5px;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }

</style>