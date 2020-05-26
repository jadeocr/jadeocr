const fs = require('fs')

module.exports = {
	devServer: {
		open: process.platform === 'darwin',
		https: {
			key: fs.readFileSync('./certs/chinese-ocr.com+5-key.pem'),
			cert: fs.readFileSync('./certs/chinese-ocr.com+5.pem'),
		},
		public: 'https://localhost:8080/'
	}
}