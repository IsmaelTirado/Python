#!/usr/bin/env python3

import sys

def name_counts(path):
    file = open(path, 'r')
    names_to_counts = {}
    for line in file:
        line = line.strip()
        if not line in names_to_counts:
            names_to_counts[line] = 1
        else:
            names_to_counts[line] += 1
    file.close()
    return names_to_counts

def main():
    fileName = sys.argv[1]
    names = name_counts(fileName)
    for name, count in names.items():
        print(name + " - " + str(count))

main()

