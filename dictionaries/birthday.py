#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###

def birthday_party(file):
  birthday_dictionary = {}
  with open(file) as open_file:
    for name in open_file:
      name = name.strip("\n")
      if name not in birthday_dictionary:
        birthday_dictionary[name] = 1
      elif name in birthday_dictionary:
        birthday_dictionary[name] = birthday_dictionary.get(name, 0) + 1
  
  for key in sorted(birthday_dictionary):
    print(key + " - " + str(birthday_dictionary[key]))



### MAIN FUNCTION ###
def main():
  birthday_party(sys.argv[1])

  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()