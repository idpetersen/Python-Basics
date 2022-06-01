#!/usr/bin/env python3

import sys

# helpers
def lines_lines_lines(file):
  message = ""
  with open(file) as open_file:
    for lines in open_file:
      if len(lines) > 1:
        message += lines.replace("\n","") + " "
  print(message.strip())
      

# main
def main():
  file = sys.argv[1]
  lines_lines_lines(file)

# dunder check

if __name__ == "__main__":
  main()