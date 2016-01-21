#!/usr/bin/python

import sys
import re
count = 0

## collect user input
filename = sys.argv[1]
#findwords = re.split(" ",sys.argv[2].lower())
findword = sys.argv[2]

with open (filename, "r") as myfile:
    input_file = myfile.read()
    print re.findall(findword, input_file)
#for word in findwords:
    
