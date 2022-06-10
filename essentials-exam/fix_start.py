#!/usr/bin/env python3


import sys

def fix_it(word):
  fixed_word = ""
  fixed_word += word[0]
  for char in word[1:]:
    if char == word[0]:
      fixed_word += "*"
    else:
      fixed_word += char
  print(fixed_word)


      

def main():
  word = sys.argv[1]
  fix_it(word)


if __name__ == "__main__":
    main()