#!/usr/bin/env python3

import sys

def is_palindrome(str):
    return str == str[::-1]

def main():
    path = sys.argv[1]
    file = open(path, "r")
    for line in file:
        line = line.strip("\n")
        print(is_palindrome(line))
    file.close
main()

