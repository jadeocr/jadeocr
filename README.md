# chinese-ocr
A web-based flashcard app directed at language learning and focused on learning Chinese. Complete with handwriting recognition, a [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition) system, and a clean, minimalist UI. This project aims to cover all these bases while staying open source.


## Demo
See and interact with the live [demo](https://chinese-ocr-274418.web.app/). It's still in the works

### Landing Page

![Landing Page](demos/landing-page.png)

## Built With
* [TensorFlow](https://www.tensorflow.org)
* [Vue.js](https://vuejs.org)
* [Firebase](https://firebase.google.com/)

## Features
* [x] Chinese handwriting recognition
* [x] Individual user accounts
* [ ] Spaced repetition flashcards
* [ ] Support for more languages

## Installation
We're still working on the webapp. Please help out by [contributing](#contribute)!

To use the Chinese handwriting OCR model, see the section on using the CNN below.

### Quickstart
Run these 3 commands to spin up a quick development instance:
```
npm install
npm run twbuild
npm run serve
```

#### Project setup
Note: Since `node_modules` is not committed, this _must_ be run right after cloning the repo.
```
npm install
```

#### Builds TailwindCSS files
Note: Run this after first cloning the repo or after modifying **tailwind.config.js**
```
npm run twbuild
```

#### Adding Firebase
To add the backend, create a project on [Firebase](https://firebase.google.com). Copy the JS config snippets from the Firebase console into the `firebaseConfig` object in **chinese-ocr-webapp/src/firebase/credentials.js** to add the SDK credentials.
```javascript
export default {
  firebaseConfig: {
  
  }
}
```

### Compilation

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Lints and fixes files
```
npm run lint
```

## CNN
The OCR neural network is trained on a 100-class subset of the [CASIA Chinese Handwriting Dataset](http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html). Data augmentation needs to be applied to the dataset to achieve a usable training accuracy. Also, more computing power is needed to train on the 2 million+ training examples.

### Obtaining the Dataset
To obtain the full dataset, download [**HWDB1.1train_gnt (2741MB)**](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn.zip) and [**HWDB1.1test_gnt (681MB)**](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst.zip) and extract the zip files. Store them in the directory **convnet/data** and make sure the extracted folders are named **HWDB1.1trn_gnt** and **HWDB1.1tst_gnt**, respectively.

### Preprocessing
Run **preprocess.py** to convert from GNT to png.

### Training
Modify **train.py** to reflect the number of classes you want to train the model on.
```python
model.add(Dense(number_of_classes, activation='softmax'))
```

This is the model structure for training on the subsetted dataset.

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 32, 32, 64)        640       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 16, 16, 64)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 16, 16, 64)        36928     
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        36928     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 4096)              0         
_________________________________________________________________
dense (Dense)                (None, 256)               1048832   
_________________________________________________________________
dropout (Dropout)            (None, 256)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 100)               25700     
=================================================================
Total params: 1,149,028
Trainable params: 1,149,028
Non-trainable params: 0
_________________________________________________________________
```

### Prediction
Save an image **test.jpg** you would like to have the network predict to **data** and run **predict.py**.

## Contribute
Contributions are very much appreciated! Please take a look at the information below. There are no set-in-stone rules; use your best judgement while trying to follow the guidelines.

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

## Contact
If you would like to get in touch with me for any (legitimate) reason, please do not hesitate to 
<a href='mailto: tanaybiradar24@gmail.com'>contact</a> me.

## License
This repository is licensed under the MIT License.

[Tanay Biradar](https://github.com/TanayB11)
