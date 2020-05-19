<template>
	<div id='app'>
		<Navigation/>
		<router-view/>
	</div>
</template>

<script>
import Navigation from './components/Navigation.vue'

export default {
	name: 'App',
	components: {
		Navigation
	}
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400&display=swap');
@import './assets/css/output.css';

/* Styling the background */
body {
	background-size: cover;
	background: #121212;
}

#app {
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	font-family: 'Open Sans', sans-serif;
	font-weight: 300;
	color: #ffffff;
}

.chinese {
	font-family: 'Noto Sans SC';
}

.btn-red {
	background-color: #cf6679;
	opacity: 0.87;
}

.btn-red:hover {
	opacity: 0.75;
}

.btn-purple {
	background-color: #bb86fc;
	opacity: 0.87;
}

.btn-purple:hover {
	opacity: 0.75;
}

#page-content {
	position: fixed;
	right: 0px;
	width: calc(100vw - 300px);
	-webkit-transition: width 0.3s ease;
	transition: width 0.3s ease;
}

@media(max-width: 640px) {
	#page-content {
		width: 100vw;
	}
}
</style>
