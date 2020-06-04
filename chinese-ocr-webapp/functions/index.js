const functions = require('firebase-functions')
const vision = require('@google-cloud/vision')
const client = new vision.ImageAnnotatorClient()

exports.helloWorld = functions.https.onRequest((request, response) => {
	response.set('Access-Control-Allow-Origin', '*')
	console.log('Hello World!')
	response.send("Hello from Firebase!")
})

exports.ocrVision = functions.https.onRequest(async (request, response) => {
	response.set('Access-Control-Allow-Origin', '*')

	const fileName = './vision-test-imgs/handwriting-master.jpg';
	// Read a local image as a text document
	const [result] = await client.documentTextDetection(fileName);
	const fullTextAnnotation = result.fullTextAnnotation;
	console.log(`Full text: ${fullTextAnnotation.text}`);
	fullTextAnnotation.pages.forEach(page => {
		page.blocks.forEach(block => {
			console.log(`Block confidence: ${block.confidence}`);
			block.paragraphs.forEach(paragraph => {
				console.log(`Paragraph confidence: ${paragraph.confidence}`);
				paragraph.words.forEach(word => {
					const wordText = word.symbols.map(s => s.text).join('');
					console.log(`Word text: ${wordText}`);
					console.log(`Word confidence: ${word.confidence}`);
					word.symbols.forEach(symbol => {
						console.log(`Symbol text: ${symbol.text}`);
						console.log(`Symbol confidence: ${symbol.confidence}`);
					})
				})
			})
		})
	})
})