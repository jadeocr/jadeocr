const functions = require('firebase-functions')
// const axios = require('axios')
const vision = require('@google-cloud/vision')
const client = new vision.ImageAnnotatorClient()

exports.ocrVision = functions.https.onRequest(async (request, response) => {
	response.set('Access-Control-Allow-Origin', '*') // TODO: Add whitelisted domains

	const fileName = request.body.imageData

	const req = {
		image: {
			content: fileName
		},
		imageContext: {
			languageHints: ["zh-Hans-handwrit"]
		}
	}

	client.documentTextDetection(req)
		.then(result => response.send(result))
		.catch(error => response.send(error))
})