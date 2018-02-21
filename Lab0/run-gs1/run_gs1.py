#!/usr/bin/env python3

import gs1
import sys
import random

def generate_random_number():
    return random.randint(1, 55000)

def main():

    for i in range(0, 20): 
        trial_input = generate_random_number()
        gs1.main(trial_input)
    

if __name__ == '__main__':
    main()

