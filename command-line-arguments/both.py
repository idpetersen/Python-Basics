#!/usr/bin/env python3

import sys


#helpers
def both_ends(s):
  output_string = ""

  if len(s) >= 2:
    # when trying to go backwards on the indecies, no endpoint is needed, if we specify for example "-1" it will not include the last character of the string
    output_string = s[0:2] + s[-2:]
  return output_string

#main
def main():
  arg_1 = sys.argv[1]

  print(both_ends(arg_1))


#dunder check

if __name__ == "__main__":
  main()