#!/usr/bin/python

import sys

word_count = 0

for line in sys.stdin:
        if line != ("" or "\n"):
                word_count += 1

print word_count