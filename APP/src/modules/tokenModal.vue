<template>
	<form @submit.prevent="inspect()">
	<Modal ref="modal">
		<template v-slot:content>
			<p class="flex">
				<Key class="mr-2 mt-1" width=5 height=5 />
				<div >
					<p class="text-lg font-bold mt-0">Masukan Token</p>
					<p class="text-sm text-gray-500">Silahkan memasukan token pemeriksaan</p>
				</div>
			</p>
			<Text class="mt-4 mb-2" :value="token" @input="token = $event.target.value" placeholder="Nomor Token"/>
			<p class="text-xs" :class="footer.class"><InformationCircle/> {{footer.text}}</p>
		</template>
		<template v-slot:button>
			<button class="orange-button col-span-2 ml-2">
				<transition name="fade" mode="out-in">
					<Refresh class="animate-spin mr-1 -mt-1" v-show="animateSpinIcon"/>
				</transition>
				<span>Periksa</span>
			</button>
		</template>
	</Modal></form>
</template>

<script type="text/javascript">
	
    /* TOKEN MODAL
	*  Bertugas untuk memeriksa jika token yang diberikan adalah valid atau tidak
	*  [VALID] diarahkan ke url /pasien/periksa/{nomor_token}
	*/

	// API
	const axios = require('axios');

	// Components
	import Modal from '@/components/Modal.vue';
	import Text from '@/components/form_component/text.vue'

	// Icons
	import InformationCircle from '@/assets/icons/informationCircle.vue'
	import Refresh from '@/assets/icons/refresh.vue'
	import Key from '@/assets/icons/key.vue'

	export default{
		components : {Text, Modal, InformationCircle, Key, Refresh},
		data(){
			return{
				animateSpinIcon : false,
				token : "",
				footer : {
					class : "text-gray-400",
					text : 'Pelajari token lebih lanjut disini'
				},
			}
		},
		computed:{
			defaultURL : function(){
				return process.env.VUE_APP_API + "/token/check/" + this.token;
			}
		},
		methods : {
			
			open(){
				this.$refs.modal.openModal();
			},

			inspect(){
				const app = this;
				if (!app.tokenFormatValid()) {return}
				app.animateSpinIcon = true;
				app.changeFooter('text-yellow-400','Mengecek Token');
				
				axios.get(app.defaultURL)
					 .then(response => {
					 	setTimeout(function(){
					 		let tokenTemporary  = app.token;
					 		app.token = "";
					 		app.animateSpinIcon = false;

					 		if(response.data.valid){
					 			app.changeFooter('text-green-600', "Token valid");
					 			app.$router.replace("/pasien/periksa/" + tokenTemporary);
					 			setTimeout(function(){
					 				app.changeFooter('text-gray-400','Pelajari token lebih lanjut disini');
					 				app.$refs.modal.closeModal();
					 			},500)
					 			return;
					 		}
							app.changeFooter('text-red-600', "Token tidak valid");
						},1000)
					 })
			},

			tokenFormatValid(){
				this.changeFooter('text-gray-400','Pelajari token lebih lanjut disini');

				// Validate empty
				if (!this.token) {this.changeFooter("text-red-600", "Anda harus mengisi token");return false}

				// Validate length
				if (this.token.length < 5) {this.changeFooter("text-red-600", "Token terdiri dari 5 angka");return false}

				// Validate Success
				return true
			},

			changeFooter(css, text){
				this.footer.text = text;
				this.footer.class = css;
			}
		}
	}
</script>