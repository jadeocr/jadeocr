import json, h5py
import numpy as np
import keras
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Flatten
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint, TensorBoard
# TODO: Add GPU Support and the CUDA stuff for Nvidia Jetson - You can do this part

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
model.add(Dropout(0.1))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.1))
# There's a chance you'll run into an error here because of some weird thing where the number of classes in test set ≠ train set
# In that case please let me know
model.add(Dense(3755, activation='softmax')) # TODO: CHANGE TO REFLECT NUM OF CLASSES IN ACTUAL TRAINING SET
opt = keras.optimizers.Adadelta(learning_rate = 1.0)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.summary()

with open ('../model/model.json', 'w') as f:
    f.write(model.to_json())

# Load preprocessed training data
with h5py.File('../data/compressed/trainX.h5', 'r') as f:
    trainX = f['trainX'][:]
with h5py.File('../data/compressed/testX.h5', 'r') as f:
    testX = f['testX'][:]
with h5py.File('../data/compressed/trainY.h5', 'r') as f:
    trainY = f['trainY'][:]
with h5py.File('../data/compressed/testY.h5', 'r') as f:
    testY = f['testY'][:]
print(trainY.shape, '\n', testY.shape)
print(trainX.shape, testX.shape, trainY.shape, testY.shape)

# Callbacks: Model checkpoints and tensorboard
weights_path='../model/weights.h5'
checkpoint = ModelCheckpoint(weights_path, monitor='val_accuracy', verbose=1, save_best_only=True, save_weights_only=True, mode='max')
log_dir="../logs/training_log" # View using $tensorboard --logdir ../logs/training_log
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)
callbacks_list = [checkpoint, tensorboard_callback]

# Training
model.fit(trainX, trainY, epochs=25, batch_size=128, validation_data=(testX, testY), verbose=1, callbacks=callbacks_list)
score = model.evaluate(testX, testY, verbose=0)
print('Test score:', score[0], '\n', 'Test accuracy:', score[1])

model.save_weights(weights_path)
