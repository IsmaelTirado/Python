#!/usr/bin/env python3

import sys

xlist = []
list = []

def main():
    for item in sys.argv[1:]:
        if item[0] == 'x':
            xlist.append(item)
        else:
            list.append(item)
    xlist.sort()
    list.sort()
    xlist.extend(list)
    print(xlist)

main()
