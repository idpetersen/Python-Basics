#!/usr/bin/env python3

import sys


def naughty_or_nice(santa_list):
  santas_dictionary = {}
  with open(santa_list) as open_file:
    for line in open_file:
      li = list(line.split(" "))
      for word in li:
        #some_dict[key] = some_dict.get(key, 0) + 1
        if word == "good\n" or word =="good":
          santas_dictionary["good"] = santas_dictionary.get("good", 0) + 1
          santas_dictionary["Boop"] = 7
        elif word == "bad\n" or word == "bad":
          santas_dictionary["bad"] = santas_dictionary.get("bad", 0) + 1
  print("Naughty list has " + str(santas_dictionary["bad"]) + " people!")
  print("Nice list has " + str(santas_dictionary["good"]) + " people!")


def main():
  file_name = sys.argv[1]
  naughty_or_nice(file_name)
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()