#!/usr/bin/python
import sys
sum = 0
for line in sys.stdin:
    sum += len(line.split())

print sum
#Please insert your code