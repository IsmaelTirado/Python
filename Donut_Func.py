#!/usr/bin/env python3

import sys

def donut_count(num1):
    if num1 < 10:
        return 'Number of donuts: ' + str(num1)
    else:
        return 'Number of donuts: many'
#print(sys.argv[1])
num = int(sys.argv[1])
print(donut_count(num))