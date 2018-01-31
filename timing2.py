#!/usr/bin/env python3

import time

start = time.process_time()
print('Hello, World!')
for i in range(5):
    print(i)

print('\nElapsed time:')
print(time.process_time()-start)
