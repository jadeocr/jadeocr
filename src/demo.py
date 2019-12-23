#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Code from integeruser on Github
import base64
import io
import json
import random
import sys

import h5py
from keras.models import model_from_json
import numpy as np
import PIL.Image

import utils


def create_cell(i, bitmap, tagcode, correct):
    cell = '                <div class="cell" style="animation-name: appear; animation-delay: %.1fs; animation-duration: 0.7s; \
animation-fill-mode: both; animation-iteration-count: 1;">\n' % (4.0+0.2*(i//4))

    # save bitmap as data uri
    im = PIL.Image.fromarray(np.squeeze(x, axis=0))
    buffer = io.BytesIO()
    im.save(buffer, format='png')
    cell += '                    <img alt="" src="data:image/png;base64,%s" />\n' % base64.b64encode(buffer.getvalue()).decode('ascii')

    cell += '                    <span style="animation-name: %s; animation-delay: %.1fs; animation-duration: 2s; \
animation-fill-mode: both; animation-iteration-count: 1;">%s</span>\n' % ('togreen' if correct else 'tored', random.uniform(6.0, 18.0), utils.tagcode_to_unicode(tagcode))

    cell += '                </div>\n'
    return cell


# if len(sys.argv) != 4:
#     print('Usage: %s subset_filepath model_filepath weights_filepath' % sys.argv[0])
#     sys.exit(1)

subset_filepath = '../data/HWDB1.1subset.hdf5'
model_filepath = '../output/model.json'
weights_filepath = '../output/weights.hdf5'

# load the model
with open(model_filepath) as f:
    d = json.load(f)
    model = model_from_json(json.dumps(d))

model.load_weights(weights_filepath)
model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

# test the model and output results
with h5py.File(subset_filepath, 'r') as f1, open('../output/results.html', 'wb') as f2:
    print('Evaluating the network on the test set...')
    score = model.evaluate(f1['tst/x'], f1['tst/y'], verbose=0)
    print('Test score:', score[0])
    print('Test accuracy:', score[1])

    print('Extracting some results...')
    f2.write(b'''\
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>results</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div id="wrapper">
            <span id="title">CLASSIFICATION RESULTS</span>
            <p>
            <span id="subtitle">ACCURACY: ''' + (b'%.5f' % score[1]) + b'''</span>
            <p>
            <div id="cells">
            \n''')

    for i in range(96):
        index = random.randint(0, 11947-1)
        x, y, t = f1['tst/x'][index], f1['tst/y'][index], f1['tst/t'][index][0]
        score = model.evaluate(np.expand_dims(x, axis=0), np.expand_dims(y, axis=0), verbose=0)
        f2.write(create_cell(i, x, t, score[1] == 1).encode('utf-8'))
        if (i+1)%4 == 0: f2.write(b'                <br>\n')

    f2.write(b'''\
            </div>
        </div>
    </body>
</html>''')
