<template>
	<form class="shadow-lg mt-3 mb-10" @submit.prevent="create()">
		<p class="text-2xl text-gray-800 font-bold mt-2 mb-0.5">Form Pemeriksaan Dokter</p>
		<span class="text-gray-400 text-sm"><span class="text-red-600">*</span> Masukan data pemeriksaan disini</span>
		<hr class="mt-4" />
		<div class="grid grid-cols-2 gap-x-10 gap-y-4">
			<div>
				<label>Nama Dokter :</label>
				<input class="w-full p-2 border-b border-gray-300" placeholder="Contoh. Cleyra Lovelace" required="true" v-model="anamnesis.doctor" disabled type="text">
			</div>
			<div>
				<label>Nama Layanan Kesehatan :</label>
				<input class="w-full p-2 border-b border-gray-300" placeholder="Contoh. Puskesmas Tomohon" required="true" v-model="anamnesis.facility" disabled type="text">
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
			<label>Obat yang Diberikan :</label>
			<input required="true" placeholder="contoh: Paracetamol, CTM, Vit.B" class="w-full p-2 border-b border-gray-300" type="text" v-model="anamnesis.drugs" id="obat">
		</section>
		<p v-if="!readonly" @click="create()" class="mt-5 text-center yellow-glow-button">Simpan</p>
	</form>
</template>

<script type="text/javascript">
	
	import Anamnesis from "../models/Anamnesis.js";

	export default{
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
				submitButtonState : true
			}
		},
		methods : {
			create(){
				if (!this.readonly) {
					this.$emit('on-submit')	
				}
			}
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