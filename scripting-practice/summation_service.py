#!/usr/bin/env python3

import sys

# Write a program, which takes two distinct integers separated by space as input and prints the sum of all the integers between them, including the two given numbers. Note that the numbers can appear in either order.

def summation_service(file):
    with open(file) as open_file:
        for line in open_file:
            sum_from_between = 0
            numbers = line.rstrip().split()
            numbers = list(map(int, numbers))
            numbers.sort()
            for integer in range(numbers[0], (numbers[1] + 1)):
                sum_from_between += integer
            print(sum_from_between)



def main():
    file = sys.argv[1]
    summation_service(file)


if __name__ == "__main__":
    main()