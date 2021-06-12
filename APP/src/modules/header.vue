<template>

	<div class="px-10 relative shadow">
		<div class=" absolute center-v right-10 flex">

			<a href="/dataDokter" class="p-2 flex text-blue-400 transition-colors duration-200 rounded-full bg-blue-50 hover:text-blue-600 hover:bg-blue-100 dark:hover:text-light dark:hover:bg-blue-700 dark:bg-dark focus:outline-none focus:bg-blue-100 dark:focus:bg-blue-700 focus:ring-blue-800">
				<Notification width="6" height="6"/>
			</a>

			<router-link to="/dataDokter">
					<a href="/dataDokter" class="p-2 ml-3 flex text-blue-400 transition-colors duration-200 rounded-full bg-blue-50 hover:text-blue-600 hover:bg-blue-100 dark:hover:text-light dark:hover:bg-blue-700 dark:bg-dark focus:outline-none focus:bg-blue-100 dark:focus:bg-blue-700 focus:ring-blue-800">
						<Identification width="6" height="6"/>
					</a>
			</router-link>

			<p class="red-secondary-button text-sm mt-1 ml-1" @click="logOut()">
				<LogOut class="-mt-0.5 mr-1" />Keluar</p>

		</div>

			<p class="text-xl text-blue-700 font-semibold relative py-5">{{$route.name}}</p>

	</div>
		
	
</template>

<script type="text/javascript">
	import LogOut from '@/assets/icons/logout.vue'
	import Identification from '../assets/icons/identification.vue'
	import Notification from '../assets/icons/notification.vue'

	export default{
		components : {LogOut, Identification, Notification},
		created(){
			
		}
	}
</script>