from keras.preprocessing.image import ImageDataGenerator,img_to_array, load_img
import os, cv2
import numpy as np

def cvmods(path, label, filename, data):
    image = load_img(os.path.join(path, label, filename)); image = img_to_array(image)
    image = cv2.resize(image, (64, 64))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    data.append(image)
    return data

def augment(path):
    out_dir = '../data/augmentation/out/'
    datagen = ImageDataGenerator(rotation_range=20) # Just use preprocessing function attribute
    for i, label in enumerate(sorted(os.listdir(path))):
        if (label != '.DS_Store'):
            for j, filename in enumerate(os.listdir(os.path.join(path, label))):
                data = []; save_count=0
                if (filename != '.DS_Store') & (label != '.DS_Store') & (label != 'out'):
                    cvmods(path, label, filename, data)
                    data = np.array(data); data = data.reshape(1, 64, 64, 1)
                    if not os.path.exists(out_dir + label):
                        os.makedirs(out_dir + label)
                    for batch in datagen.flow(data, save_to_dir=out_dir + label, save_format='png'):
                        save_count += 1
                        if save_count > 5:
                            break

train_path = '../data/augmentation/train'

augment(train_path)
