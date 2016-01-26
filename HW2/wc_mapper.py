
import sys
import re

#in the mapper, we take each line and split
#and we also count words at the end to reduce
#transfer to the reducer

word_list = []
word_seen = []

for line in sys.stdin:
    
    #grab only content for word count
    tmp = line.split('\t')

    if len(tmp) != 4:
        content = tmp[-1]
    else:
        content = tmp[-2] + tmp[-1]

        #split line into words and add word if new and add to list
        for element in re.split("[, \.\n]+", content):

            if element not in word_seen:
                word_seen.append(element)
            word_list.append(element)

#prepare for counting

word_list.sort()
word_seen.sort()
cur_pos = 0
cur_count = 0
word_count = {}
end_of_list = False

#go through word-by-word counting until next word is seen
for word in word_seen:
    while (word_list[cur_pos] == word) and (end_of_list is False):
        cur_count += 1

        if cur_pos == (len(word_list) - 1):
            end_of_list = True

        else:
            cur_pos += 1

    word_count[word] = cur_count
    cur_count = 0

#print word_count
for key, value in word_count.items():
    print str(key + '\t' + str(value))