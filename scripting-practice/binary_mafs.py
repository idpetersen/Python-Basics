#!/usr/bin/env python3


import sys




def binary_mafs(file):
    with open(file) as open_file:
        for lines in open_file:
            print(lines)
 


def main():
    file = sys.argv[1]
    binary_mafs(file)

if __name__ == "__main__":
    main()



