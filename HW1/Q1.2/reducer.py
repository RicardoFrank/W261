#!/usr/bin/python

import sys
import re

filelist = re.split(" ",sys.argv[1].lower())

sum = 0

for file_chunk in filelist:
    with open (file_chunk, "r") as myfile:
        input_file = myfile.read()
        sum += len(input_file.split())

print sum