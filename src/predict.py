import json, datetime, os, pickle
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
# print(labels)

# Use the model to predict an image
test_img = '../data/test.png' # TODO: UPDATE TO SAMPLE DATA
sample = normalize_predict(extract_data_predict(test_img))
sample = model.predict(sample)
# print(sample)
maxindex = sample.argmax() # Index of largest item
# print(int(labels[maxindex]))

with open('char_dict', 'rb') as f:
    char_dict = pickle.load(f)
char_dict = dict([(value, key) for key, value in char_dict.items()])

print('Prediction: ', char_dict.get(int(labels[maxindex]))) # Final Prediction
