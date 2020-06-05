const functions = require('firebase-functions')
// const axios = require('axios')
const vision = require('@google-cloud/vision')
const client = new vision.ImageAnnotatorClient()

exports.ocrVision = functions.https.onRequest(async (request, response) => {
	response.set('Access-Control-Allow-Origin', '*') // TODO: Add whitelisted domains
	// const fileName = './vision-test-imgs/handwriting-master.jpg'

	const fileName = request.body.imageData

	const req = {
		image: {
			content: fileName
		}
	}

	client.documentTextDetection(req)
		.then(result => response.send(result))
		.catch(error => response.send(error))
})


// OLD CODE -- TEMP REMOVED

// axios({
// 	method: 'post',
// 	url: 'https://vision.googleapis.com/v1/images:annotate',
// 	headers: {
// 		"Authorization": `Bearer ${request.body.token}`,
// 		"Content-Type": "application/json charset=utf-8"
// 	},
// 	data: {
// 		"requests": [
// 			{
// 				"image": {
// 					"content": request.body.imageData
// 				},
// 				"features": [
// 					{
// 						"type": "DOCUMENT_TEXT_DETECTION"
// 					}
// 				]
// 			}
// 		]
// 	},
// 	maxContentLength: 100000,
// 	maxBodyLength: 100000
// })
// 	.then((result) => response.send(result))
	// .catch(error => console.log(JSON.stringify(error)))