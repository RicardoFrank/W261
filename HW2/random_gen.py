#!/usr/bin/python

import math
import sys
import random

num_vals = int(sys.argv[1])

while num_vals > 0:
        print "<"+str(random.random()*100)+",\"\">"
        num_vals -= 1