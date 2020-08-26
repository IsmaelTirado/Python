#!/usr/bin/env python3

import sys

def main():
    paths = sys.argv[1:]
    for path in paths:
        file = open(path)
        for line in file:
            line = line.strip()
            if line != "":
                print(line, end = " ")
        file.close()
main()

