import my_perceptron as funcs
import numpy as np

class MLP:
    def __init__(self, nb_inputs, nb_hidden):
        self.__nb_inputs = nb_inputs
        self.__nb_hidden = nb_hidden
        self.__weights1 = np.random.rand(nb_inputs, nb_hidden)
        self.__weights2 = np.random.rand(nb_hidden, 1)
        self.__bias1 = np.random.rand(nb_hidden)
        self.__bias2 = np.random.rand(1)

    def train(self, inputs, expected_outputs, learning_rate, nb_epochs):
        for epoch in range(nb_epochs):
            # Forward propagation
            hidden_layer_output = funcs.sigmoid(np.dot(inputs, self.__weights1) + self.__bias1)
            output = funcs.sigmoid(np.dot(hidden_layer_output, self.__weights2) + self.__bias2)

            # Backward propagation
            error = expected_outputs - output
            d_output = error * funcs.sigmoid_derivative(output)

            error_hidden_layer = d_output.dot(self.__weights2.T)
            d_hidden_layer = error_hidden_layer * funcs.sigmoid_derivative(hidden_layer_output)

            # Updating Weights and Biases
            self.__weights2 += hidden_layer_output.T.dot(d_output) * learning_rate
            self.__bias2 += np.sum(d_output,axis=0) * learning_rate
            self.__weights1 += inputs.T.dot(d_hidden_layer) * learning_rate
            self.__bias1 += np.sum(d_hidden_layer,axis=0) * learning_rate