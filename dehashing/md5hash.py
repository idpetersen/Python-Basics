#!/usr/bin/env python3

import hashlib

def encode():
    match_this = "5230fb8e58bfbb9c0f8ec920449ef6e3"
    translated = ""
    for num in range(0,1000):
        if num < 10:
            num = "00" + str(num)
        elif num < 100:
            num = "0" + str(num)
        else:
            num = str(num)
        flag_nums = ("FS{cabbage-wait_that's_not_right_" + num + "}")
        hashed_flag = hashlib.md5(flag_nums.encode())
        translated = hashed_flag.encode()

        if translated == match_this:
            print(num) 

def main():
    encode()

if __name__ == "__main__":
    main()

