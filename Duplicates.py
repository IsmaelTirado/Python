#!/usr/bin/env python3

#Write a function that takes a list as a parameter and returns a second list composed of any objects that appear more than once in the original list
#eg. duplicates([1,2,3,6,7,3,4,5,6])

def duplicates(original):
    itemCounts = {}
    for item in original:
        if item in itemCounts:
            itemCounts[item] += 1
        else:
            itemCounts[item] = 1

    duplicatesList = []
    for key, value in itemCounts.items():
        if value > 1:
            duplicatesList.append(key)
    return duplicatesList

def main():
    testList = [1,2,3,6,7,3,4,5,6]
    print(duplicates(testList))
main()