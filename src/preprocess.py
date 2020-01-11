import os, h5py
import numpy as np
from keras.utils import to_categorical
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
    labels = to_categorical(labels, num_classes=None, dtype='float32') # One-hot; this seems to work
    return (data.reshape(numOfItems, 1, 64, 64), np.array(labels))

def normalize(trainX, testX):
    # Int to float
	train_norm = trainX.astype('float32')
	test_norm = testX.astype('float32')
    # Normalize between 0 and 1
	train_norm = train_norm / 255.0
	test_norm = test_norm / 255.0
	return train_norm, test_norm

# TODO: Comment out after extraction
# Call preprocessing functions
train_path = '../data/train'
test_path = '../data/test'
print('Extracting Train...')
(trainX, trainY) = extract_data(train_path)
print('Extracting Test...')
(testX, testY) = extract_data(test_path)
print('Normalizing...')
trainX, testX = normalize(trainX, testX)
print('Saving...')

# TODO: CHANGE PATHS
with h5py.File('../data/compressed/trainX.h5', 'w') as f:
   f.create_dataset('trainX', data=trainX, compression='gzip', compression_opts=6)
with h5py.File('../data/compressed/testX.h5', 'w') as f:
   f.create_dataset('testX', data=testX, compression='gzip', compression_opts=6)
with h5py.File('../data/compressed/trainY.h5', 'w') as f:
   f.create_dataset('trainY', data=trainY, compression='gzip', compression_opts=6)
with h5py.File('../data/compressed/testY.h5', 'w') as f:
   f.create_dataset('testY', data=testY, compression='gzip', compression_opts=6)
