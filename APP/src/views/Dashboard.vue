<template>
	<div>
		<TokenModal ref="tokenModal" />
		<p @click="$refs.tokenModal.open()">Buka</p>
	</div>
</template>

<script type="text/javascript">
	
	import TokenModal from '@/modules/tokenModal.vue';

	export default{
		components : {TokenModal},
		
	}
</script>