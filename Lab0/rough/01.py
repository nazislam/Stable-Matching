#!/usr/bin/env python3

import random

boys = ['Abe', 'Bob', 'Col']
girls = ['Abi', 'Bea', 'Cath']

boys_pref = []
girls_pref = []

for i in range(0, len(boys)):
    girls = ['Abi', 'Bea', 'Cath']
    random.shuffle(girls)
    boys_pref.append(girls)

for i in range(0, len(girls)):
    boys = ['Abe', 'Bob', 'Col']
    random.shuffle(boys)
    girls_pref.append(boys)

print('\nParticipants:')
print('BOYS:', end=' ')
for boy in boys:
    print(boy, end=' ')
print()
print('GIRLS:', end=' ')
for girl in girls:
    print(girl, end=' ')
print('\n')

print(boys_pref)
print(girls_pref)

print('Preferences:')
# boys pref list
# v: 2
# for i in boys:
#     print(boys, end=' ')
#     for j in boys_pref:
#         print(j,)

# v: 1
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



