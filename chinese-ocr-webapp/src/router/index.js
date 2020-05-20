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
		redirect: '/dashboard/learn'
	},
	{
		path: '/dashboard/learn',
		name: 'learn',
		component: () => import('../views/Learn')
	},
	{
		path: '/dashboard/decks',
		name: 'decks',
		component: () => import('../views/Decks')
	},
	{
		path: '/dashboard/stats',
		name: 'stats',
		component: () => import('../views/Stats')
	},
	{
		path: '/dashboard/profile',
		name: 'profile',
		component: () => import('../views/Profile')
	},
	{
		path: '/create',
		name: 'create',
		component: () => import('../views/Create')
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
