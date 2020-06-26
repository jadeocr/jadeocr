import os, h5py, cv2
import numpy as np


# Input and output directories
TRAIN_PATH = '../data/full/train'
TEST_PATH = '../data/full/test'
OUTPUT_DIR = '../data/full/compressed'
IMG_SIZE = 48


def extract_data(path):
    labels = []
    data = []
    numOfItems = 0

    for i, label in enumerate(sorted(os.listdir(path))):
        if (label != '.DS_Store'): # Escapes annoying MacOS problem
            for j, filename in enumerate(os.listdir(os.path.join(path, label))):
               image = cv2.imread(os.path.join(path, label, filename))
               image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
               image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
               data.append(image)
               labels.append(i-1)
               numOfItems += 1

    data = np.array(data)
    
    return (data.reshape(numOfItems, IMG_SIZE, IMG_SIZE, 1), np.array(labels))


def normalize(trainX, testX):
	train_norm = trainX.astype('float32') / 255.0
	test_norm = testX.astype('float32') / 255.0
	return train_norm, test_norm


print('Extracting Train...')
(trainX, trainY) = extract_data(TRAIN_PATH)
print('Extracting Test...')
(testX, testY) = extract_data(TEST_PATH)
print('Normalizing...')
trainX, testX = normalize(trainX, testX)
print('Saving...')
print(trainX.shape, testX.shape, trainY.shape, testY.shape)


# Saves
with h5py.File(OUTPUT_DIR + '/trainX.h5', 'w') as f:
   f.create_dataset('trainX', data=trainX, compression='gzip', compression_opts=6)
with h5py.File(OUTPUT_DIR + '/testX.h5', 'w') as f:
   f.create_dataset('testX', data=testX, compression='gzip', compression_opts=6)
with h5py.File(OUTPUT_DIR + '/trainY.h5', 'w') as f:
   f.create_dataset('trainY', data=trainY, compression='gzip', compression_opts=6)
with h5py.File(OUTPUT_DIR + '/testY.h5', 'w') as f:
   f.create_dataset('testY', data=testY, compression='gzip', compression_opts=6)

print('Done!')
