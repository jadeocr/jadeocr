from keras.models import model_from_json
import h5py
import numpy
import os

subset_filepath = "../data/HWDB1.1subset.hdf5"

with open('../output/model.json', 'r') as json_file:
    loaded_json = json_file.read()

model = model_from_json(loaded_json)
model.load_weights('../output/weights.hdf5')
model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

# It works! TODO: Prediction
with h5py.File(subset_filepath, 'r') as f:
    score = model.evaluate(f['tst/x'], f['tst/y'], verbose=0)
    print('Test score:', score[0])
    print('Test accuracy:', score[1])
