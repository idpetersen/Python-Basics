#!/usr/bin/env python3

import sys

#helpers
def six_args(list):
    message = ""
    if len(list) < 6:
        message = "Sorry, no!"
    else:
        message = "FS{here_is_your_flag!}"
    return message




#main
def main():
    args = sys.argv[1:]
    print(six_args(args))


#dunder check

if __name__ == "__main__":
    main()