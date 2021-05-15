<template>
	<Modal ref="modal">
		<template v-slot:content>
			<p class="flex">
				<Key class="mr-2 mt-1" width=5 height=5 />
				<div >
					<p class="text-lg font-bold mt-0">Masukan Token</p>
					<p class="text-sm text-gray-500">Silahkan memasukan token pemeriksaan</p>
				</div>
			</p>
			<Text class="mt-4 mb-2" @input="token = $event.target.value" placeholder="Nomor Token" />
			<p class="text-xs" :class="footer.class"><InformationCircle/> {{footer.text}}</p>
		</template>
		<template v-slot:button>
			<button @click="inspect()" class="orange-button col-span-2 ml-2">
				<transition name="fade" mode="out-in">
					<Refresh class="animate-spin mr-1 -mt-1" v-show="animateSpinIcon"/>
				</transition>
				<span>Periksa</span>
			</button>
		</template>
	</Modal>
</template>

<script type="text/javascript">
	
    /* TOKEN MODAL
	*  Bertugas untuk memeriksa jika token yang diberikan adalah valid atau tidak
	*  [VALID] diarahkan ke url /pasien/periksa/{nomor_token}
	*/

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
		methods : {
			
			open(){
				this.$refs.modal.openModal();
			},

			inspect(){
				const app = this;
				if (!app.tokenFormatValid()) {return}
				app.animateSpinIcon = true;
				app.changeFooter('text-yellow-400','Mengecek Token');
				
				setTimeout(function(){
					app.changeFooter('text-red-600', "Token tidak valid");
					app.animateSpinIcon = false;
				},1000)
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