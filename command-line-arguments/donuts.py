#!/usr/bin/env python3

import sys

#helpers

def donuts(count):
  donut_msg = ""
  if count < 10:
    donut_msg = "Number of donuts: " + str(count)
  else:
    donut_msg = "Number of donuts: many" 

  return donut_msg


def main():
  arg_1 = int(sys.argv[1])

  print(donuts(arg_1))


if __name__ == "__main__":
  main()