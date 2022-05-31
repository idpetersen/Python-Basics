#!/usr/bin/env python3

import sys

def main():
  arg_1 = sys.argv[1]
  arg_2 = sys.argv[2]

  print(arg_1)
  print(type(arg_2))
  print(str(arg_1) + str(arg_2))




if __name__ == "__main__":
  main()