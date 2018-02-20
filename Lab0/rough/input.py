#!/usr/bin/env python3

a = [1, 2, 3, 4, 5]

while True:
    for i in a:
        print(i)
    k = input("Another trial?")
    if (k == 'n'):
        break
    else:
        continue
