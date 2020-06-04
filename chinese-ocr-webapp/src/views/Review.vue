<template>
	<div id='review'>
		<div class="w-1/2 m-auto text-center lg:text-left mt-12 md:mt-16 
		opacity-87 text-xl lg:text-2xl xl:text-3xl font-normal">
			{{ name }}
		</div>
		<div class='w-3/5 lg:w-1/2 m-auto mt-8 text-center'>	
			<div class='card-container'>
				<div
				class='bg-black rounded-md py-6 card font-normal text-xl lg:text-2xl xl:text-3xl'>
					<div>
						<p v-for='(n, side) in cardSideData' :key='side.key'>
							{{ cardSideData[side] }}
						</p>
					</div>
				</div>
				<div v-if='deck.ocr' id="draw-wrapper" ref="draw-wrapper" class='lg:ml-10 mt-8 lg:mt-0'>
					<canvas id='draw'></canvas>
					<div class="mt-1 md:mt-5 lg:mt-2 mr-0 flex justify-end" id="canvas-ctrls">
						<div class="mx-2" @click='clearCanvas()'>
							<svg class="bi bi-arrow-counterclockwise" width="1.25em" height="1.25em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
								<path fill-rule="evenodd" d="M12.83 6.706a5 5 0 0 0-7.103-3.16.5.5 0 1 1-.454-.892A6 6 0 1 1 2.545 5.5a.5.5 0 1 1 .91.417 5 5 0 1 0 9.375.789z"/>
								<path fill-rule="evenodd" d="M7.854.146a.5.5 0 0 0-.708 0l-2.5 2.5a.5.5 0 0 0 0 .708l2.5 2.5a.5.5 0 1 0 .708-.708L5.707 3 7.854.854a.5.5 0 0 0 0-.708z"/>
							</svg>
						</div>
					</div>
				</div>
			</div>
			<div class="mt-10">
				<div class="md:w-2/3 mt-4 m-auto flex items-center justify-between opacity-87">
					<div class='btn btn-red rounded-md px-4 py-3'
						@click='cardCheck("wrong")'
					>
						<svg class="bi bi-x" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
							<path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
						</svg>
					</div>
					<div @click='flipCard()'
						class="btn btn-blue mx-auto rounded-md py-2 px-4 text-xs md:text-sm font-normal unselect"
					>
						{{ reviewedButton }}
					</div>
					<div class='btn btn-cyan rounded-md px-4 py-3'
						@click='cardCheck("correct")'
					>
						<svg class="bi bi-check2" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd" d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
						</svg>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import * as moment from 'moment'

