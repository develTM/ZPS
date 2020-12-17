from configuration import image_width, image_height, color_scale, A_deck_path, color_model_path, value_model_path
from tqdm import tqdm
import numpy as np
import cv2
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


color_dictionary = {0:'karo', 1:'kier', 2:'pik', 3:'trefl'}
value_dictionary = {0:'10', 1:'9', 2:'as', 3:'dama',4:'jack', 5:'krol'}

def guess(path_to_file, model):
    img = cv2.imread(path_to_file, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (image_width, image_height))
    img = img.reshape((1, img.shape[0], img.shape[1], 1))
    data_generator = ImageDataGenerator(rotation_range=0, brightness_range=(1, 1), shear_range=0.0, zoom_range=[1, 2])
    data_generator.fit(img)
    image_iterator = data_generator.flow(img)
    prediction = []
    for i in range(10):
        img_transformed = image_iterator.next()[0].astype('int') / color_scale
        prediction.append(model.predict(np.array([img_transformed])))
    data = []
    local_max_probability = 0
    max_probability_list = []
    for element in prediction:
        element_list = element[0].tolist()
        data.append(element_list.index(max(element_list)))
        if max(element_list) > local_max_probability:
            local_max_probability = max(element_list)
        max_probability_list.append(local_max_probability ** 2)
        local_max_probability = 0
    if len(set(data)) > 1:
        weighted_elements = []
        i = 0
        for candidate in sorted(set(data)):
            weighted_elements.append(0)
            j = 0
            for element in data:
                if candidate == element:
                    weighted_elements[i] += max_probability_list[j]
                j += 1
            i += 1
        max_element = sorted(set(data))[weighted_elements.index(max(weighted_elements))]
    else:
        max_element = data[0]
    #max_element = max(set(data), key = data.count)
    if model is color_model:
        return color_dictionary[max_element]
    return value_dictionary[max_element]


with tf.device('/CPU:0'):
    color_model = tf.keras.models.load_model(color_model_path)
    value_model = tf.keras.models.load_model(value_model_path)
    for img in tqdm(os.listdir(A_deck_path)):
        color = guess(A_deck_path+img, color_model)
        value = guess(A_deck_path+img, value_model)
        #if color not in img or value not in img:
        print(img, color, value)


"""
flag = True
with tf.device('/CPU:0'):
    color_model = tf.keras.models.load_model(color_model_path)
    value_model = tf.keras.models.load_model(value_model_path)
    
    if flag:
        flag = False
        print(guess())
    
    time.sleep(0.01)
"""