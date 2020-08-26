#!/usr/bin/env python3

import sys

def main():
    path = sys.argv[1]
    file = open(path, 'r')
    
    dictionary = {"good": 0, "bad": 0}
    for line in file:
        line = line.strip()
        if line.endswith("good"):
            dictionary["good"] += 1
        elif line.endswith("bad"):
            dictionary["bad"] += 1
    print("Naughty list has " + str(dictionary["bad"]) + " people!")
    print("Nice list has " + str(dictionary["good"]) + " people!")

    file.close
main()

