#!/usr/bin/env python3

from zlib import crc32

data = open("pngflag.png",'rb').read()
index = 12

ihdr = bytearray(data[index:index+17]) #ihdr
width_index = 7 #width
height_index = 11 #height

for x in range (1,2000):
    height = bytearray(x.to_bytes(2,'big'))
    for y in range(1,2000):
        width = bytearray(y.to_bytes(2,'big'))
        for h in range(len(height)):
            ihdr[height_index - h] = height[-h -1]
        for w in range(len(width)):
            ihdr[width_index - w] = width[-w -1]
        if hex(crc32(ihdr)) == '0xc615b7e2': #crc starting with 0x this is the checksum. 
            print("width: {} height: {}".format(width.hex(),height.hex()))
        for i in range(len(width)):
            ihdr[width_index - i] = bytearray(b'\x00')[0]