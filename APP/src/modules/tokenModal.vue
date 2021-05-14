<template>
	<Modal ref="modal">
		<template v-slot:content>
			<p class="text-lg font-bold">Masukan Token</p>
			<p class="text-sm text-gray-500">Silahkan memasukan token pemeriksaan</p>
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
	
	// Components
	import Modal from '@/components/Modal.vue';
	import Text from '@/components/form_component/text.vue'

	// Icons
	import InformationCircle from '@/assets/icons/informationCircle.vue'
	import Refresh from '@/assets/icons/refresh.vue'

	export default{
		components : {Text, Modal, InformationCircle, Refresh},
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
				app.changeFooter('text-gray-400','Pelajari token lebih lanjut disini');
				if (!app.token) {app.changeFooter("text-red-600", "Anda harus mengisi token");return}
				app.animateSpinIcon = true;
				app.changeFooter('text-yellow-400','Mengecek Token');
				/*this.$refs.modal.closeModal();
				setTimeout(function(){
					app.$router.replace("/pasien/periksa/29991");
				},500);*/
				setTimeout(function(){
					app.changeFooter('text-red-600', "Token tidak valid");
					app.animateSpinIcon = false;
				},1000)
			},

			changeFooter(css, text){
				this.footer.text = text;
				this.footer.class = css;
			}
		}
	}
</script>