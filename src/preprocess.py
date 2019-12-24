import os
import numpy as np
import tensorflow as tf
import cv2
from matplotlib import pyplot
# import pickle

train_path = '../data/temptrn' # TODO: CHANGE LATER TO ACTUAL TRAINING SET
test_path = '../data/temptst'

def extract_data(path):
    labels = []
    data = []
    for i, label in enumerate(sorted(os.listdir(path))):
        if (label == '.DS_Store'): # Gets rid of the problem of that file
            pass
        else:
            for j, filename in enumerate(os.listdir(os.path.join(path, label))):
                image = cv2.imread(os.path.join(path, label, filename))
                image = cv2.resize(image, (64, 64))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                data.append(image)
                labels.append(i-1) # Will have to look up in dictionary later for final result labels = pickle.load(open('char_dict', 'rb'))
    # cv2.imshow('abc', data[0]); cv2.waitKey(0); cv2.destroyAllWindows() # Show the image at data[0]
    return (np.array(data), np.array(labels))

def plot_images():
    # plot first few images
    for i in range(9): # Train images
        pyplot.subplot(330 + 1 + i)
        pyplot.imshow(trainX[i], cmap=pyplot.get_cmap('gray'))
    pyplot.show()
    for i in range(9): # Test images
        pyplot.subplot(330 + 1 + i)
        pyplot.imshow(testX[i], cmap=pyplot.get_cmap('gray'))
    pyplot.show()

(trainX, trainY) = extract_data(train_path)
(testX, testY) = extract_data(test_path)
print('Train: X=%s, y=%s' % (trainX.shape, trainY.shape))
print('Test: X=%s, y=%s' % (testX.shape, testY.shape))
