import os
import numpy as np
import tensorflow as tf
import cv2

def extract_data(path):
    labels = []
    data = []
    numOfItems = 0
    for i, label in enumerate(sorted(os.listdir(path))):
        if (label == '.DS_Store'): # Gets rid of problem on MacOS
            pass
        else:
            for j, filename in enumerate(os.listdir(os.path.join(path, label))):
                image = cv2.imread(os.path.join(path, label, filename))
                image = cv2.resize(image, (64, 64))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                data.append(image)
                labels.append(i-1)
                numOfItems += 1
    data = np.array(data)
    labels = tf.keras.utils.to_categorical(labels, num_classes=None, dtype='float32') # This seems to work
    return (data.reshape(numOfItems, 1, 64, 64), np.array(labels))

def plot_images(xval, yval):
    from matplotlib import pyplot as plt
    for i in range(9): # Plots 1st 9 images
        plt.subplot(330 + 1 + i)
        plt.imshow(xval[i], cmap=plt.get_cmap('gray'))
    plt.show()
    print('XY SHAPE: X=%s, y=%s' % (xval.shape, yval.shape))
    # cv2.imshow('abc', data[0]); cv2.waitKey(0); cv2.destroyAllWindows() # cv2 implementation - show the image at data[0]
