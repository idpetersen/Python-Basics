#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def ip_logger(file):
  ip_logs = {}
  with open(file) as open_file:
    for line in open_file:
      li = list(line.split(" "))
      individual_ip = li[0]
      if individual_ip not in ip_logs:
        ip_logs[individual_ip] = 1
      elif individual_ip in ip_logs:
        ip_logs[individual_ip] = ip_logs.get(individual_ip, 0) + 1

  for key in sorted(ip_logs):
    print(key + " - " + str(ip_logs[key]))

### MAIN FUNCTION ###
def main():
  ip_logger(sys.argv[1])
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()