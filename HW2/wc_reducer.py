
import sys
import operator
import re

#build reducer able to handle input from multiple mappers
#input comes in as "word,count"
#build a vocab, sort, and then reduce

total_wc_list = []

#for some reason my mapper outputs a new line between each entry
#so just fixing that nonsense the stupid way

for line in sys.stdin:
    if line != ("" or "\n"):
        total_wc_list.append(line)

total_wc_list.sort()
#print total_wc_list

cur_word = ""
cur_sum = 0
first_word = True
output = {}

#re-aggregate the counts
for entry in total_wc_list:

    if len(entry.split('\t')) != 2:
            print entry
    word = entry.split('\t')[0]
        #count = re.sub("[^0-9]","",entry.split('\t')[1])
    count = int(re.sub("\n","",entry.split('\t')[-1]))
        #print word+","+str(count)

    if word in output:
        output[word] += count
    else:
        output[word] = count

#pick the top 10.  Could be done more efficiently by tracking
#while aggregating above, but the section below is easy and cheap

sorted_out = sorted(output.items(), key = lambda x: int(x[1]), reverse=True)

cur_count = 0

for key, value in sorted_out:
    print key +'\t'+ str(value)
    cur_count += 1

    if cur_count == 10:
        break
