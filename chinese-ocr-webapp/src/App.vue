<template>
	<div id='app'>
		<div id="nav">
			<Navigation/>
		</div>
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
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap');
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
	overflow: scroll;
	color: #ffffff;
}
</style>
