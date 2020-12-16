from configuration import image_width, image_height, color_scale, A_deck_path
import numpy as np
import cv2
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


color_dictionary = {3:'trefl', 0:'karo', 1:'kier', 2:'pik'}

def guess(path_to_file):
    img = cv2.imread(path_to_file, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (image_width, image_height))
    img = img.reshape((1, img.shape[0], img.shape[1], 1))
    data_generator = ImageDataGenerator(rotation_range=0, brightness_range=(1, 1), shear_range=1.0, zoom_range=[1, 1.5])
    data_generator.fit(img)
    image_iterator = data_generator.flow(img)
    prediction = []
    for i in range(10):
        img_transformed = image_iterator.next()[0].astype('int') / color_scale
        prediction.append(color_model.predict(np.array([img_transformed])))
    data = []
    for element in prediction:
        element_list = element[0].tolist()
        data.append(element_list.index(max(element_list)))
    max_element = max(set(data), key = data.count)
    return color_dictionary[max_element]


with tf.device('/CPU:0'):
    color_model = tf.keras.models.load_model('models\color_serious.h5')
    color_model.summary()
    error_count = 0
    guess('cards/talia_A/3 pik.png' )
    for img in os.listdir('cards/talia_A/'):
        if guess('cards/talia_A/' + img) in img:
            pass
        else:
            print(img, guess('cards/talia_A/' + img), color_model.predict(prepare('cards/talia_A/'+img)))
            error_count += 1
    print(error_count/52*100)

