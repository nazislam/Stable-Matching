#!/usr/bin/env python3


import random

boys = ['Abe', 'Bob', 'Col']
girls = ['Abi', 'Bea', 'Cath']

boys_pref = []
girls_pref = []

for i in range(0, len(boys)):
    random.shuffle(girls)
    boys_pref.append(girls)
    girls = ['Abi', 'Bea', 'Cath']

for i in range(0, len(girls)):
    random.shuffle(boys)
    girls_pref.append(boys)
    boys = ['Abe', 'Bob', 'Col']

print(boys_pref)
print(girls_pref)

for i in range(0, len(boys)):
    print(boys[i], ':', end='  ')
    for j in boys_pref[i]:
        print(j, end='  ')
    print()

for i in range(0, len(girls)):
    print(girls[i], ':', end='  ')
    for i in girls_pref[i]:
        print(i, end='  ')
    print()










