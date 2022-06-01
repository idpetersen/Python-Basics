#!/usr/bin/env python3

import sys




#helpers
def is_even(file_path):
  with open(file_path) as open_file:
    for line in open_file:
      if int(line) % 2 == 0:
        print(line.strip() + " True")
      else:
        print(line.strip() + " False")




#main
def main():
  file_name = sys.argv[1]
  is_even(file_name)
  
  


#dunder dome
if __name__ == "__main__":
  main()