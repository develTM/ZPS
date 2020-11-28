
from tools import Clock
import os
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
from random import shuffle
import statistics
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread, imshow, subplots, show

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


clock = Clock()
clock.tick()
clock.tick()
clock.tick()
clock.tick('dupa')

clock.tick()
# read single image and plot 16 transformations with matplotlib.pyplot
"""
def plot_16(device_name):
    #with tf.device(device_name):
    image = plt.imread('images/3 karo.jpg')
    images = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        #imshow(images[0])
        #show()
    data_generator = ImageDataGenerator(rotation_range=90, brightness_range=(0.5, 1.5), shear_range=15.0, zoom_range=[.3, .8])
    data_generator.fit(images)
    image_iterator = data_generator.flow(images)
    plt.figure(figsize=(16,16))
    for i in range(16):
        plt.subplot(4,4,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(image_iterator.next()[0].astype('int'))
        print(i)
    plt.show()

#plot_16('/CPU:0')
plot_16('/GPU:0')
"""




"""
def gen_data(device_name):
    with tf.device(device_name):
        #data = []

        for i, img in tqdm(enumerate(os.listdir('cards/'))):
            #label = i

            img = cv2.imread('cards/' + img, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (180, 180))
            imgs = img.reshape((1, img.shape[0], img.shape[1], 1))
            data_generator = ImageDataGenerator(rotation_range=90, brightness_range=(0.5, 1.5), shear_range=15.0,
                                                zoom_range=[.3, .8])
            data_generator.fit(imgs)
            image_iterator = data_generator.flow(imgs)

            for x in range(100):
                img_transformed = image_iterator.next()[0].astype('int') / 255
                np.save('P:\card cv\data_' + str(x) + '.npy', img_transformed)
                #data.append([img_transformed, label])

time_start_time = time.time()
gen_data('/GPU:0')
first_time = time.time() - time_start_time
print('GPU:',first_time * 1000)

time_start_time = time.time()
gen_data('/CPU:0')
second_time = time.time() - time_start_time
print('CPU:',second_time* 1000)
print('GPU gain: ', format(second_time/first_time, '.2%')-1)
"""






