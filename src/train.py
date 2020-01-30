import json, h5py
import numpy as np
from tensorflow.python.keras.layers.convolutional import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers.core import Dense, Dropout, Flatten
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.callbacks import ModelCheckpoint, TensorBoard

model = Sequential()
model.add(Conv2D(64, (3, 3),
    activation='relu', padding='same', strides=(1, 1),
    input_shape=(64, 64, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (3, 3),
    activation='relu', padding='same', strides=(1, 1)))
model.add(Conv2D(64, (3, 3),
    activation='relu', padding='same', strides=(1, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(3755, activation='softmax')) # TODO - Classes
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
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
print(trainX.shape, testX.shape, trainY.shape, testY.shape)

weights_path='../model/weights.h5'
log_dir="../logs/training_log" # View using $tensorboard --logdir ../logs/training_log
checkpoint = ModelCheckpoint(weights_path, monitor='val_accuracy', verbose=1, save_best_only=True, save_weights_only=True, mode='max')
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)
callbacks_list = [checkpoint, tensorboard_callback]

model.fit(trainX, trainY, epochs=10, batch_size=128, validation_data=(testX, testY), verbose=1, callbacks=callbacks_list, shuffle=True)
model.save_weights(weights_path)
score = model.evaluate(testX, testY, verbose=0)
print('Test score:', score[0], '\n', 'Test accuracy:', score[1])
