# Most of this code comes from https://github.com/integeruser/CASIA-HWDB1.1-cnn
import json, sys, time
import numpy as np
np.random.seed(3141)
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Flatten
from keras.models import Sequential

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
model.add(Dense(200, activation='softmax'))
myAdam = keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False)
model.compile(loss='categorical_crossentropy', optimizer=myAdam, learning_rate=0.05 metrics=['accuracy'])

# Save the model to a JSON file for easy import
timestamp = int(time.time())
with open('../output/model.json' % timestamp, 'w') as f:
    d = json.loads(model.to_json())
    json.dump(d, f, indent=4)

# Training - TODO: Change filetype input
with h5py.File(subset_filepath, 'r') as f:
    model.fit(f['trn/x'], f['trn/y'], validation_data=(f['vld/x'], f['vld/y']),
              epochs=15, batch_size=128, shuffle='batch', verbose=1)

    score = model.evaluate(f['tst/x'], f['tst/y'], verbose=0)
    print('Test score:', score[0])
    print('Test accuracy:', score[1])

    model.save_weights('../output/weights.hdf5' % (timestamp, score[1]))
