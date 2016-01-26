
#the mapper is changed to keep count of all words seen in the dictionary
#so the reducer can filter and compute

import sys
import re

## collect user input

input = []

for line in sys.stdin:
    input.append(line)
        #matches = re.findall('\bassistance\b',line)
        #if len(matches) > 0:
        #       print matches

output = {}
output["1"] = 0
output["0"] = 0
output["1 words"] = ""
output["0 words"] = ""
output["1 assistance"] = 0
output["0 assistance"] = 0
output["1 word count"] = 0
output["0 word count"] = 0
output["1 list"] = ""
output["0 list"] = ""

skip_email = False

#go through line-by-line and count assistance
#note any new words in spam / not spam
#and count spam emails

for line in input:

    skip_email = False

    if len(line.split('\t')) == 4:
        tmp = line.split('\t')
        all_text = tmp[2] + " " + tmp[3]
        true_label = tmp[1]

        #empty subject
    elif len(line.split('\t')) == 3:
        tmp = line.split('\t')
        all_text = tmp[-1]
        true_label = tmp[1]

    else:
        skip_email = True

    clean_line = re.split("[, \.\n]+", all_text)

    if skip_email is False:
        #count number of times assistance is present
        #output["assistance"] += len(re.findall("assistance",clean_line))

        #append the email text
        id = tmp[0]
        output[id] = all_text
        
        #add words seen and increment keys
        tokens = re.split("[, \.\n]+", all_text)
        for word in tokens:
            if word in output.keys():
                output[word] += 1
            else:
                output[word] = 1
        

        #if spam
        if tmp[1] == "1":
            #add id to spam list
            output["1 list"] += id + " "

            #check to see if we've seen the word before in spam
            for word in re.split("[, \.\n]+", all_text):
                if word not in output["1 words"].split(' '):
                    output["1 words"] = output["1 words"] + word + " "

            #increment spam count, assistance in spam count, and words in spam
            matches = re.findall(r'\bassistance\b',all_text)

            output["1 assistance"] += len(matches)
            output["1 word count"] += len(clean_line)
            output["1"] += 1

                #if len(matches) > 0:
                #       print line
        #not spam
        else:
            #add id to not spam list
            output["0 list"] += id + " "

            #check to see if we've seen the word before in not spam
            for word in re.split("[, \.\n]+", all_text):
                    if word not in output["0 words"].split(' '):
                            output["0 words"] = output["0 words"] + word + " "

            #increment not spam count, assistance in not spam count, and words
            #not in spam
            matches = re.findall(r'\bassistance\b',all_text)
            output["0 assistance"] += len(matches)
            output["0 word count"] += len(clean_line)
            output["0"] += 1

                        #if len(matches) >0:
                        #       print line
#print all info
for key, value in output.items():
    print key + "\t" + str(value)