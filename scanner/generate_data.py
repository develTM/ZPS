from configuration import color_dataset_path, image_height, image_width, color_scale
import time
import os
import cv2
from random import shuffle
import numpy as np
from tqdm import tqdm
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def gen_data(device_name = '/CPU:0'):
    with tf.device(device_name):
        data = []

        for label, img in tqdm(enumerate(os.listdir('cards/colors/'))):
            print(label, img)
            img = cv2.imread('cards/colors/' + img, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (image_width, image_height))
            imgs = img.reshape((1, img.shape[0], img.shape[1], 1))
            data_generator = ImageDataGenerator(rotation_range=180, brightness_range=(0.5, 1.5), shear_range=15.0, zoom_range=[.3, .8])
            data_generator.fit(imgs)
            image_iterator = data_generator.flow(imgs)

            for x in range(1000):
                img_transformed = image_iterator.next()[0].astype('int')/color_scale
                #np.save('P:\card cv\data_' + str(x) + '.npy', [img_transformed, label])
                data.append([img_transformed, label])
        shuffle(data)
        np.save(color_dataset_path, data)



time_start_time = time.time()
gen_data('/GPU:0')
first_time = time.time() - time_start_time
print(first_time * 1000, 'ms')
