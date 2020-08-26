#!/usr/bin/env python3

import sys

#return whether num is even or odd
def even(num):
    if num % 2 == 0:
        return 'True'
    else:
        return 'False'
def main():
    #get the list of command line arguments
    #open the file at the path indicated by the first argument after our script
    #name
    file = open(sys.argv[1], "r")
    for line in file:
        num = int(line.strip("\n"))
        print(str(num), even(num))
    file.close()
    #output each number followed by the boolean value of whether it's even or
    #odd on the same line
main()


