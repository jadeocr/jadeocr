import 'firebase/firestore'
import { firebaseApp }  from './firebaseInit'

export const db = firebaseApp.firestore()
