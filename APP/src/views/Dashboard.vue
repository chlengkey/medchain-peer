<template>
	<div>
		<TokenModal ref="tokenModal" />
		<p @click="$refs.tokenModal.open()">Buka</p>
	</div>
</template>

<script type="text/javascript">
	
	import TokenModal from '@/modules/tokenModal.vue';
	const axios = require('axios');
	
	export default{
		components : {TokenModal},
		created(){
			axios.get("http://127.0.0.1:5000/token/generate").then(response =>{
				console.log(response);
			})
		}
	}
</script>