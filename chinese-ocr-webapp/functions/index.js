const functions = require('firebase-functions')
const axios = require('axios')

// exports.helloWorld = functions.https.onRequest((request, response) => {
// 	response.set('Access-Control-Allow-Origin', '*')
// 	console.log('Hello World!')
// 	response.send("Hello from Firebase!")
// })

exports.ocrVision = functions.https.onRequest(async (request, response) => {
	response.set('Access-Control-Allow-Origin', '*') // TODO: Add whitelisted domains
	// const fileName = './vision-test-imgs/handwriting-master.jpg'

	const body = {
		"requests": [
			{
				"image": {
					"content": request.body.imageData
				},
				"features": [
					{
						"type": "DOCUMENT_TEXT_DETECTION"
					}
				],
				"imageContext": {
					"languageHints": ["zh-handwrit"]
				}
			}
		]
	}

	axios({
		method: 'post',
		url: 'https://vision.googleapis.com/v1/images:annotate',
		data: body,
		maxContentLength: 100000,
		maxBodyLength: 100000
	})
		.then((result) => {
			console.log(result)
			response.send(result[0].textAnnotations)
		})
		.catch(error => console.log(JSON.stringify(error)))
})