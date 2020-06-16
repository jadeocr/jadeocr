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


.btn-teal {
	background-color: #03dac5;
	opacity: 0.87;
}

.btn-blue {
	background-color: #1e88e5;
	opacity: 0.87;
}

.btn-purple:hover, .btn-red:hover, .btn:hover {
	opacity: 0.75;
}

.btn-purple {
	background-color: #bb86fc;
	opacity: 0.87;
}

#page-content {
	position: fixed;
	right: 0px;
	width: calc(100vw - 300px);
	-webkit-transition: width 0.3s ease;
	transition: width 0.3s ease;
	height: calc(98vh - 8.5rem);
}

@media(max-width: 640px) {
	#page-content {
		width: 100vw;
		height: 100vh;
	}
}
@media(max-width: 768px) {
	#page-content {
		height: calc(98vh - 7.75rem);
	}
}
@media(max-width: 1024px) {
	#page-content {
		height: calc(98vh - 4.5rem);
	}
}

/* Credit to @devinrhode2 on GitHub: https://gist.github.com/devinrhode2/2573411 */
::-webkit-scrollbar {
  width: 8px;
  background-color: rgba(0,0,0,0);
  -webkit-border-radius: 100px;
	border-radius: 100px;
}

::-webkit-scrollbar:hover {
  background-color: rgba(255,255,255, 0.05);
  transition: background-color 0.5 ease;
}

::-webkit-scrollbar-thumb:vertical {
  background: rgba(255,255,255,0.3);
  -webkit-border-radius: 100px;
	border-radius: 100px;
}
::-webkit-scrollbar-thumb:vertical:active {
  background: rgba(255,255,255,0.2);
  -webkit-border-radius: 100px;
	border-radius: 100px;
}

/* ::-webkit-scrollbar {
	display: none;
}

body {
	-ms-overflow-style: none;
} */

#page-content {
	-webkit-transition: width 0.3s ease, opacity 0.1s ease, visibility 0.1s ease;
	transition: width 0.3s ease, opacity 0.1s ease, visibility 0.1s ease;
}
</style>
