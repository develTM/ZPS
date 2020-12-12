from configuration import image_width, image_height
import numpy as np
import cv2
import tensorflow as tf


def prepare(path_to_file):
    img = cv2.imread(path_to_file, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (image_width, image_height))
    img = img.reshape((1, img.shape[0], img.shape[1], 1))

    img = img.astype('int')
    data = np.array(img)

    return data


color_model = tf.keras.models.load_model('models\color_demo.h5')
color_model.summary()
# clubs = prepare('E:\ZPS\scanner\cards\colors\clubs.png')

prediction = color_model.predict(prepare('E:\ZPS\scanner\cards\colors\clubs.png'))
print(prediction)

prediction = color_model.predict(prepare('E:\ZPS\scanner\cards\colors\diamonds.png'))
print(prediction)

prediction = color_model.predict(prepare('E:\ZPS\scanner\cards\colors\hearts.png'))
print(prediction)

prediction = color_model.predict(prepare('E:\ZPS\scanner\cards\colors\spades.png'))
print(prediction)


#prepare('E:\ZPS\scanner\cards\colors\clubs.png')

