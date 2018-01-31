#!/usr/bin/env python3

# timing operations

import time

start = time.time()
print('Hello, World!')
for i in range(5):
    print(i)
end = time.time()

print('\nElapsed time:')
print(end-start)
