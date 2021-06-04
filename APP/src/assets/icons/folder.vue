<template>
	<svg class="h-5 w-5 inline-block" 
		 :class="'w-' + width + ' h-' + height" 
		 fill="none" 
		 viewBox="0 0 24 24" 
		 stroke="currentColor">
		 <path stroke-linecap="round" 
		 	   stroke-linejoin="round"
		 	   d="M5 19a2 2 0 01-2-2V7a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1M5 19h14a2 2 0 002-2v-5a2 2 0 00-2-2H9a2 2 0 00-2 2v5a2 2 0 01-2 2z"/>
	</svg>
</template>

<script type="text/javascript">
	export default{
		props : ["width", "height"]
	}
</script>