<template>
    <div class="mx-10">
        <div class="flex my-1">
            <div class="bg-blue-500 rounded-md shadow-lg mt-8 w-7/12">

                <!-- Avatar dan Nama Pasien -->
                <div class="flex p-3 mx-3 items-center mt-1">
                    <avatar :fullname="patient.name" size="60"></avatar>
                    <div class="pl-3">
                        <h2 class="text-xl text-white font-semibold -mb-1">{{patient.name}}</h2>
                        <p class="text-l text-white mt-0">{{user.umur}}</p>
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
                        <p class="mt-2 text-sm leading-4 text-sm text-gray-700">{{user.penyakit}}</p>
                    </div>
                </div>

                <div class="px-5 mt-1 flex mx-3 items-center grid grid-cols-2 gap-10">
                    <div class="">
                        <p class="text-sm leading-4 text-base font-bold text-gray-700">Alergi Obat</p>
                        <p class="mt-2 text-sm leading-4 text-sm text-gray-700">{{user.alergi_obat}}</p>
                    </div>
                    <div>
                        <p class="text-sm leading-4 text-base font-bold text-gray-700">Alergi Makanan</p>
                        <p class="mt-2 text-sm leading-4 text-sm text-gray-700">{{user.alergi_makanan}}</p>
                    </div>
                </div>

            </div>
        </div>

        <!-- Form Anamnesis -->
        <form class="shadow-lg mt-3 mb-10" @submit.prevent="create()">
            <p class="text-2xl text-gray-800 font-bold mt-2 mb-0.5">Form Pemeriksaan Dokter</p>
            <span class="text-gray-400 text-sm"><span class="text-red-600">*</span> Masukan data pemeriksaan disini</span>
            <hr class="mt-4" />
            <div class="grid grid-cols-2 gap-x-10 gap-y-4">
                <div>
                   <label>Nama Dokter :</label>
                   <p class="w-full p-2 border-b border-fuchsia-600 border-gray-500">
                        {{pemeriksaan.nama_dokter}}</p>
                </div>
                <div>
                   <label>Nama Layanan Kesehatan :</label>
                   <p class="w-full p-2 border-b-2 border-fuchsia-600 border-gray-500">
                        {{pemeriksaan.layanan_kesehatan}}</p>
                </div>
			</div>
            <div>

                <!-- Keluhan (Complaint) -->
                <label class="pt-4">Keluhan Pasien :</label>
                <textarea class="w-full p-2 border-b border-gray-300" placeholder="Contoh: Pasien mengalami penyakit sesak nafas" required="true" v-model="anamnesis.complaint"></textarea>

                <!-- Diagnosa (Diagnosis) -->
                <label class="pt-4 ">Hasil Pemeriksaan :</label>
                <textarea required="true" class="w-full p-2 border-b border-gray-300" placeholder="Contoh: Pasien diduga menderita flu berat" v-model="anamnesis.diagnosis"></textarea>

                <!-- Obat (Drugs) -->
                <label class="pt-4">Obat yang Diberikan :</label>
                <input required="true" placeholder="contoh: Paracetamol, CTM, Vit.B" class="w-full p-2 border-b border-gray-300" type="text" v-model="anamnesis.drugs" id="obat">
            </div>
            <p @click="create()" class="mt-5 text-center yellow-glow-button">Simpan</p>
        </form>
	</div>
</template>

<script>

// API
const DEFAULT_URL = "http://127.0.0.1:5000"
const axios = require('axios')

// RSA
const NodeRSA = require('node-rsa');
const key = new NodeRSA({b: 1024});

// UI Component
const Swal = require('sweetalert2')
import Avatar from 'vue-avatar-component'

export default {
    data(){
        return {
            anamnesis : {
                complaint : "",
                diagnosis : "",
                drugs : "",
                doctor : "Cleyra Lovelace",
                facility : "Puskesmas Tomohon"
            },

            patient : {
                id : "",
                name : "User Name",
                gender : "",
                weight : "10",
                height : "10",
                blood_type : "A+",
                allergy : ""
            },

            pemeriksaan : {
                nama_dokter : "Cleyra Lovelace",
                layanan_kesehatan : "RS. Tomohon",
                hasil_pemeriksaan : "",
                obat : ""
            },

            user : {
                username : "Chrisdityra Lengkey",
        		umur  : "20 tahun",
        		berat_badan : "58 kg",
                tinggi_badan : "169 cm",
                golongan_darah : "A+",
                penyakit : "Amandel dan Maag",
                alergi_obat : "Asam Mefenamat",
                alergi_makanan : "Kacang Tanah"
            }
        }
    },
    components: {Avatar},
    methods : {

        // Fungsi untuk menambahkan data baru
        create : function(){

            // Mengenkripsi data pasien dan data pemeriksaan
            const app = this;
            let encoded_patient = app.encode(app.patient);
            let encoded_anamnesis = app.encode(app.anamnesis);

            // Mengirim data ke Server
            axios.post(DEFAULT_URL + "/data/create", {
                "patient_id" : app.patient.id, 
                "patient" : encoded_patient,
                "anamnesis" : encoded_anamnesis
            }).then(response => {
                console.log(response.data);
            }).catch(error => {
                console.log(error);
            })

        },

        // Fungsi untuk mengambil data token
        get : function(){

            Swal.fire({
                icon : "warning",
                title : "Mohon Tunggu",
                text : "Sedang mengambil data dari blockchain..",
                allowOutsideClick: false,
                showConfirmButton: false,
                timerProgressBar: true,
                didOpen: () => {
                    Swal.showLoading()
                },
            });

            const app = this;
            setTimeout(function(){
                axios.get(DEFAULT_URL + "/token/" + app.$route.params.token)
                    .then(response => {
                        key.importKey(response.data.publicKey, "pkcs1-public-pem");
                        app.patient = response.data.patient;
                        Swal.close();
                    })
                    .catch(error => {
                        Swal.fire({
                            icon : "error",
                            title : "Terjadi kesalahan",
                            text : "Gagal saat mengambil data, silahkan cek koneksi internet anda"
                        })
                    })
            }, 2000);
        },

        // Fungsi untuk mengenkripsi data
        encode : function(data){
            let data_keys = Object.keys(data);
            let index = 0;

            let encoded_data = {}
            for(index; index < data_keys.length; index++){
                let data_key = data_keys[index];
                let encode_key_data = String(data[data_key]);
                if(data_key != "id"){
                    encode_key_data = key.encrypt(encode_key_data, "base64")
                }
                encoded_data[data_key] = encode_key_data;
            }
            console.log(encoded_data);
            return encoded_data;}
    },

    created(){
        this.get();
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
