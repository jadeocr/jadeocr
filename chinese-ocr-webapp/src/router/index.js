import Vue from 'vue'
import VueRouter from 'vue-router'

import Landing from '../views/Landing'

Vue.use(VueRouter)

const mode = 'history' // Removes # in URL: Configure history mode for production

const routes = [
	{
		path: '/',
		name: 'landing',
		component: Landing
	},
	{
		path: '/login',
		name: 'login',
		component: () => import('../views/Login')
	},
	{
		path: '/dashboard',
		name: 'dashboard',
		component: () => import('../views/Dashboard')
	},
	{
		path: '/profile',
		name: 'profile',
		component: () => import('../views/Profile')
	},
	{
		path: '*',
		component: () => import ('../views/NotFound')
	}
]

const router = new VueRouter({
	mode,
	routes
})

export default router
