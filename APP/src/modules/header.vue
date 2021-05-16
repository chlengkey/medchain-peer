<template>
	<div class="px-10 relative shadow">
		<div class="absolute center-v right-10 flex">
			<p  v-if="blockchainValidity" class="font-semibold text-sm green-button"
			    title="Blockchain anda valid">
			    <ShieldCheck class="-mt-0.5 mr-1 -ml-1" /> Valid</p>
			<p 	v-else class="font-semibold text-sm red-button"
				title="Blockchain anda tidak valid">
				<ShieldCheck class="-mt-0.5 mr-1 -ml-1" /> Error</p>
			<p class="red-secondary-button text-sm ml-1" @click="logOut()">
				<LogOut class="-mt-0.5 mr-1" />Keluar</p>	
		</div>
		<p class="text-xl text-blue-700 font-semibold relative py-5">{{$route.name}}</p>
	</div>
</template>
<script type="text/javascript">
	import LogOut from '@/assets/icons/logout.vue'
	import ShieldCheck from '@/assets/icons/shieldCheck.vue'

	export default{
		components : {LogOut, ShieldCheck},
		created(){
			
		}
	}
</script>