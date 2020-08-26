#!/usr/bin/env python3

import sys

def main():
    path = sys.argv[1]
    logFile = open(path, "r")
    ipCounts = {}

    for line in logFile:
        line = line.strip()
        ip = line.split(" - - ")[0]
        if ip not in ipCounts:
            ipCounts[ip] = 1
        else:
            ipCounts[ip] += 1

    sortedIpCounts = sorted(list(ipCounts.keys()))
    
    for ip in sortedIpCounts:
         print(ip + " - " + str(ipCounts[ip]))

    logFile.close()

main()

