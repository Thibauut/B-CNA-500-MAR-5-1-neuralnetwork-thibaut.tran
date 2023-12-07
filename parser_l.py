##
## EPITECH PROJECT, 2023
## Maths
## File description:
## parser.py
##

import os
import numpy as np
import argparse

class parser_c:
    def __init__(self):
        self.__parser = None
        self.__args = None
        self.__new = None
        self.__load = None
        self.__save = None
        self.__mode = None
        self.__file = None

    def parse(self):
        self.__parser = argparse.ArgumentParser()
        self.__parser.add_argument("--new", help="Creates a new perceptron with NB_INPUTS inputs.")
        self.__parser.add_argument("--load", help="Loads an existing perceptron from LOADFILE.")
        self.__parser.add_argument("--save", help="Save the perceptron’s state into SAVEFILE. If not provided, the state of the perceptron will be displayed on standard output.")
        self.__parser.add_argument("--mode", help="train or predict")
        self.__parser.add_argument("FILE", help="a file containing a list of inputs (and expected outputs) that the perceptron needs to evaluate (either for training, or predicting).")
        self.__args = self.__parser.parse_args()
        self.__new = self.__args.new
        self.__load = self.__args.load
        self.__save = self.__args.save
        self.__mode = self.__args.mode
        self.__file = self.__args.FILE
        if (self.__new == None and self.__load == None):
            print("Error: You must use --new or --load")
            exit(84)
        if (self.__new != None and self.__load != None):
            print("Error: You must use --new or --load, not both")
            exit(84)
        if (self.__mode != "train" and self.__mode != "predict"):
            print("Error: You must use --mode train or --mode predict")
            exit(84)
        if (self.__mode == "train" and self.__save == None):
            print("Error: You must use --save to save the perceptron’s state")
            exit(84)
        if (self.__mode == "predict" and self.__save != None):
            print("Error: You must not use --save to save the perceptron’s state")
            exit(84)
        if (self.__new != None):
            try:
                self.__new = int(self.__new)
            except ValueError:
                print("Error: --new must be an integer")
                exit(84)
            if (self.__new < 1):
                print("Error: --new must be greater than 0")
                exit(84)
        if (self.__load != None):
            if (os.path.isfile(self.__load) == False):
                print("Error: File", self.__load, "doesn't exist")

    def get_new(self):
        return self.__new

    def get_load(self):
        return self.__load

    def get_save(self):
        return self.__save

    def get_mode(self):
        return self.__mode

    def get_file(self):
        return self.__file

if (__name__ == "__main__"):
    parser = parser_c()
    parser.parse()
    print(parser.get_new())
    print(parser.get_load())