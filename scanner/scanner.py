from configuration import image_width, image_height, color_scale
import numpy as np
import cv2
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


color_dictionary = {0:'clubs', 1:'diamonds', 2:'hearts', 3:'spades'}

def prepare(path_to_file):
    img = cv2.imread(path_to_file, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (image_width, image_height))
    img = img.reshape((1, img.shape[0], img.shape[1], 1))
    data_generator = ImageDataGenerator(rotation_range=0, brightness_range=(1, 1), shear_range=1.0, zoom_range=[1, 1])
    data_generator.fit(img)
    image_iterator = data_generator.flow(img)
    img_transformed = image_iterator.next()[0].astype('int') / color_scale
    data = np.array([img_transformed])
    return data


def guess(path_to_file):
    prediction = color_model.predict(prepare(path_to_file))
    prediction = prediction[0].tolist()
    return color_dictionary[prediction.index(max(prediction))]


with tf.device('/CPU:0'):
    color_model = tf.keras.models.load_model('models\color_demo.h5')
    color_model.summary()
    for img in os.listdir('cards/colors/'):
        print(img, guess('cards/colors/' + img), color_model.predict(prepare('cards/colors/'+img)))

