<template>
	<div id='review'>
		<div class="w-1/2 m-auto text-center lg:text-left mt-12 md:mt-16 
		opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">
			{{ name }}
		</div>
		<div class='w-3/5 lg:w-1/2 m-auto mt-8 text-center'>	
			<div class='bg-black rounded-md px-12 py-24 md:py-32 card'>
				<!-- {{ currentWord }} --> HELLO
			</div>
			<div class="mt-10">
				<div class="md:w-2/3 mt-4 m-auto flex items-center justify-between opacity-87">
					<div class='btn btn-red rounded-md px-4 py-3'>
						<svg class="bi bi-x" width="1.25em" height="1.25em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
							<path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
						</svg>
					</div>
					<div class="btn btn-blue mx-auto rounded-md py-2 px-4 text-sm font-normal">
						{{ reviewedButton }}
					</div>
					<div class='btn btn-cyan rounded-md px-4 py-3'>
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
	data() {
		return {
			deck: Object,
		}
	},
	props: {
		name: String
	},
	computed: {
		reviewedButton() {
			if (this.deck.ocr) {
				return 'Check Writing'
			} else {
				return 'Flip Card'
			}
		}
	},
	methods: {
		
	},
	mounted() {
		this.deck = this.$store.state.decks.find(obj => {
			return obj.name == this.name
		})
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

.btn:hover {
	opacity: 0.75;
}

.btn-cyan {
	background-color: #26a69a;
	opacity: 0.87;
}

.btn-review-red {
	background-color: #ff7043;
	opacity: 0.87;
}
</style>