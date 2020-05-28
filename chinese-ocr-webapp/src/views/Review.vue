<template>
	<div id='review'>
		<div class="w-1/2 m-auto text-center lg:text-left lg:ml-16
		mt-12 md:mt-18 xl:mt-24 opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">
			{{ name }}
		</div>
		<div class='w-3/5 lg:w-1/2 m-auto mt-12 lg:mt-24 text-center'>	
			<div class='bg-black rounded-md px-12 py-12 md:py-24 card'>
				<!-- {{ currentWord }} --> HELLO
			</div>
			<div class="mt-8">
				<div class='text-md md:text-lg lg:text-xl xl:text-2xl rounded-md
				w-1/2 md:w-1/5 text-center m-auto btn btn-blue rounded-md px-4 py-2'>
					Submit
				</div>
				<div class="mt-8 w-3/4 md:w-3/5 m-auto flex items-center justify-between opacity-87">
					<div class='btn btn-red rounded-md px-4 py-2'>
						<svg class="bi bi-x" width="1.25em" height="1.25em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
							<path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
						</svg>
					</div>
					<div class='btn btn-teal rounded-md px-4 py-2'>
						<svg class="bi bi-check2" width="1.25em" height="1.25em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
						</svg>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Review',
	props: {
		name: String
	},
	methods: {
		
	}
}
</script>

<style scoped>
.card {
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255,255,255,0.07);
	z-index: 2;
}

</style>