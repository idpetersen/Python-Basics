#!/usr/bin/env python3

import sys

# helpers
def front_x(str_list):
  x_list = []
  non_x = []
  str_list.sort()
  for str in str_list:
    if str[0].lower() == "x":
      x_list.append(str)
    else:
      non_x.append(str)
  x_list.extend(non_x)
  return x_list

# main
def main():
  args = sys.argv[1:]

  print(front_x(args))

#dunderdome 
if __name__ == "__main__":
  main()