#!/usr/bin/env python3

#Write a function which takes an integer and will find the sum of all multiples of 3 or 5 below the input.

def fives_and_threes(n):
    sum = 0
    for number in range(n):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum

def main():
    testData = 10
    testResult = fives_and_threes(testData)
    print(testResult)

main()