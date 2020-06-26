import json, h5py
import numpy as np
from tensorflow.python.keras.layers.convolutional import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers.core import Dense, Dropout, Flatten
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.callbacks import ModelCheckpoint, TensorBoard
import tensorflowjs as tfjs


# Input and output directories
DATA_DIR = '../data/full/compressed'
LOG_DIR='../logs/training_log' # View using % tensorboard --logdir ../logs/training_log
WEIGHTS_MODEL_DIR = '../model'

# Hyperparameters
NUM_OF_CLASSES = 100
NUM_OF_EPOCHS = 20
BATCH_SIZE = 64


# Model Structure
model = Sequential()
model.add(Conv2D(64, (3, 3),
    activation='relu', padding='same', strides=(1, 1),
    input_shape=(32, 32, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (3, 3),
    activation='relu', padding='same', strides=(1, 1)))
model.add(Conv2D(64, (3, 3),
    activation='relu', padding='same', strides=(1, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(NUM_OF_CLASSES, activation='softmax')) # Modify to number of classes

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

with open (WEIGHTS_MODEL_DIR + '/model.json', 'w') as f:
    f.write(model.to_json())


# Load preprocessed training data
with h5py.File(DATA_DIR + '/trainX.h5', 'r') as f:
    trainX = f['trainX'][:]
with h5py.File(DATA_DIR + '/testX.h5', 'r') as f:
    testX = f['testX'][:]
with h5py.File(DATA_DIR + '/trainY.h5', 'r') as f:
    trainY = f['trainY'][:]
with h5py.File(DATA_DIR + '/testY.h5', 'r') as f:
    testY = f['testY'][:]
print(trainX.shape, testX.shape, trainY.shape, testY.shape)


checkpoint = ModelCheckpoint(WEIGHTS_MODEL_DIR, monitor='val_accuracy', 
    verbose=1, save_best_only=True, save_weights_only=True, 
    mode='max')
tensorboard_callback = TensorBoard(log_dir=LOG_DIR, histogram_freq=1)
callbacks_list = [checkpoint, tensorboard_callback]


model.fit(trainX, trainY, epochs=NUM_OF_EPOCHS, batch_size=BATCH_SIZE, 
    validation_data=(testX, testY), verbose=1, 
    callbacks=callbacks_list, shuffle=True)

model.save_weights(WEIGHTS_MODEL_DIR + '/weights.h5')

score = model.evaluate(testX, testY, verbose=0)
print('Test score:', score[0], '\n', 'Test accuracy:', score[1])

# Save JS Model
tfjs.converters.save_keras_model(model, '../js/')
