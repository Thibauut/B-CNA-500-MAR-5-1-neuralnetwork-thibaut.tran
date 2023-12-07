##
## EPITECH PROJECT, 2023
## Maths
## File description:
## main.py
##

import numpy as np
import sys
import os
from parser_l import parser_c
from help import help

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class Perceptron:
    def __init__(self, nb_inputs):
        self.__nb_inputs = nb_inputs
        self.__weights = np.random.rand(nb_inputs, 2)
        self.__bias = np.random.rand(1)

    def train(self, inputs, expected_outputs, learning_rate, nb_epochs):
        for epoch in range(nb_epochs):
            output = self.predict(inputs)
            error = expected_outputs - output
            adjustments = error * sigmoid_derivative(output)
            new_adjustments = np.dot(inputs.T, adjustments)
            self.__weights += new_adjustments * learning_rate
            self.__bias += np.sum(adjustments) * learning_rate
        # print("")
        # print("result", self.predict(inputs), end="\n\n")
        print("output", output, end="\n\n")
        # print("error", error, end="\n\n")
        # print("adjustments", adjustments, end="\n\n")
        # print("new_adjustments", new_adjustments, end="\n\n")
        # print("weights", self.__weights, end="\n\n")
        # print("bias", self.__bias, end="\n\n")
        # print("expected", expected_outputs, end="\n\n")

    def predict(self, inputs):
        # print(self.__weights, end="\n\n")
        # print(self.__bias, end="\n\n")
        # print(inputs, end="\n\n")
        return sigmoid(np.dot(inputs, self.__weights) + self.__bias)

    def save(self, file):
        np.savez(file, weights=self.__weights, bias=self.__bias)

    def load(self, file):
        data = np.load(file)
        self.__weights = data["weights"]
        self.__bias = data["bias"]
        # print("weights", self.__weights)
        # print("bias", self.__bias)

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        help()

    parser = parser_c()
    parser.parse()
    if (parser.get_new() != None):
        perceptron = Perceptron(parser.get_new())
    else:
        perceptron = Perceptron(0)
        perceptron.load(parser.get_load())

    if (parser.get_mode() == "train"):
        if (os.path.isfile(parser.get_file()) == False):
            print("Error: " + parser.get_file() + " is not a file")
            exit(84)
        try:
            data = np.genfromtxt(parser.get_file(), delimiter=',')
        except ValueError:
            print("Error: " + parser.get_file() + " is not a valid file")
            exit(84)
        inputs = data[:, :-1]
        expected_outputs = data[:, -1]
        perceptron.train(inputs, expected_outputs, 0.05, 10000)
        perceptron.save(parser.get_save())
    else:
        if (os.path.isfile(parser.get_file()) == False):
            print("Error: " + parser.get_file() + " is not a file")
            exit(84)
        try:
            data = np.genfromtxt(parser.get_file(), delimiter=',')
        except ValueError:
            print("Error: " + parser.get_file() + " is not a valid file")
            exit(84)
        inputs = data[:, :-1]
        expected_outputs = data[:, -1]
        perceptron.train(inputs, expected_outputs, 0.05, 10000)

if (__name__ == "__main__"):
    main()
