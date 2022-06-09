#!/usr/bin/env python3

import sys

# While taking a college programming class, your instructor just taught you about ordinal values. You need to take the sample file and add up the total sum of ordinal values of characters upper and lowercase, but not anything else

def ord_sum(file):
    sum = 0
    with open(file) as open_file:
        for line in open_file:
            line = line.strip()
            for char in line:
                if char.isalpha():
                    sum += ord(char)
    return sum




def main():
    file = sys.argv[1]
    print(ord_sum(file))


if __name__ == "__main__":
    main()