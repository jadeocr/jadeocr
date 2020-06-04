const vision = require('@google-cloud/vision')({
	projectId: 'your-project-id',
	keyfileName: 'keyfile.json'
})
const admin = require('firebase-admin')
const functions = require('firebase-functions')


