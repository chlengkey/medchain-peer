<template>
	<div class="relative h-full">
		<div class="md:w-56"></div>
		<div class=" fixed w-56 bg-blue-500 h-full shadow">

			<div class="px-4 mt-8">
				<img src="@/assets/logo.png" class="w-8 mb-5">
				<p class="font-extrabold text-white text-lg">Halo, Chrisdityra</p>
				<p class="text-sm text-white mt-0.5">Blockchain based medical service</p>
				<p class="red-glow-button mt-4 text-sm"><LogOut class="-mt-0.5 mr-1" />Log Out</p>
			</div>
			
			<hr class="my-5 border-white opacity-30" />

			<div class="w-full px-5 text-sm relative">
				<p class="yellow-glow-button w-full"><Plus class="mr-1" />Pemeriksaan Baru</p>
				<p class="nav-item"><Home class="-mt-0.5 mr-2" /> Dashboard</p>
				<p class="nav-item"><UserGroup class="-mt-0.5 mr-2" />Daftar Pasien</p>
				<p class="nav-item"><UserAdd class="-mt-0.5 mr-2" />Pasien Baru</p>
				<p class="nav-item"><Cog class="-mt-0.5 mr-2" />Pengaturan</p>
			</div>

		</div>
	</div>
</template>

<style type="text/css">
	
	.nav-item{
		@apply text-white font-semibold mt-2 hover:text-gray-800 transition rounded-md  cursor-pointer py-2
	}

</style>

<script type="text/javascript">
	
	import Plus from '@/assets/icons/plus.vue'
	import Home from '@/assets/icons/home.vue'
	import UserAdd from '@/assets/icons/userAdd.vue';
	import UserGroup from '@/assets/icons/userGroup.vue'
	import LogOut from '@/assets/icons/logout.vue'
	import Cog from '@/assets/icons/cog.vue'

	export default{
		components : {
			// icons
			Plus, Home, UserAdd, UserGroup, LogOut, Cog
		} 
	}
</script>