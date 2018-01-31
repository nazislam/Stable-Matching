#!/usr/bin/env python3

import random

#---> SUITORS AND GIRLS
suitors = [
            'Abe', 'Bob', 'Col', 'Dan', 'Ed', 
            'Fred', 'Gav', 'Hal', 'Ian', 'Jon'
          ]

girls = [
            'Abi', 'Bea', 'Cath', 'Dee', 'Eve',
            'Fay', 'Gay', 'Hope', 'Ivy', 'Jan'
        ]


#---> PARTICIPANTS LIST
print('Participants:')
for suitor in suitors:
    print(suitor, end="  ")
print()
for girl in girls:
    print(girl, end="  ")
print()
print()


# works: but needs improvement
print('Preferences:')
for suitor in suitors:
    name = suitor
    suitor = []
    random.shuffle(girls)
    suitor = girls
    print(name, ': ', end='')
    for girl in suitor:
        print(girl, end='  ')
    print()






