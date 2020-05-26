import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index'

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
		redirect: '/dashboard/learn',
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/dashboard/learn',
		name: 'learn',
		component: () => import('../views/Learn'),
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/dashboard/decks',
		name: 'decks',
		component: () => import('../views/Decks'),
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/dashboard/stats',
		name: 'stats',
		component: () => import('../views/Stats'),
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/dashboard/profile',
		name: 'profile',
		component: () => import('../views/Profile'),
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/create',
		name: 'create',
		component: () => import('../views/Create'),
		meta: {
			requiresAuth: true
		}
	},
	{
		path: '/review/:name',
		props: true,
		component: () => import('../views/Learn'), // Make this point to the view for actually reviewing the cards
		meta: {
			requiresAuth: true			
		}
	},
	{
		path: '/edit/:name',
		props: true,
		component: () => import('../views/Edit'),
		meta: {
			requiresAuth: true
		}
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

router.beforeEach((to, from, next) => {
	const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
	if(requiresAuth && !store.state.signedIn) {
		next('login')
	} else {
		next()
	}
})

export default router
