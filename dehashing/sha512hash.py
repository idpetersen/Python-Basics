#!/usr/bin/env python3

import hashlib

def encode():
    match_this = "3052cfcc32d0c7c47138649872f3d7ef74413330a8dc1b29c9d21c991dc4d44a19ece2f4e3ed5e3cb7bbac3a05a7624d1010fd502265e7a636960349698342e2"
    first = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]
    second = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]
    third = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]
    for f in first:
        for s in second:
            for t in third:
                flag_combo = f + s + t
                flag_nums = ("FS{hash-I_had_corned_beef_and_hash_" + flag_combo + "}")
                hashed_flag = hashlib.sha512(flag_nums.encode())
                translated = hashed_flag.hexdigest()

                if translated == match_this:
                    print(flag_combo) 

def main():
    encode()

if __name__ == "__main__":
    main()