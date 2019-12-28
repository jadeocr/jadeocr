import json, datetime, os
import numpy as np
import keras
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Flatten
from keras.models import Sequential, model_from_json
from preprocess import extract_data_predict, normalize_predict


# Load the model and weights
with open('../model/model1.json', 'r') as f: # TODO: CHANGE THE FILE PATH AFTER TRAINING
    model = f.read()
    model = model_from_json(model)

model.load_weights('../model/weights.h5') # TODO: CHANGE THE FILE PATH AFTER TRAINING
opt = keras.optimizers.Adadelta(learning_rate = 1.0)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Allows predictions to be mapped to classes
path = '../data/temptrn' # TODO: CHANGE LATER TO ACTUAL TRAINING SET
labels = os.listdir(path)
labels.remove('.DS_Store')
print(labels)

sample = '../data/test.png' # TODO: UPDATE TO SAMPLE DATA
sample = extract_data_predict(sample) # TODO: MAKE CODE MORE ELEGANT
sample = normalize_predict(sample)
print(model.predict(sample))
