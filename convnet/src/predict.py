import json, pickle, cv2
import numpy as np
from tensorflow.python.keras.models import model_from_json


# Input and output directories
WEIGHTS_MODEL_DIR = '../model'
DICT_DIR = './dict'
TEST_DIR = '../data/tests'
TEST_IMG = '/test.png'
LOG_DIR = '../logs'

# These two are for normalizing
def extract_data_predict(path):
    data = []
    image = cv2.imread(path)
    image = cv2.resize(image, (64, 64))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    data.append(image)
    data = np.array(data)
    return (data.reshape(1, 64, 64, 1))

def normalize_predict(arr):
    # Int to float
	norm = arr.astype('float32')
	norm = norm / 255.0
	return norm


# Load the model and weights
with open(WEIGHTS_MODEL_DIR + '/model.json', 'r') as f:
    model = f.read()
    model = model_from_json(model)
model.load_weights(WEIGHTS_MODEL_DIR + '/weights.h5')
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# Allows predictions to be mapped to classes and characters
with open(DICT_DIR + '/char_dict', 'rb') as f:
    char_dict = pickle.load(f)
char_dict = dict([(value, key) for key, value in char_dict.items()])


# Use the model to predict an image
test_img = TEST_DIR + TEST_IMG
sample = normalize_predict(extract_data_predict(test_img))
sample = model.predict(sample)


# Print all predictions and probabiliites
with open(LOG_DIR + '/predictions.txt', 'w') as f:
    for i in range(len(sample[0])):
        pred = str(i) + ' ' + char_dict.get(i) + ' ' + str(sample[0][i]) + '\n'
        f.write(pred)
        print(pred)

# Print out overall prediction
maxindex = sample.argmax() # Index of largest item
print('Prediction: ', maxindex, char_dict.get(maxindex), ' ', sample[0][maxindex])