export default {
	name: 'Review',
	data() {
		return {
			deck: Object,
			untilDue: [],
			dueIndices: [], // Refers to which cards to review
			currentIndex: 0, // Iterator for dueIndices
			cardSideData: '',
			cardFace: 'front',
			canvas: null,
			ctx: null,
			xPos: 0,
			yPos: 0,
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
		flipCard() {
			if (!this.deck.ocr) {
				if (this.cardFace == 'back') {
					this.cardSideData = [
						this.deck.cards[this.dueIndices[this.currentIndex]].pinyin,
						this.deck.cards[this.dueIndices[this.currentIndex]].definition
					]
					this.cardFace = 'front'
				} else {
					this.cardSideData = [
						this.deck.cards[this.dueIndices[this.currentIndex]].hanzi,
						this.deck.cards[this.dueIndices[this.currentIndex]].definition
					]
					this.cardFace = 'back'
				}
			} else {
				// Handle OCR logic here
				this.$store.dispatch('getVisionPrediction')
			}
		},
		nextCard() {
			this.currentIndex ++
			this.cardFace = 'front'
			this.cardSideData = [
				this.deck.cards[this.dueIndices[this.currentIndex]].pinyin,
				this.deck.cards[this.dueIndices[this.currentIndex]].definition
			]
		},
		calculateSuperMemo2(index, quality) { // Thanks to Suragch on Stack Overflow!
			let repetitions = Number.parseInt(this.deck.repetitions[index])
			let easiness = Number.parseFloat(this.deck.easiness[index])
			let interval = Number.parseInt(this.deck.interval[index])

			let repetitionFormula = easiness + 0.1 - (5.0 - quality) * (0.08 + (5.0 - quality) * 0.02)
			easiness = Math.max(1.3, repetitionFormula)
			this.deck.easiness[index] = Number.parseFloat(easiness).toFixed(1)
		

			if (quality == 0) { // Modified for only 2 quality buttons (is either 0 or 5)
				this.deck.repetitions[index] = 0
			} else {
				this.deck.repetitions[index]++
			}

			if (repetitions <= 1) {
				this.deck.interval[index] = 1;
			} else if (repetitions == 2) {
				this.deck.interval[index] = 6;
			} else {
				this.deck.interval[index] = Math.round(interval * easiness);
			}

			// TODO: Add enhancements to tune SM-2 algorithm
			let today = this.$store.state.serverTime.clone()
			this.deck.dueDates[index] = today.add(this.deck.interval[index], 'days').format('YYYY-MM-DD')
		},
		submitFinished() {
			this.$store.dispatch('createDeck', {
				method: 'edit',
				name: this.name,
				deck: JSON.parse(JSON.stringify(this.deck))
			})
		},
		randInt(min, max) {
			return Math.floor(Math.random() * (max - min) + min)
		},
		cardCheck(correctness) {
			if (correctness == 'correct') {
				this.calculateSuperMemo2(this.dueIndices[this.currentIndex], 5)
			} else {
				this.calculateSuperMemo2(this.dueIndices[this.currentIndex], 0)
			}

			if (((this.currentIndex == (this.dueIndices.length - 1)) && (this.currentIndex < this.randInt(10, 20)))) {
				this.submitFinished()
			} else {
				this.nextCard()
			}
		},
		getDueDifference(due) {
			due = moment(due, 'YYYY-MM-DD')
			let now = moment(this.$store.state.serverTime.format('YYYY-MM-DD'), 'YYYY-MM-DD')
			return moment.duration(due.diff(now)).asDays()
		},
		chooseCards() {
			for (let i = 0; i < this.deck.numOfWords; i++) {
				this.untilDue.push(this.getDueDifference(this.deck.dueDates[i]))
			}
			let mostDue = Math.min(...this.untilDue)
			for (let i = 0; i < this.untilDue.length; i++) { // Checks for all cards due today
				if (this.untilDue[i] == mostDue) this.dueIndices.push(i)
			}
		},
		setPos(e) {
			let domRect = this.canvas.getBoundingClientRect()
			this.xPos = (e.clientX - domRect.left) / domRect.width * this.canvas.width
			this.yPos = (e.clientY - domRect.top) / domRect.height * this.canvas.height
		},
		draw(e) {
			if (e.buttons !== 1) return;
			this.ctx.beginPath()
			this.ctx.lineWidth = 20
			this.ctx.lineCap = 'round'
			this.ctx.strokeStyle = '#ffffff'
			this.ctx.moveTo(this.xPos, this.yPos)
			this.setPos(e)
			this.ctx.lineTo(this.xPos, this.yPos)
			this.ctx.stroke()
		},
		clearCanvas() {
			this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)
		},
	},
	mounted() {
		this.$store.dispatch('getServerTime')
			.then(this.$store.dispatch('getDecks'))
			.then(() => {
				this.deck = this.$store.state.decks.find(obj => {
					return obj.name == this.name
				})
				this.chooseCards()
				this.cardSideData = [
					this.deck.cards[this.dueIndices[this.currentIndex]].pinyin,
					this.deck.cards[this.dueIndices[this.currentIndex]].definition
				]
			})
			.catch(error => console.log(error))
	},
	updated() {
		if (this.deck.ocr) {
			this.canvas = document.getElementById("draw")
			this.ctx = this.canvas.getContext("2d")

			this.ctx.canvas.width = window.innerWidth
			this.ctx.canvas.height = window.innerHeight

			this.ctx.lineWidth = 10
			this.ctx.lineCap = 'round'
			this.ctx.strokeStyle = '#ffffff'

			this.canvas.addEventListener("mousemove", this.draw, false)
			this.canvas.addEventListener("mousedown", this.setPos, false)
			this.canvas.addEventListener("mouseenter", this.setPos, false)
		}
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
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
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

.unselect {
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	-o-user-select: none;
	user-select: none;
	cursor: default;
}

#draw-wrapper {
	border: 1px solid rgba(255, 255, 255, 0.6);
	border-radius: 10px;
	width: 100%;
	height: 60vw;
}

#canvas-ctrls {
	height: 1rem;
}

canvas {
	border-radius: 10px 10px 10px 10px;
	width: 100%;	
	height: 87.5%;
}

.bi {
	width: 0.75em;
	height: 0.75em;
}

@media (max-width: 768px) and (orientation:landscape) {
	#canvas-ctrls {
		margin-top: 1rem;
	}
}

@media(min-width: 1024px) {
	.card-container {
		display: flex;
		justify-content: space-between;  
	}
	.card {
		height: 40vh;
	}
	#draw-wrapper {
		width: 80vh;
		height: 40vh;
	}
	.bi {
		width: 1.25em;
		height: 1.25em;
	}
}
</style>