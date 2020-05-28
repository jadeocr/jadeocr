<template>
	<div class='row-span-1' :class='{ "mt-12 md:mt-16": "!isFirstElement"}'>
			<div class="flex items-center justify-center font-normal">
				<FeatureIcons :name='name'/>
				<p class="ml-5">{{ title }}</p>
			</div>
			<p class="text-left mt-2 text-md text-center">{{ body }}</p>
	</div>
</template>

<script>
import FeatureIcons from '../components/FeatureIcons'
export default {
	components: {
		FeatureIcons
	},
	props: {
		title: String,
		name: String,
		body: String,
		isFirstElement: Boolean
	}
}
</script>

<style scoped>

</style>