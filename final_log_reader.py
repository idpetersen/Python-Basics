#!/usr/bin/env python3

import sys

def logger(file):
    read_file = file.readlines()
    ips = []
    for line in read_file:
        if "EDT;;" not in line:
            ips.append(line)
    ip = {}
    for line in ips:
        fields = line.split(";")
        if fields[2] not in ip:
            ip[fields[2]] = 1
        elif fields[4] not in ip:
            ip[fields[4]] = 1
        elif fields[2] in ip:
            ip[fields[2]] += 1
        elif fields[4] in ip:
            ip[fields[4]] += 1
       
    ip_list = sorted((value, key) for (key, value) in ip.items())
    sorted_by_ip = dict([(k, v) for v,k in ip_list])
    print(sorted_by_ip)
    
            
    

def main():
    file = sys.argv[1]
    with open(file) as open_file:
        logger(open_file)

if __name__ == "__main__":
    main()