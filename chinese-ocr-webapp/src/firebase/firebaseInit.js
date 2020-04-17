import * as firebase from 'firebase/app'
import credentials from './credentials'

export const firebaseApp = firebase.initializeApp(credentials.firebaseConfig)
