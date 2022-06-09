#!/usr/bin/env python3

import sys

def simple_cipher(file):
    with open(file) as open_file:
        for line in open_file:
            line = line.strip()
            message = ""
            line = line.split(".")
            for sentence in line:
                sentence = sentence.strip().split()
                if len(sentence) > 0:
                    message += sentence[0] + ' '
            return message



def main():
    file = sys.argv[1]
    print(simple_cipher(file))

if __name__ == "__main__":
    main()