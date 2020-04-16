import * as firebase from 'firebase/app'
import credentials from './credentials'
import 'firebase/firestore'

const firebaseApp = firebase.initializeApp(credentials.firebaseConfig)
export const db = firebaseApp.firestore()
