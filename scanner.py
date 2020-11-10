#sauce:
#Playing card detection with YOLO:
#https://www.youtube.com/watch?v=pnntrewH0xg
#Python neurals:
#https://towardsdatascience.com/image-recognition-with-machine-learning-on-python-convolutional-neural-network-363073020588

#How to?
#1. convert image to greyscale
#2. apply gaussian blur
#3. apply adaptative thresholding
#4. find segments using probabilistic Hough transform, locate biggest rectangle
#5. resize found image to rectangle/approximate polygon
#6. locate top_left/bot_right corner
#7. extract mxn rectangle with value and color
#8. use one network to identify value and other for color
#ad.8 training set: mxn rectangles (slight variations?), same for both networks

#might prefer locate the value directly, even if can't see whole card, (exchange steps 1-4)



#simple 1-layer useless neural
import numpy as np


class NeuralNetwork():

    def __init__(self):
        # seeding for random number generation
        np.random.seed(1)

        # converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        # applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        # training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            # siphon the training data via  the neuron
            output = self.predict(training_inputs)

            # computing error rate for back-propagation
            error = training_outputs - output

            # performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def predict(self, inputs):
        # passing the inputs via the neuron to get output
        # converting values to floats

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":
    neural_network = NeuralNetwork()

    print("Weights before training: ")
    print(neural_network.synaptic_weights)
    print("Predicting [0, 0, 1]: ", neural_network.predict(np.array([0, 0, 1])))

    # training data
    training_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_outputs = np.array([[0, 1, 1, 0]]).T   #.T transponuje macierz

    neural_network.train(training_inputs, training_outputs, 100000)

    print("Weights After Training: ")
    print(neural_network.synaptic_weights)

    print("Predicting [0, 0, 1]: ",neural_network.predict(np.array([0, 0, 0])))
    print("Predicting [1, 1, 1]: ", neural_network.predict(np.array([0, 0, 1])))

