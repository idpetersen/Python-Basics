#!/usr/bin/env python3

import sys

# helpers
def match_ends(str_list):
  greater_than_1 = 0

  for index in str_list:
    if len(index) >= 2 and index[0] == index[-1]:
      greater_than_1 += 1


  return greater_than_1

#main
def main():
  args = sys.argv[1:]
  print(match_ends(args))


#dunder check
if __name__ == "__main__":
  main()