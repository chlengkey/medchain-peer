<template>
	<div class="mx-10 mt-4">
		<div class="flex">
			<div class="w-2/3">
				<h2 class="text-lg font-bold">Pengaturan Blockchain</h2>
				<p class="mb-4 text-sm" :disabled="mining_status.code == 'MINING_NOT_NEEDED'" :class="get_class()">{{mining_status.msg}}</p>
			</div>
			<div class="mt-2">
				<button class="blue-glow-button mr-2" @click="get_blockchain()">Segarkan Data</button>
				<button class="green-glow-button" @click="start_mining()">Lakukan Mining</button>
			</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	
	const axios = require('axios');
	const default_endpoint = "/block/mine"
	const Swal = require('sweetalert2');

	export default{
		data(){
			return{
				mining_status : {}
			}
		},
		methods : {
			
			get_blockchain(){
				var app = this;

				// Memulai Loading
                Swal.fire({
                    icon : "info",
                    title : "Mohon Tunggu",
                    text : "Sedang mengambil data dari blockchain..",
                    allowOutsideClick: false,
                    showConfirmButton: false,
                    timerProgressBar: true,
                    didOpen: () => {
                        Swal.showLoading()
                    },
                });
				axios.get("http://127.0.0.1:5000" + default_endpoint)
					 .then(response => {
					 	app.mining_status = response.data
					 	Swal.close()
					 })
					 .catch(error => {
					 	Swal.fire("error", "error", "error")
					 })
			},

			start_mining(){
				var app = this;
				
				if(this.mining_status.code == "MINING_NOT_NEEDED"){
					return;
				}

				// Memulai Loading
				Swal.fire({
					icon : "info",
					title : "Mohon Tunggu, Mining sedang dilakukan..",
					text : "Proses ini dapat berjalan selama 3 - 5 menit",
                    allowOutsideClick: false,
                    showConfirmButton: false,
                    timerProgressBar: true,
                    didOpen: () => {
                        Swal.showLoading()
                    },
                });

				axios.post("http://127.0.0.1:5000" + default_endpoint)
					 .then(response => {
					 	Swal.fire("Berhasil", "Data berhasil ditambahkan ke dalam blockchain", "success")
					 })
					 .catch(error => {
					 	Swal.fire("error", "error", "error")
					 })
			},

			get_class(){
				if (this.mining_status.code == "MINING_NEEDED") {
					return "text-red-600"
				}
				return "text-green-600"
			}

		},
		created(){
			this.get_blockchain();
		}
	}
</script>