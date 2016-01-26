
#!/usr/bin/env python

import sys
import math

top_10_counter = 10
total_lines = 0
line_counter = 0
tmp = []

for line in sys.stdin:
        line_counter += 1
        tmp.append(line)

total_lines = line_counter
line_counter = 0

for line in tmp:

        #print top 10 or bottom ten
        if top_10_counter > 0:
                print "<" + str(line.strip('\n')) + ",\"\">"
                top_10_counter -= 1
                line_counter += 1

        elif (total_lines - line_counter) > 10:
                line_counter += 1

        else:
                print "<" + line.strip('\n') + ",\"\">"
                line_counter += 1