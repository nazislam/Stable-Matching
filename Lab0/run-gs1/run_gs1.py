#!/usr/bin/env python3

import gs1
import sys
import random
from subprocess import call

def generate_random_number():
    return random.randint(1, 5500)

def main():

    for i in range(0, 20): 
        trial_input = generate_random_number()
        gs1.main(trial_input)
    
    call(["/usr/bin/gnuplot", "-persist", "model.gpt"])

if __name__ == '__main__':
    main()

