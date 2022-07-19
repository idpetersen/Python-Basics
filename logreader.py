#!/usr/bin/env python3

import sys

def logger(file):
    ftp_req = []
    read_file = file.readlines()
    for line in read_file:
        if "FTP;Request" in line:
            ftp_req.append(line)
    ftp_by_ip = {}
    for line in ftp_req:
        fields = line.split(";")
        if fields[2] not in ftp_by_ip:
            ftp_by_ip[fields[2]] = 1
        else:
            ftp_by_ip[fields[2]] += 1
    ftp_by_ip_list = sorted((value, key) for (key, value) in ftp_by_ip.items())
    sorted_ftp_by_ip = dict([(k, v) for v,k in ftp_by_ip_list])
    print(sorted_ftp_by_ip)
    
            
    

def main():
    file = sys.argv[1]
    with open(file) as open_file:
        logger(open_file)

if __name__ == "__main__":
    main()