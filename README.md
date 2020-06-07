# chinese-ocr
Chinese-ocr is a beautiful web-based [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition) flashcard app for learning languages (not just Chinese), complete with handwriting recognition.

It ticks all the boxes. It's beautiful, efficient, and effective. Most importantly, it provides handwriting recognition that is crucial for learning languages without an alphabet.


## Demo
A demo is still in the works. Stay tuned for updates.

### Landing Page
![Landing Page](demos/landing-page.png)


## Built With
* [TensorFlow](https://www.tensorflow.org)
* [Vue.js](https://vuejs.org)
* [Firebase](https://firebase.google.com/)


## Features
* [x] Handwriting recognition
* [x] Spaced repetition flashcards
* [x] Support for more languages

### Quickstart
In the **chinese-ocr-webapp** directory, run the following to quickly spin up a development instance.
```bash
$ npm install        # Installs dependencies
$ npm run twbuild    # Builds Tailwind CSS files
$ npm run serve      # Compiles/hot-reloads dev server
```

#### Adding Firebase
To add the backend, create a project in [Firebase](https://firebase.google.com). Copy the JS config snippets from the Firebase console into the `firebaseConfig` in **chinese-ocr-webapp/src/firebase/credentials.js** to add the SDK credentials.
```javascript
export default {
  firebaseConfig: {
    apiKey: "API_KEY",
    authDomain: "AUTH_DOMAIN",
    ...
  }
}
```

#### Development
```bash
$ npm run serve      # Compiles/hot-reloads dev server
$ npm run build      # Compiles/minifies -> dist for production
$ npm run lint       # Lints/fixes files
```

#### Deployment
```bash
$ npm run devbuild   # Builds, deploys to Firebase Hosting, and removes dist
```


## CNN
Currently, chinese-ocr uses the Google Cloud Vision API to handle handwriting recognition. In the future, it is planned to switch to a custom neural network for more accurate detection of languages not based on the Latin script.

The OCR neural network is trained on a 100-class subset of the [CASIA Chinese Handwriting Dataset](http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html). To train on the full dataset effectively, it is necessary to have more training examples per class.

### Obtaining the Dataset
To obtain the full dataset, download [**HWDB1.1train_gnt (2741MB)**](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn.zip) and [**HWDB1.1test_gnt (681MB)**](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst.zip) and extract the zip files. Store them in the directory **convnet/data** and check that the extracted folders are named **HWDB1.1trn_gnt** and **HWDB1.1tst_gnt**, respectively.

### Preprocessing
Run **preprocess.py** to convert from GNT to png.

### Training
Modify **train.py** to reflect the number of classes you want to train the model on.
```python
model.add(Dense(NUMBER_OF_CLASSES, activation='softmax'))
```

### Prediction
Save an image **test.jpg** that you would like to have the network predict to **data** and run **predict.py**.


## Contribute
Contributions are very much appreciated! Please take a look at the information below before contributing.

### Issues
Browse through the [issues](https://github.com/TanayB11/chinese-ocr/issues) or submit one. Here are a couple guidelines to follow:
* Make sure all of your dependencies are up to date
* Include steps to reproduce the issue
* Expected behavior and what went wrong
* Screenshots/terminal output if necessary

### Pull Requests
Pull requests are also always welcome. Here are a couple simple guidelines:
* Make sure your code is readable and commented when necessary
* Document your changes adequately when opening a pull request

### Donations
If chinese-ocr has been of some value to you, and if you can afford it, please consider donating. Donations will always first be allocated to the upkeep of the project. Your donations will also support the development of new features and code maintenance. Here's how you can donate:
* BTC: 15Y9NZjxTLWHDU8kVsqN7FKey3c1RPNiFi
* (We'll add more options soon)

Thank you so much for taking the time to contribute!


## Credits
* [integeruser on Github](https://github.com/integeruser/CASIA-HWDB1.1-cnn)
* [想飞的石头在知乎](https://zhuanlan.zhihu.com/p/24698483)
* [蹦跶的小羊羔在cdsn.net](https://blog.csdn.net/yql_617540298/article/details/82740382)
* [Suragch on Stack Overflow](https://stackoverflow.com/questions/49047159/spaced-repetition-algorithm-from-supermemo-sm-2)


## Contact
If you would like to get in touch with me for any (legitimate) reason, please do not hesitate to 
<a href='mailto: tanaybiradar24@gmail.com'>contact</a> me.


## License
This repository is licensed under the MIT License.

[Tanay Biradar](https://github.com/TanayB11)
