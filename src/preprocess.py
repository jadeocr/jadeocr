import imageio
import numpy as np
import h5py

f = h5py.File('../output/in1.hdf5', 'r')
dset = f['key']
data = np.array(dset[:,:,:])
file = 'test.png' # or .jpg
imageio.imwrite(file, data)

# TODO: Make sure in1.hdf5 works so we can input it into the model to predict
# Also recover the code that converted png to hdf5
