#!/usr/bin/env python3
import sys

def main():
    path = sys.argv[1]
    dict_file = open(path, "r")
    line = dict_file.readline()
    line = line.strip()
    dict = eval(line)
    int_dict = {}
    
    for k, v in dict.items():
        int_dict[int(k)] = v

    for key in sorted(int_dict):
        if int_dict[key] == '\n':
            sep = ''
        else:
            sep = ' '
        print(int_dict[key], end=sep)

    dict_file.close()

main()

