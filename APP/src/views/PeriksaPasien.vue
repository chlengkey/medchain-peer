<template>
    <div class="mx-10">
        <!-- Timer -->
        <div class="bg-red-600 px-3 py-3 rounded-b">
            <span class="text-red-50"><b class="bg-red-100 px-2 py-1 rounded text-red-600 mr-1.5">{{timer}}</b> Sebelum sesi pemeriksaan anda berakhir</span>    
        </div>
        <PatientProfile :patient="patient" />

        <p class="my-2 text-red-400 italic text-sm">* Silahkan Menambahkan atau Mengubah data Diri Pasien diatas sesuai Hasil Pemeriksaan</p>

        <PatientExamine :anamnesis="anamnesis" @on-submit="create()"/>
        <PatientHistory :record="record" />
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
    const Swal = require('sweetalert2');

    // Classes
    import Anamnesis from '@/patient/models/Anamnesis.js'
    import Patient from '@/patient/models/Patient.js'

    // Views
    import PatientProfile from '@/patient/views/PatientProfile.vue'
    import PatientExamine from '@/patient/views/PatientExamine.vue'
    import PatientHistory from '@/patient/views/PatientHistory.vue'

    export default {
        data(){
            return {
                timer : "-",
                anamnesis : new Anamnesis(),
                patient : new Patient(),
                record : []
            }
        },
        components: {PatientHistory, PatientProfile, PatientExamine},
        methods : {

            // Fungsi untuk menambahkan data baru
            create : function(){

                if(this.anamnesis.complaint != "",
                   this.anamnesis.diagnosis != ""){

                    // Mengenkripsi data pasien dan data pemeriksaan
                    const app = this;
                    let encoded_patient = app.encode(app.patient);
                    let encoded_anamnesis = app.encode(app.anamnesis);
                    
                    // Memulai Loading
                    Swal.fire({
                        icon : "info",
                        title : "Mohon Tunggu",
                        text : "Sedang mengirim data ke blockchain..",
                        allowOutsideClick: false,
                        showConfirmButton: false,
                        timerProgressBar: true,
                        didOpen: () => {
                            Swal.showLoading()
                        },
                    });

                    // Mengirim data ke Blockchain
                    axios.post(DEFAULT_URL + "/data/create", {
                        "patient_id" : app.patient.id, 
                        "patient" : encoded_patient,
                        "anamnesis" : encoded_anamnesis
                    }).then(response => {
                        if (response.data.success) {
                            setTimeout(function(){
                                app.swal_error("CREATE_DATA_SUCCESS");
                                app.$router.replace("/");
                            }, 2000);
                        }
                    }).catch(error => {
                        app.swal_error("INTERNAL_SERVER_ERROR");
                    })
                    return;
                }
                app.swal_error("FORM_EMPTY");
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
                            if(response.data.success){
                                // Memasukan key untuk proses enkripsi
                                key.importKey(response.data.publicKey, "pkcs1-public-pem");
                                // Mengambil data pasien
                                app.patient = response.data.patient;
                                app.record = response.data.record;
                                // Memulai timer
                                app.start_timer();
                                Swal.close();
                            }
                            else if(!response.data.success){
                                Swal.fire(response.data.code, response.data.msg, "error");
                            }
                        })
                        .catch(error => {
                            app.swal_error("INTERNAL_SERVER_ERROR");
                        })
                }, 2000);
            },

            // Fungsi untuk mengatur timer
            start_timer : function(){
                var app = this;
                var timeNow = new Date().getTime();
                var timer = setInterval(function(){
                    var countdown = new Date().getTime();
                    var distance = (timeNow + 3600000) - countdown;
                    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    if(minutes < 10){ minutes = "0" + minutes; }
                    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                    if(seconds < 10){ seconds = "0" + seconds; }
                    app.timer = minutes + " : " + seconds;

                    if(seconds <= 0 && minutes <= 0){
                        clearInterval(timer);
                        app.$router.replace("/");
                        Swal.fire("Waktu Habis", "Waktu pemeriksaan anda habis, anda tidak bisa lagi melihat riwayat medis pasien", "error");
                    }
                }, 1000);},

            // Fungsi untuk menampilkan error
            swal_error : function(code){
                
                if(code == "FORM_EMPTY"){
                    Swal.fire("Proses Gagal", "Semua form harus diisi", "error");
                }

                else if(code == "INTERNAL_SERVER_ERROR"){
                    Swal.fire("Proses Gagal", "Terjadi kesalahan, silahkan periksa koneksi anda", "danger");
                }

                else if(code == "CREATE_DATA_SUCCESS"){
                    Swal.fire("Proses Berhasil", "Data berhasil ditambahkan, silahkan menunggu proses mining agar data dapat disimpan secara permanen..", "success");
                }},

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
            this.anamnesis.doctor = "Cleyra Lovelace";
            this.anamnesis.facility = "Puskesmas Tomohon";
            this.get();
        }

}
</script>
