# Most of this code comes from https://github.com/integeruser/CASIA-HWDB1.1-cnn
import json, sys, datetime
import numpy as np
import keras
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
model.add(Dropout(0.1))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(10, activation='softmax')) # CHANGE TO REFLECT NUM OF CLASSES
opt = keras.optimizers.Adadelta(learning_rate = 1.0)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Save the model to a JSON file for easy import
timestamp = str(datetime.time())
with open('../model/model' + timestamp + '.json', 'w') as f:
    d = json.loads(model.to_json())
    json.dump(d, f, indent=4)


train_path = '../data/temptrn' # TODO: CHANGE LATER TO ACTUAL TRAINING SET
test_path = '../data/temptst'

# Preprocessing
(trainX, trainY) = preprocess.extract_data(train_path)
(testX, testY) = preprocess.extract_data(test_path)
trainX, testX = preprocess.normalize(trainX, testX)
# preprocess.plot_images(trainX, trainY)

# Training
log_dir="../logs/" + timestamp
# $ tensorboard --logdir ../logs/log_timestamp
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
model.fit(trainX, trainY, epochs=15, batch_size=128, verbose=1, callbacks=[tensorboard_callback]) # 15 epochs
score = model.evaluate(testX, testY, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])

model.save_weights('../model/weights' + timestamp + '.hdf5')

# sample = '../data/test.png'
# sample = preprocess.extract_data_predict(sample)
# sample = preprocess.normalize_predict(sample)
# print(model.predict(sample))
