# import required module
import os


# assign directory
directory = '/home/kali/malware_signature/bin'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    file = os.path.join(filename)
   # checking if it is a file
    if os.path.isfile(file):
        directory = file
        print (file)