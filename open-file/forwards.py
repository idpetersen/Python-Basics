#!/usr/bin/env python3

import sys




#helpers
def forwards_is_backwards(file):
  with open(file) as open_file:
    for line in open_file:
      if line.strip() == line[::-1].strip():
        print("True")
      else:
        print("False")




#main
def main():
  forwards_is_backwards(sys.argv[1])
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()