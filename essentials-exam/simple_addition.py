#!/usr/bin/env python3

import sys


def simp_add(file):
  # opening the file as ope_file
    with open(file) as open_file:
      # looping through each line of the file
        for line in open_file:
          # setting a blank sum to be added to later
            sum = 0
          # splitting each line into a list to beable to iterate through later
            numbers = line.rstrip().split()
          # using map to create an updated list with the entries as floats
            numbers = list(map(float, numbers))
          # iterating through each of the lists and adding the two numbers together
            for integer in numbers:
                sum += integer
            # printing out each iteration
            print(sum)


def main():
  # Grabbing the file name from the command line
    file = sys.argv[1]
  # Calling function with the file name
    simp_add(file)


if __name__ == "__main__":
    main()
