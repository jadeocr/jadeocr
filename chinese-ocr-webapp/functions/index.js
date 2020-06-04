const functions = require('firebase-functions')
const vision = require('@google-cloud/vision')
const client = new vision.ImageAnnotatorClient()

// exports.helloWorld = functions.https.onRequest((request, response) => {
// 	response.set('Access-Control-Allow-Origin', '*')
// 	console.log('Hello World!')
// 	response.send("Hello from Firebase!")
// })

exports.ocrVision = functions.https.onRequest(async (request, response) => {
	response.set('Access-Control-Allow-Origin', '*') // TODO: Add whitelisted domains

	const fileName = './vision-test-imgs/handwriting-master.jpg'
	// Read a local image as a text document
	client.documentTextDetection(fileName)
		.then((result) => {
			console.log(result)
		})
		.catch(error => console.log(error))
})