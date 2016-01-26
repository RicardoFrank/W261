#!/usr/bin/python


import sys
import re

REGEX_NUM = re.compile('[0-9]+')
total_num_list = []

for line in sys.stdin:
        total_num_list.append(float(re.search(REGEX_NUM,line).group()))

total_num_list.sort()

for element in total_num_list:
        print element