##
## EPITECH PROJECT, 2023
## Maths
## File description:
## help.py
##

import sys

def help():
    print("USAGE")
    print("\t./my_perceptron [--new NB_INPUTS | --load LOADFILE] [--save SAVEFILE] --mode [train | predict] FILE")
    print("DESCRIPTION")
    print("\t--new\t\tCreates a new perceptron with NB_INPUTS inputs.")
    print("\t--load\t\tLoads an existing perceptron from LOADFILE.")
    print("\t--save\t\tSave the perceptron’s state into SAVEFILE. If not provided, the state of the perceptron will be displayed on standard output.")
    print("\tFILE\t\ta file containing a list of inputs (and expected outputs) that the perceptron needs to evaluate (either for training, or predicting).")
    sys.exit(0)

if (__name__ == "__main__"):
    help()