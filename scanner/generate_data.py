import matplotlib.pyplot as plt

from configuration import color_dataset_path, image_height, image_width, color_scale
import time
import os
import cv2
from random import shuffle
import numpy as np
from tqdm import tqdm
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator



# read single image and plot 16 transformations with matplotlib.pyplot
def plot_16():
    image = plt.imread('E:\ZPS\scanner\cards\colors\clubs.png')
    images = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    data_generator = ImageDataGenerator(rotation_range=180, brightness_range=(0.5, 1.5), shear_range=15.0, zoom_range=[1, 2])
    data_generator.fit(images)
    image_iterator = data_generator.flow(images)
    plt.figure(figsize=(16,16))
    for i in range(16):
        plt.subplot(4,4,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(image_iterator.next()[0].astype('int'))#/color_scale
        print(i)
    plt.show()



def gen_data(device_name = '/CPU:0'):
    with tf.device(device_name):
        data = []
        for label, img in tqdm(enumerate(os.listdir('cards/colors/'))):
            print(label, img)
            img = cv2.imread('cards/colors/' + img, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (image_width, image_height))
            imgs = img.reshape((1, img.shape[0], img.shape[1], 1))
            data_generator = ImageDataGenerator(rotation_range=180, brightness_range=(0.5, 1.5), shear_range=15.0, zoom_range=[1, 2])
            data_generator.fit(imgs)
            image_iterator = data_generator.flow(imgs)
            for x in range(10000):
                img_transformed = image_iterator.next()[0].astype('int')/color_scale
                #np.save('P:\card cv\data_' + str(x) + '.npy', [img_transformed, label])
                data.append([img_transformed, label])
        shuffle(data)
        np.save(color_dataset_path, data)



time_start_time = time.time()
#plot_16()
gen_data('/GPU:0')
first_time = time.time() - time_start_time
print(first_time * 1000, 'ms')
