#!/usr/bin/env python3


import sys
import ast


### HELPER FUNCTIONS (IF NECESSARY) ###
def haikuify(file):
  haiku = ""
  data = file.read()
  haiku_dict = ast.literal_eval(data)
  key_values = haiku_dict.items()
  int_haiku_dict = {int(key): str(value) for key, value in key_values}
  for key in sorted(int_haiku_dict):
    if int_haiku_dict[key] != "\n" and int_haiku_dict[key + 1] != "\n":
      haiku += (int_haiku_dict[key] + ' ')
    else:
      haiku += int_haiku_dict[key]
  return haiku

### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  with open(file_name) as file:
    print(haikuify(file), end="")
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()