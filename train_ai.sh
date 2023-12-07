#!/bin/bash

for i in {1..1000}
do
    echo "Run number: $i"
    python3 my_perceptron.py --load or_save.npz --mode train --save or_save or_logic.txt
done