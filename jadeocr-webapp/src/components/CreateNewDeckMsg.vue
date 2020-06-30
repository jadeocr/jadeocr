<template>
	<div>
		<div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 mt-8">
			<div class='mr-4 md:mr-12 mt-4 mb-8 col-span-1'>
				<div class='bg-black rounded-md px-6 py-6 decklist'>
					<div>
						<p class="text-sm md:text-md lg:text-lg xl:text-xl mt-2 text-center">Create a new deck to start</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'CreateNewDeckMsg'
}
</script>

<style scoped>
.decklist {
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255,255,255,0.07);
	z-index: 2;
}
</style>