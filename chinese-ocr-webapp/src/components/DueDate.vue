<template>
	<div class="text-sm font-light" id='dueDate' :class='color'>
		<span v-if="untilDue >= 0">Due in</span> 
		<span v-else>Overdue by</span>
		{{ Math.abs(untilDue).toFixed(0) }}
		<span v-if='Math.abs(untilDue).toFixed(0) == 1 || Math.abs(untilDue).toFixed(0) == -1'>day</span>
		<span v-else>days</span>
	</div>
</template>

<script>
export default {
	name: 'DueDate',
	props: {
		untilDue: Number,
		color: String
	}
}
</script>