import tensorflow as tf



color_model = tf.keras.models.load_model('models\color_demo.h5')

color_model.summary()

color_model.leave()

