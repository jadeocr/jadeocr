# chinese-ocr

## Demo
View a [live demo](https://tanayb11.github.io/chinese-ocr/) of this project. It's still in the works. (NOTE: Demo not available yet)

## About
This repository contains code that trains a convolutional neural network (CNN) to recognize handwritten Chinese characters. The network is trained on the CASIA dataset, which can be found at [http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html](http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html).

## Downloading
Clone this repository to your computer. From the [Downloads Section of the CASIA page](http://www.nlpr.ia.ac.cn/databases/handwriting/Download.html), Download **HWDB1.0train_gnt (2741MB)** and **HWDB1.0test_gnt (681MB)** and extract the folder so that you end up with two folders with GNT files. Store them in a directory labeled **data**.

## Obtaining the full dataset
Change your directory to this repository. Modify **convert.py** to correspond to the relative locations of your train and test directories. Call them **train** and **test**.
```
train_data_dir = os.path.join(data_dir, 'your_path_here')
test_data_dir = os.path.join(data_dir, 'your_path_here')
```

## Training
Modify **train.py** to reflect the number of classes you choose to train the network on.
```
model.add(Dense(number_of_classes, activation='softmax'))
```
Run the program.

## Prediction
Save an image labelled **test.png** you would like to have the network predict to **data**. Comment out lines 60-79 of **preprocess.py**, then run **predict.py**

## Acknowledgements
I'd like to thank the following people/pages for providing resources that have especially helped me.

[integeruser on Github](https://github.com/integeruser/CASIA-HWDB1.1-cnn)

[想飞的石头在知乎](https://zhuanlan.zhihu.com/p/24698483)

[蹦跶的小羊羔在cdsn.net](https://blog.csdn.net/yql_617540298/article/details/82740382)

[Benson Ruan on Github](https://github.com/bensonruan/Hand-Written-Digit-Recognition)
