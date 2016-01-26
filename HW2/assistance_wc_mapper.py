#!/usr/bin/python

import sys
import re

for line in sys.stdin:

#split line into words and print out if target is found for reduce
        for element in re.findall('assistance', line):
                print element