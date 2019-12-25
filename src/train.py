# Most of this code comes from https://github.com/integeruser/CASIA-HWDB1.1-cnn
import json, sys, time
import numpy as np
from tensorflow import keras
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Flatten
from keras.models import Sequential
import preprocess
# TODO: Tensorboard

# This is the CNN model
# https://github.com/integeruser/CASIA-HWDB1.1-cnn/blob/master/src/3-train_subset.py
# as described in http://yuhao.im/files/Zhang_CNNChar.pdf
model = Sequential()
model.add(Conv2D(64, (3, 3), weights=[np.random.normal(0, 0.01, size=(3, 3, 1, 64)), np.zeros(64)],
    activation='relu', padding='same', strides=(1, 1),
    input_shape=(1, 64, 64), data_format='channels_first'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(128, (3, 3), weights=[np.random.normal(0, 0.01, size=(3, 3, 64, 128)), np.zeros(128)],
    activation='relu', padding='same', strides=(1, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(256, (3, 3), weights=[np.random.normal(0, 0.01, size=(3, 3, 128, 256)), np.zeros(256)],
    activation='relu', padding='same', strides=(1, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax')) # CHANGE TO REFLECT NUM OF CLASSES
opt = keras.optimizers.Adam(lr = 0.05)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Save the model to a JSON file for easy import
# timestamp = int(time.time())
# with open('../output/model.json' % timestamp, 'w') as f:
#     d = json.loads(model.to_json())
#     json.dump(d, f, indent=4)

train_path = '../data/temptrn' # TODO: CHANGE LATER TO ACTUAL TRAINING SET
test_path = '../data/temptst'

# Preprocessing
(trainX, trainY) = preprocess.extract_data(train_path)
(testX, testY) = preprocess.extract_data(test_path)
# preprocess.plot_images(trainX, trainY)

# Training
model.fit(trainX, trainY, epochs=50, batch_size=128, shuffle='batch', verbose=1)
score = model.evaluate(testX, testY, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
model.save_weights('../output/weights.hdf5' % (time.time(), score[1])) # TODO: Switch to pickle
