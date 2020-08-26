#!/usr/bin/env python3

import sys

s = (str(sys.argv[1]))
count = 0
for i in s:
    count += 1
if count > 2:
    print(str(s[0:2]) + str(s[-2:]))
else:
    print('') 